#!/usr/bin/env python3

from typing import Union
from .scraping_utilities import Scraping_utilities
import logging
from urllib.parse import quote
import os
import json

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Keywords_api:
    def __init__(self, query: str, proxy: Union[str, None],
                 tweets_count: int) -> None:
        self.query = query
        self.proxy = proxy
        self.tweets_count = tweets_count
        self.x_guest_key = ''
        self.authorization_key = \
            'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
        self.posts_data = {}

    def parse_tweets(self, tweets, users):
        for key in tweets.keys():
            user = users[tweets[key]['user_id_str']]
            tweet = tweets[key]
            self.posts_data[key] = {
                "tweet_url": "https://twitter.com/{}/status/{}".format(user['screen_name'], key),
                "tweet_details": tweet,
                "user_details": user
            }

    def find_cursor(self, timeline):
        cursor = None
        try:
            cursor = timeline["instructions"][-1]["replaceEntry"]["entry"]["content"]["operation"]["cursor"]["value"]
        except KeyError:
            cursor = timeline["instructions"][0]["addEntries"]["entries"][-1]["content"]["operation"]["cursor"]["value"]
        return cursor

    def scrap(self):
        try:
            self.x_guest_key \
                = Scraping_utilities.find_x_guest_token(self.authorization_key)
            logger.setLevel(logging.INFO)
            headers = Scraping_utilities.build_keyword_headers(
                self.x_guest_key, self.authorization_key, quote(self.query))
            cursor = None
            retry = 5
            while len(self.posts_data) < self.tweets_count:
                params = Scraping_utilities.build_params(self.query, cursor)
                response = Scraping_utilities.make_http_request_with_params(
                    'https://twitter.com/i/api/2/search/adaptive.json', params,
                    headers, self.proxy)
                if response:
                    tweets = response['globalObjects']['tweets']
                    users = response['globalObjects']['users']
                    timeline = response['timeline']
                    self.parse_tweets(tweets, users)
                    cursor = self.find_cursor(timeline)
                    if cursor is None:
                        retry -= 1
                    logger.info('Number of Tweets scraped : {}'.format(
                        len(self.posts_data)))
                elif retry <= 0:
                    logger.info("Can't Find more Post")
                    break
                else:
                    logger.warning('Failed to make request!')
                    break
            data = dict(list(self.posts_data.items())
                        [0:int(self.tweets_count)])
            return data
        except Exception as ex:
            logger.warning('Error at scrap : {}'.format(ex))


def scrape_keyword_with_api(query: str, proxy: Union[str, None] = None,
                            tweets_count: int = 10,
                            output_filename: Union[str, None] = None,
                            output_dir: Union[str, None] = os.getcwd()):
    """Function to scrape tweets from Twitter API using provided query.

    Args:
        query (str): query to search.
        proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
        tweets_count (int, optional): Number of Tweets to scrape. Defaults to 10.
        output_filename (Union[str, None], optional): Name of the output JSON file. Defaults to None.
        output_dir (Union[str, None], optional): Directory where to save the file. Defaults to os.getcwd().

    Returns:
        (dict | none): None if data was saved, else JSON String.
    """
    keyword_scraper = Keywords_api(query, proxy, tweets_count)
    data = keyword_scraper.scrap()
    if output_filename:
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
                    logger.info('Data was saved to {}'.format(path))
    else:
        return data
