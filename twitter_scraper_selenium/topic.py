#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import logging
import pathlib
import json
from .keyword import Keyword


def scrap_topic(
    filename: str,
    url: str,
    browser: str = "firefox",
    proxy: str = None,
    tweets_count: int = 10,
    output_format: str = "json",
    directory: str = None,
    headless: bool = True,
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
    )
    data = keyword_bot.scrap()
    if output_format == "json":
        output_path = directory / "{}.json".format(filename)
        if output_path.exists():
            try:
                with output_path.open() as f:
                    existing_data = json.load(f)
                data = json.dumps(existing_data.update(json.loads(data)))
            except Exception as err:
                logging.Exception("load existing data failed")
        output_path.write_text(data)
    elif output_format == "csv":
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
                with output_path.open() as f:
                    reader = csv.DictReader(f, fieldnames=fieldnames)
                    for row in reader:
                        old_data.append(row)
            except Exception as err:
                logging.Exception("Load Existing Data Failed")
        with output_path.open("w") as f:
            writer = csv.DictWriter(f, filenames=fieldnames)
            writer.writeheader()
            writer.writerows(old_data + list(json.loads(data).values()))
    else:
        raise ValueError("Invalid Output Format")
