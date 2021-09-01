#!/usr/bin/env python3
try:
    from seleniumwire import webdriver
    # to add capabilities for chrome and firefox, import their Options with different aliases
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    # import webdriver for downloading respective driver for the browser
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
except Exception as ex:
    print(ex)


class Initializer:

    def __init__(self, browser_name, proxy=None):
        self.browser_name = browser_name
        self.proxy = proxy

    def set_properties(self, browser_option):
        """adds capabilities to the driver"""
        browser_option.add_argument(
            '--headless')  # runs browser in headless mode
        browser_option.add_argument('--no-sandbox')
        browser_option.add_argument("--disable-dev-shm-usage")
        browser_option.add_argument('--ignore-certificate-errors')
        browser_option.add_argument('--disable-gpu')
        browser_option.add_argument('--log-level=3')
        browser_option.add_argument('--disable-notifications')
        browser_option.add_argument('--disable-popup-blocking')
        return browser_option

    def set_driver_for_browser(self, browser_name):
        """expects browser name and returns a driver instance"""
        # if browser is suppose to be chrome
        if browser_name.lower() == "chrome":
            browser_option = ChromeOptions()
            # automatically installs chromedriver and initialize it and returns the instance
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                print("Using: {}".format(self.proxy))
                return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                        options=self.set_properties(browser_option), seleniumwire_options=options)

            return webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.set_properties(browser_option))
        elif browser_name.lower() == "firefox":
            browser_option = FirefoxOptions()
            if self.proxy is not None:
                options = {
                    'https': 'https://{}'.format(self.proxy.replace(" ", "")),
                    'http': 'http://{}'.format(self.proxy.replace(" ", "")),
                    'no_proxy': 'localhost, 127.0.0.1'
                }
                print("Using: {}".format(self.proxy))
                return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                         options=self.set_properties(browser_option), seleniumwire_options=options)

            # automatically installs geckodriver and initialize it and returns the instance
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=self.set_properties(browser_option))
        else:
            # if browser_name is not chrome neither firefox than raise an exception
            raise Exception("Browser not supported!")

    def init(self):
        """returns driver instance"""
        driver = self.set_driver_for_browser(self.browser_name)
        return driver
