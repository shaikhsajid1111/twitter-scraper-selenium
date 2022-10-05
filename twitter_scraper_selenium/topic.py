#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import logging
import pathlib
import json
from .keyword import Keyword

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


def scrap_topic(
    url: str,
    browser: str = "firefox",
    filename: str = "",
    proxy: str = None,
    tweets_count: int = 10,
    output_format: str = "json",
    directory: str = None,
    headless: bool = True,
    browser_profile = None
):
    """
    Returns tweets data in CSV or JSON.

    Args:
        filename: Filename to write result output.
        url: Topic url.
        browser: Which browser to use for scraping?, Only 2 are supported Chrome and Firefox
        proxy: If user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port
        tweets_count: Number of posts to scrap. Default is 10.
        output_format: The output format, whether JSON or CSV. Default is JSON.
        directory: If output parameter is set to CSV, then it is valid for directory parameter to be passed. If not passed then CSV file will be saved in current working directory.
        browser_profile: Path of Browser Profile where cookies might be located to scrap data in authenticated way.
    """
    pass
    if directory is None:
        directory = pathlib.Path.cwd()
    keyword_bot = Keyword(
        keyword=filename,
        browser=browser,
        url=url,
        headless=headless,
        proxy=proxy,
        tweets_count=tweets_count,
        browser_profile=browser_profile
    )
    data = keyword_bot.scrap()
    if output_format.lower() == "json":
        if filename == '':
            # if filename was not provided
            return json.dumps(data)
        elif filename != '':
            # if filename was provided
            output_path = directory / "{}.json".format(filename)
            if output_path.exists():
                try:
                    with output_path.open(encoding="utf-8") as f:
                        existing_data = json.load(f)
                    data.update(existing_data)
                except Exception as err:
                    logger.exception("Error Appending Data: {}".format(err))
            output_path.write_text(json.dumps(data))
            logger.info(
                'Data Successfully Saved to {}'.format(output_path))
    elif output_format == "csv":
        if filename == '':
            raise Exception('Filename is required to save the CSV file.')
        fieldnames = [
            "tweet_id",
            "username",
            "name",
            "profile_picture",
            "replies",
            "retweets",
            "likes",
            "is_retweet",
            "posted_time",
            "content",
            "hashtags",
            "mentions",
            "images",
            "videos",
            "tweet_url",
            "link",
        ]
        output_path = directory / "{}.csv".format(filename)
        old_data = []
        if output_path.exists():
            try:
                with output_path.open(encoding="utf-8") as f:
                    reader = csv.DictReader(f, fieldnames=fieldnames)
                    for row in reader:
                        old_data.append(row)
            except Exception as err:
                logger.exception("Error Appending Data: {}".format(err))
        with output_path.open("w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(old_data + list(json.loads(data).values()))
            logger.setLevel(logging.INFO)
            logger.info('Data Successfully Saved to {}'.format(output_path))
    else:
        raise ValueError("Invalid Output Format")
