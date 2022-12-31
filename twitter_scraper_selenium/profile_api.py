#!/usr/bin/env python3

from .driver_initialization import Initializer
import logging
from .scraping_utilities import Scraping_utilities
import json
from typing import Union
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire.utils import decode
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Profile_api:
    def __init__(self, username, browser, proxy, headless, tweets_count):
        self.username = username
        self.browser = browser
        self.proxy = proxy
        self.headless = headless
        self.driver = ''
        self.data_dict = {}
        self.tweets_count = tweets_count

    def start_driver(self):
        """changes the class member driver value to driver on call"""
        self.driver = Initializer(
            self.browser, self.headless, self.proxy).init()

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

    def find_entries(self, response):
        try:
            tweets = response["data"]["user"]["result"]["timeline_v2"]["timeline"][
                "instructions"
            ][0]["entries"]
            return tweets
        except KeyError:
            tweets = response["data"]["user"]["result"]["timeline_v2"]["timeline"][
                "instructions"
            ][1]["entries"]
            return tweets

    def augment_data(self, tweets):
        try:
            for tweet in tweets:
                try:
                    tweet_results = tweet["content"]["itemContent"]["tweet_results"]['result']
                    rest_id = tweet_results['rest_id']
                    user_details = tweet_results['core']['user_results']['result']
                    del tweet_results['core']
                    self.data_dict[rest_id] = {
                        "tweet_url": f'https://twitter.com/{self.username}/status/{rest_id}',
                        'tweet_details': tweet_results,
                        "user_details": user_details
                    }

                except KeyError:
                    continue
        except Exception as ex:
            logger.exception('Error at augment_data : {}'.format(ex))

    def find_cursor(self, tweets):
        try:
            cursor = None
            for tweet in tweets:
                try:
                    if tweet["content"]["cursorType"] == "Bottom":
                        cursor = tweet["content"]["value"]
                        break
                except KeyError:
                    continue
            return cursor
        except Exception as ex:
            logger.exception("Find Cursor : ", ex)

    def get_headers_and_uid(self, url, retry=5):
        try:
            self.start_driver()
            self.driver.get(url)
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '[data-testid="tweet"]')
                )
            )
            header = {}
            uid = None
            user_id = None
            for request in self.driver.requests:
                if "UserTweets" in request.url:
                    header = request.headers
                    uid = request.url.split("/")[-2]
                elif "UserByScreenName" in request.url:
                    body = decode(
                        request.response.body,
                        request.response.headers.get(
                            "Content-Encoding", "identity"),
                    )
                    data = json.loads(body.decode())
                    user_id = data["data"]["user"]["result"]["rest_id"]
            self.close_driver()
            return [dict(header), uid, user_id]
        except TimeoutException:
            retry -= 1
            self.close_driver()
            return self.get_headers_and_uid(url, retry)
        except Exception as ex:
            logger.exception(ex)
            self.close_driver()
            return [dict(header), uid, user_id]

    def scrape(self):
        try:
            header, uid, user_id = self.get_headers_and_uid(
                f"https://twitter.com/{self.username}")
            if not uid:
                logger.error(f'Failed to find UID for {self.username}')
            cursor = None
            params = None
            while len(self.data_dict) < self.tweets_count:
                params = Scraping_utilities.build_params_for_profile(
                    user_id, cursor)
                response = Scraping_utilities.make_http_request_with_params(
                    f"https://twitter.com/i/api/graphql/{uid}/UserTweets", params, header, self.proxy)
                if response:
                    entries = self.find_entries(response)
                    self.augment_data(entries)
                    cursor = self.find_cursor(entries)
                    logger.setLevel(logging.INFO)
                    logger.info('Number of tweets scraped: {}'.format(
                        len(self.data_dict)))
                else:
                    logger.warning('Failed to make request!')
                    break

            data = dict(list(self.data_dict.items())
                        [0:int(self.tweets_count)])
            return data
        except Exception as ex:
            logger.warning('Error at scrap : {}'.format(ex))


def scrape_profile_with_api(username: str, proxy: Union[str, None] = None,
                            tweets_count: int = 10,
                            output_filename: Union[str, None] = None,
                            output_dir: Union[str, None] = os.getcwd(),
                            browser: str = 'firefox',
                            headless: bool = True):
    """Function to scrape twitter Topic from URL using Twitter's API.

    Args:
        username (str): username of the twitter account.
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        tweets_count (int, optional): Number of Tweets to scrape. Defaults to 10.
        output_filename (Union[str, None], optional): Name of the output JSON file. Defaults to None.
        output_dir (Union[str, None], optional): Directory where to save the file. Defaults to os.getcwd().
        browser (str, optional): Which browser to use for extracting out graphql key. Defaults to 'firefox'.
        headless (bool, optional): Whether to run browser in headless mode?. Defaults to True.
    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    profile_api_scraper = Profile_api(
        username=username, browser=browser, tweets_count=tweets_count, proxy=proxy, headless=headless)
    data = profile_api_scraper.scrape()
    if output_filename and len(data) > 0:
        path = os.path.join(output_dir, "{}.json".format(output_filename))
        mode = 'a'
        if os.path.exists(path):
            mode = 'r'
        with open(path, mode, encoding='utf-8') as file:
            if mode == 'r':  # if mode is read mode it means file already exists and may content data
                try:
                    file_content = file.read()  # read the file
                    content = json.loads(file_content.strip())  # load the data
                except json.decoder.JSONDecodeError:
                    # if the stored data is invalid data
                    logger.warning('Invalid JSON Detected!')
                    content = []
                data.update(content)
        with open(path, 'w', encoding='utf-8') as file_in_write_mode:
            # open the file in writing mode to erase the data and dump the current data
            json.dump(data, file_in_write_mode)
            logger.setLevel(logging.INFO)
            logger.info('Data was saved to {}'.format(path))
    else:
        return data
