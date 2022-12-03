#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import logging
import os
import json
from .keyword import Keyword, json_to_csv

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


def scrape_topic(
    url: str,
    browser: str = "firefox",
    filename: str = "",
    proxy: str = None,
    tweets_count: int = 10,
    output_format: str = "json",
    directory: str = None,
    headless: bool = True,
    browser_profile=None
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
        directory = os.getcwd()
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
            mode = 'w'
            output_path = os.path.join(directory, filename+".json")
            if os.path.exists(output_path):
                mode = 'r'
            with open(output_path, mode, encoding='utf-8') as file:
                if mode == 'r':
                    try:
                        file_content = file.read()
                        content = json.loads(file_content)
                    except json.decoder.JSONDecodeError:
                        logger.warning('Invalid JSON Detected!')
                        content = {}
                    file.close()
                    data.update(content)
                    with open(output_path, 'w', encoding='utf-8') as file_in_write_mode:
                        json.dump(data, file_in_write_mode)
                        logger.setLevel(logging.INFO)
                        logger.info('Data Successfully Saved to {}'.format(
                            output_path))
    elif output_format == "csv":
        json_to_csv(filename=filename, json_data=data, directory=directory)
    else:
        raise ValueError("Invalid Output Format")
