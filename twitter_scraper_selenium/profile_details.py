#!/usr/bin/env python3

from typing import Union
from .scraping_utilities import Scraping_utilities
import os
import logging
import json
from .profile_api import Profile_api

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Profile_detail:
    def __init__(self, username: str, proxy: Union[str, None], browser: str, headless: bool) -> None:
        self.username = username
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.proxy = proxy
        self.browser = browser
        self.headless = headless

    def scrape(self):
        profile_api = Profile_api(self.username, proxy=self.proxy,
          browser = self.browser, tweets_count=1, headless=self.headless)
        header, uid, user_id = profile_api.get_headers_and_uid(
                f"https://twitter.com/{self.username}")
        params = Scraping_utilities.build_params_for_profile(
                    user_id, None)
        response = Scraping_utilities.make_http_request_with_params(
                    f"https://twitter.com/i/api/graphql/{uid}/UserTweets", params, header, self.proxy)
        if response:
            entries = profile_api.find_entries(response)
            if len(entries) > 0:
                return entries[0]["content"]["itemContent"]["tweet_results"]["result"]["core"]["user_results"]["result"]
            return {}
        else:
            logger.debug('Failed to Make Request!')


def get_profile_details(twitter_username: str, proxy: Union[str, None] = None,
                       filename: str = "", directory: str = os.getcwd(), browser: str="firefox", headless: bool = True):
    """Extract Profile Detail.

    Args:
        twitter_username (str): Twitter username
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        filename (str, optional): Filename where to save the output. Defaults to "".
        directory (str, optional): Directory where to save the file. Defaults to os.getcwd().
        browser (str, optional): Which browser to use for extracting out graphql key. Defaults to 'firefox'.
        headless (bool, optional): Whether to run browser in headless mode?. Defaults to True.
    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    profile_bot = Profile_detail(username=twitter_username, proxy=proxy, browser=browser, headless=headless)
    data = profile_bot.scrape()

    if filename == '':
        # if filename was not provided then print the JSON to console
        return json.dumps(data)
    elif filename != '' and len(data) > 0:
        # if filename was provided, save it to that file
        mode = 'w'
        json_file_location = os.path.join(directory, filename+".json")
        if os.path.exists(json_file_location):
            mode = 'r'
        with open(json_file_location, mode, encoding='utf-8') as file:
            if mode == 'r':
                try:
                    file_content = file.read()
                    content = json.loads(file_content)
                except json.decoder.JSONDecodeError:
                    logger.warning('Invalid JSON Detected!')
                    content = {}
                file.close()
                data.update(content)
        with open(json_file_location, 'w', encoding='utf-8') as file_in_write_mode:
            json.dump(data, file_in_write_mode)
            logger.setLevel(logging.INFO)
            logger.info(
                'Data Successfully Saved to {}'.format(json_file_location))
    else:
      return json.dumps(data)