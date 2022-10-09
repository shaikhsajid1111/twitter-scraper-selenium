#!/usr/bin/env python3
import re
from typing import Union
from urllib.parse import quote
import logging

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Scraping_utilities:
    """
    This class contains all utility methods that help cleaning or extracting
    data from raw data.

    @staticmethod
    def method_name(parameters)
    """

    @staticmethod
    def parse_name(string) -> Union[str, None]:
        """Extract name from the given string.
           Example:
           Input: jack(@jack)
           Output: jack
        """
        try:
            return string.split("(")[0].strip()
        except Exception as ex:
            logger.exception("Error at parse_name : {}".format(ex))

    @staticmethod
    def extract_digits(string) -> Union[int, None]:
        """Extracts first digits from the string.

        Args:
          string (str): string containing digits.

        Returns:
          int: digit that was extracted from the passed string
        """
        try:
            return int(re.search(r'\d+', string).group(0))
        except Exception as ex:
            logger.exception("Error at extract_digits : {}".format(ex))

    @staticmethod
    def set_value_or_none(value, string) -> Union[str, None]:
        return string+str(value)+" " if value is not None else None

    @staticmethod
    def url_generator(keyword: str, since: Union[int, None] = None, until: Union[str, None] = None,
                      since_id: Union[int, None] = None, max_id: Union[int, None] = None,
                      within_time: Union[str, None] = None) -> str:
        """Generates Twitter URL for passed keyword

        Args:
            keyword (str): Keyword to search on twitter.
            since (Union[int, None], optional): Optional parameter,Since date for scraping,a past date from where to search from. Format for date is YYYY-MM-DD or unix timestamp in seconds. Defaults to None.
            until (Union[str, None], optional): Optional parameter,Until date for scraping,a end date from where search ends. Format for date is YYYY-MM-DD or unix timestamp in seconds. Defaults to None.
            since_id (Union[int, None], optional): After (NOT inclusive) a specified Snowflake ID. Defaults to None.
            max_id (Union[int, None], optional): At or before (inclusive) a specified Snowflake ID. Defaults to None.
            within_time (Union[str, None], optional): Search within the last number of days, hours, minutes, or seconds. Defaults to None.

        Returns:
            str: Twitter URL
        """
        base_url = "https://twitter.com/search?q="
        if within_time is None:
            words = [Scraping_utilities.set_value_or_none(since, "since:"),
                     Scraping_utilities.set_value_or_none(
                until, "until:"),
                Scraping_utilities.set_value_or_none(
                since_id, "since_id:"), Scraping_utilities.set_value_or_none(max_id, "max_id:")]
            query = ""
            for word in words:
                if word is not None:
                    query += word
            query += keyword
            query = quote(query)
            base_url = base_url + query + "&src=typed_query&f=live"
        else:
            word = Scraping_utilities.set_value_or_none(
                within_time, "within_time:")
            query = keyword + " " + word
            base_url = base_url + quote(query) + "&src=typed_query&f=live"
        return base_url
