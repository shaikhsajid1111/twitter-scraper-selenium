#!/usr/bin/env python3

from typing import Union
from .scraping_utilities import Scraping_utilities
import os
import logging
import json

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Profile_detail:
    def __init__(self, username: str, proxy: Union[str, None]) -> None:
        self.username = username
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.proxy = proxy

    def scrape(self):
        guest_token = Scraping_utilities.find_x_guest_token(
            authorization_key=self.authorization_key, proxy=self.proxy)
        headers = Scraping_utilities.build_keyword_headers(
            authorization_key=self.authorization_key, x_guest_token=guest_token)
        response = Scraping_utilities.make_http_request(
            "https://api.twitter.com/1.1/users/show.json?screen_name={}".format(
                self.username),
            headers=headers, proxy=self.proxy)
        if response:
            return response
        else:
            logger.debug('Failed to Make Request!')


def get_profile_details(twitter_username: str, proxy: Union[str, None] = None,
                       filename: str = "", directory: str = os.getcwd()):
    """Extract Profile Detail.

    Args:
        twitter_username (str): Twitter username
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        filename (str, optional): Filename where to save the output. Defaults to "".
        directory (str, optional): Directory where to save the file. Defaults to os.getcwd().

    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    profile_bot = Profile_detail(username=twitter_username, proxy=proxy)
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