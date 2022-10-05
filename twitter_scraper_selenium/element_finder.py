#!/usr/bin/env python3

from selenium.common.exceptions import NoSuchElementException
from .scraping_utilities import Scraping_utilities
from dateutil.parser import parse
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)

class Finder:
    """
    this class should contain all  the static method to find that accept
    webdriver instance and perform operation to find elements and return the
    found element.
    method should follow convention like so:

    @staticmethod
    def __method_name(parameters):
    """

    @staticmethod
    def __fetch_all_tweets(driver):
        try:
            return driver.find_elements(By.CSS_SELECTOR, '[data-testid="tweet"]')
        except Exception as ex:
            logger.exception("Error at method fetch_all_tweets : {}".format(ex))
            return []

    @staticmethod
    def __find_replies(tweet):
        try:
            replies_element = tweet.find_element(
                By.CSS_SELECTOR, '[data-testid="reply"]')
            replies = replies_element.get_attribute("aria-label")
            return Scraping_utilities._Scraping_utilities__extract_digits(replies)
        except Exception as ex:
            logger.exception("Error at method find_replies : {}".format(ex))
            return ""

    @staticmethod
    def __find_shares(tweet):
        try:
            shares_element = tweet.find_element(
                By.CSS_SELECTOR, '[data-testid="retweet"]')
            shares = shares_element.get_attribute("aria-label")
            return Scraping_utilities._Scraping_utilities__extract_digits(shares)
        except Exception as ex:
            logger.exception("Error at method find_shares : {}".format(ex))
            return ""

    @staticmethod
    def __find_status(tweet):
        try:
            anchor = tweet.find_element(
                By.CSS_SELECTOR, "a.r-bcqeeo.r-3s2u2q.r-qvutc0")
            return (anchor.get_attribute("href").split("/"), anchor.get_attribute("href"))
        except Exception as ex:
            logger.exception("Error at method find_status : {}".format(ex))
            return []

    @staticmethod
    def __find_all_anchor_tags(tweet):
        try:
            return tweet.find_elements(By.TAG_NAME, 'a')
        except Exception as ex:
            logger.exception("Error at method find_all_anchor_tags : {}".format(ex))

    @staticmethod
    def __find_timestamp(tweet):
        try:
            timestamp = tweet.find_element(By.TAG_NAME,
                                           "time").get_attribute("datetime")
            posted_time = parse(timestamp).isoformat()
            return posted_time
        except Exception as ex:
            logger.exception("Error at method find_timestamp : {}".format(ex))

    @staticmethod
    def __find_content(tweet):
        try:
            #content_element = tweet.find_element('.//*[@dir="auto"]')[4]
            content_element = tweet.find_element(By.CSS_SELECTOR, 'div[lang]')
            return content_element.text
        except NoSuchElementException:
            return ""
        except Exception as ex:
            logger.exception("Error at method find_content : {}".format(ex))

    @staticmethod
    def __find_like(tweet):
        try:
            like_element = tweet.find_element(
                By.CSS_SELECTOR, '[data-testid="like"]')
            likes = like_element.get_attribute("aria-label")
            return Scraping_utilities._Scraping_utilities__extract_digits(likes)
        except Exception as ex:
            logger.exception("Error at method find_like : {}".format(ex))

    @staticmethod
    def __find_images(tweet):
        try:
            image_element = tweet.find_elements(By.CSS_SELECTOR,
                                                'div[data-testid="tweetPhoto"]')
            images = []
            for image_div in image_element:
                href = image_div.find_element(By.TAG_NAME,
                                              "img").get_attribute("src")
                images.append(href)
            return images
        except Exception as ex:
            logger.exception("Error at method find_images : {}".format(ex))

    @staticmethod
    def __find_videos(tweet):
        try:
            image_element = tweet.find_elements(By.CSS_SELECTOR,
                                                'div[data-testid="videoPlayer"]')
            videos = []
            for video_div in image_element:
                href = video_div.find_element(
                    By.TAG_NAME, "video").get_attribute("src")
                videos.append(href)
            return videos
        except Exception as ex:
            logger.exception("Error at method find_videos : {}".format(ex))

    @staticmethod
    def __is_retweet(tweet):
        try:
            tweet.find_element(By.CSS_SELECTOR, 'div.r-92ng3h.r-qvutc0')
            return True
        except NoSuchElementException:
            return False
        except Exception as ex:
            logger.exception("Error at method is_retweet : {}".format(ex))
            return False

    @staticmethod
    def __find_name_from_post(tweet, is_retweet=False):
        try:
            name = "NA"
            anchors = Finder.__find_all_anchor_tags(tweet)
            if len(anchors) > 2:
                if is_retweet:
                    name = anchors[2].text.strip()
                else:
                    name = anchors[1].text.split("\n")[0]
            return name
        except Exception as ex:
            logger.exception("Error at method find_name_from_post : {}".format(ex))

    @staticmethod
    def __find_external_link(tweet):
        try:
            card = tweet.find_element(
                By.CSS_SELECTOR, '[data-testid="card.wrapper"]')
            href = card.find_element(By.TAG_NAME, 'a')
            return href.get_attribute("href")

        except NoSuchElementException:
            return ""
        except Exception as ex:
            logger.exception("Error at method find_external_link : {}".format(ex))
