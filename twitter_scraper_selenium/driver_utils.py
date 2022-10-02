#!/usr/bin/env python3
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.common.keys import Keys
from random import randint
import logging

logging.getLogger().setLevel(logging.INFO)


class Utilities:
    """this class contains all the method related to driver behaviour,
    like scrolling, waiting for element to appear, it contains all static
    method, which accepts driver instance as a argument"""

    @staticmethod
    def __wait_until_tweets_appear(driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid="tweet"]')))
        except WebDriverException:
            logging.exception(
                "Tweets did not appear!, Try setting headless=False to see what is happening")

    @staticmethod
    def __scroll_down(driver):
        try:
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            for _ in range(randint(1, 3)):
                body.send_keys(Keys.PAGE_DOWN)
        except Exception as ex:
            logging.exception("Error at scroll_down method {}".format(ex))

    @staticmethod
    def __wait_until_completion(driver):
        """waits until the page have completed loading"""
        try:
            state = ""
            while state != "complete":
                time.sleep(randint(3, 5))
                state = driver.execute_script("return document.readyState")
        except Exception as ex:
            logging.exception('Error at Wait Until Completion: {}'.format(ex))
