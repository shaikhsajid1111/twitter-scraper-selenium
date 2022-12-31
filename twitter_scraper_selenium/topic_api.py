#!/usr/bin/env python3

from .driver_initialization import Initializer
from .element_finder import Finder
import logging
from .scraping_utilities import Scraping_utilities
import json
from typing import Union
import os

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Topic_api:
    def __init__(self, URL, browser, proxy, headless, tweets_count):
        self.URL = URL
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

    def generate_graphql_link(self, key):
        return 'https://twitter.com/i/api/graphql/{}/TopicLandingPage'.format(key)

    def find_rest_id(self):
        return self.URL.split('topics/')[-1]

    def augment_data(self, data):
        try:
            for tweet in data:
                try:
                    typename = tweet['content']['itemContent']['tweet_results']['result']['__typename']
                except KeyError:
                    continue
                if typename.lower() == 'tweet':
                    result = tweet['content']['itemContent']['tweet_results']['result']
                    key = result['rest_id']
                    user = result['core']['user_results']['result']['legacy']
                    tweet_data = result['legacy']
                    self.data_dict[key] = {
                        'tweet_url': "https://twitter.com/{}/status/{}".format(user['screen_name'], key),
                        'tweet_detail': tweet_data,
                        'user_details': user
                    }
        except Exception as ex:
            logger.exception('Error at augment_data : {}'.format(ex))

    def find_entries(self, instructions):
        entries = []
        for item in instructions:
            if item['type'] == 'TimelineAddEntries':
                entries = item['entries']
                break
        return entries

    def find_cursor(self, entries):
        try:
            cursor = None
            for entry in entries:
                if entry['content']['entryType'] == 'TimelineTimelineCursor':
                    if entry['content']['cursorType'] == 'Bottom':
                        cursor = entry['content']['value']
                        break
            return cursor
        except Exception as ex:
            logger.exception('Error at find_cursor : {}'.format(ex))

    def scrape(self):
        try:
            BEARER_TOKEN = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
            self.start_driver()
            key = Finder.find_graphql_key(self.driver, self.URL)
            self.close_driver()
            graphql_link = self.generate_graphql_link(key)
            cursor = None
            rest_id = self.find_rest_id()
            guest_token = Scraping_utilities.find_x_guest_token(
                BEARER_TOKEN, self.proxy)
            while len(self.data_dict) < self.tweets_count:
                params = Scraping_utilities.build_topic_params(rest_id, cursor)
                headers = Scraping_utilities.build_topic_headers(
                    guest_token, BEARER_TOKEN, rest_id)
                response = Scraping_utilities.make_http_request_with_params(graphql_link,
                                                                            params, headers, self.proxy)
                if response:
                    instructions = response['data']['topic_by_rest_id']['topic_page']['body']['timeline']['instructions']
                    entries = self.find_entries(instructions)
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


def scrape_topic_with_api(URL: str, proxy: Union[str, None] = None,
                          tweets_count: int = 10,
                          output_filename: Union[str, None] = None,
                          output_dir: Union[str, None] = os.getcwd(),
                          browser: str = 'firefox',
                          headless: bool = True):
    """Function to scrape twitter Topic from URL using Twitter's API.

    Args:
        URL (str): URL of the topic.
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        tweets_count (int, optional): Number of Tweets to scrape. Defaults to 10.
        output_filename (Union[str, None], optional): Name of the output JSON file. Defaults to None.
        output_dir (Union[str, None], optional): Directory where to save the file. Defaults to os.getcwd().
        browser (str, optional): Which browser to use for extracting out graphql key. Defaults to 'firefox'.
        headless (bool, optional): Whether to run browser in headless mode?. Defaults to True.
    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    topic_api_scraper = Topic_api(
        URL=URL, browser=browser, tweets_count=tweets_count, proxy=proxy, headless=headless)
    data = topic_api_scraper.scrape()
    if output_filename and len(data) > 0:
        path = os.path.join(output_dir, "{}.json".format(output_filename))
        mode = 'a'
        if os.path.exists(path):
            mode = 'r'
        with open(path, mode, encoding='utf-8') as file:
            if mode == 'r':
                try:
                    file_content = file.read()
                    content = json.loads(file_content)
                except json.decoder.JSONDecodeError:
                    logger.warning('Invalid JSON Detected!')
                    content = {}
                file.close()
                data.update(content)
        with open(path, 'w', encoding='utf-8') as file_in_write_mode:
            json.dump(data, file_in_write_mode)
            logger.setLevel(logging.INFO)
            logger.info('Data was saved to {}'.format(path))
    else:
        return data
