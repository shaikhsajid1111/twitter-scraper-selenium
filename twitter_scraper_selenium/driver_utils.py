#!/usr/bin/env python3
try:
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import WebDriverException
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    from inspect import currentframe
    from random import randint
except Exception as ex:
    frameinfo = currentframe()
    print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))

frameinfo = currentframe()


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
            print(
                "Tweets did not appear!, Try setting headless=False to see what is happening")

    @staticmethod
    def __scroll_down(driver):
        try:
            body = driver.find_element(By.CSS_SELECTOR, 'body')
            for _ in range(3):
                body.send_keys(Keys.PAGE_DOWN)
        except Exception as ex:
            print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))

    @staticmethod
    def __wait_until_completion(driver):
        """waits until the page have completed loading"""
        try:
            state = ""
            while state != "complete":
                time.sleep(randint(3, 5))
                state = driver.execute_script("return document.readyState")
        except Exception as ex:
            print(ex)
