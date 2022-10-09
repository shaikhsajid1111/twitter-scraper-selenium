#!/usr/bin/env python3


import logging
from typing import Union
from fake_headers import Headers
# to add capabilities for chrome and firefox, import their Options with different aliases
from selenium.webdriver.chrome.options import Options as CustomChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as CustomFireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from seleniumwire import webdriver
# import webdriver for downloading respective driver for the browser
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Initializer:
    def __init__(self, browser_name: str, headless: bool, proxy: Union[str, None] = None, profile: Union[str, None] = None):
        """Initialize Browser

        Args:
            browser_name (str): Browser Name
            headless (bool): Whether to run Browser in headless mode?
            proxy (Union[str, None], optional): Optional parameter, if user wants to use proxy for scraping. If the proxy is authenticated proxy then the proxy format is username:password@host:port. Defaults to None.
            profile (Union[str, None], optional): Path of Browser Profile where cookies might be located to scrap data in authenticated way. Defaults to None.
      """
        self.browser_name = browser_name
        self.proxy = proxy
        self.headless = headless
        self.profile = profile

    def set_properties(self, browser_option):
        """adds capabilities to the driver"""
        header = Headers().generate()['User-Agent']
        if self.headless:
            # runs browser in headless mode
            browser_option.add_argument("--headless")
        if self.profile and self.browser_name.lower() == "chrome":
            browser_option.add_argument(
                "user-data-dir={}".format(self.profile))
        if self.profile and self.browser_name.lower() == "firefox":
            logger.setLevel(logging.INFO)
            logger.info("Loading Profile from {}".format(self.profile))
            browser_option.add_argument("-profile")
            browser_option.add_argument(self.profile)
        browser_option.add_argument('--no-sandbox')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        browser_option.add_argument('--user-agent={}'.format(header))
        return browser_option

    def set_driver_for_browser(self, browser_name: str):
        """expects browser name and returns a driver instance"""
        # if browser is suppose to be chrome
        if browser_name.lower() == "chrome":
            browser_option = CustomChromeOptions()
            # automatically installs chromedriver and initialize it and returns the instance
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logger.setLevel(logging.INFO)
                logger.info("Using Proxy: {}".format(self.proxy))

                return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                        options=self.set_properties(browser_option), seleniumwire_options=options)

            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.set_properties(browser_option))
        elif browser_name.lower() == "firefox":
            browser_option = CustomFireFoxOptions()
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                logger.setLevel(logging.INFO)
                logger.info("Using Proxy: {}".format(self.proxy))
                return webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()),
                                         options=self.set_properties(browser_option), seleniumwire_options=options)

            # automatically installs geckodriver and initialize it and returns the instance
            return webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), options=self.set_properties(browser_option))
        else:
            # if browser_name is not chrome neither firefox than raise an exception
            raise Exception("Browser not supported!")

    def init(self):
        """returns driver instance"""
        driver = self.set_driver_for_browser(self.browser_name)
        return driver
