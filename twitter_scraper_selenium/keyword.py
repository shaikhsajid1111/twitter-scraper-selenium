try:
  from datetime import datetime,timedelta
  from .driver_initialization import Initializer
  from .driver_utils import Utilities
except Exception as ex:
  print(ex)

class Keyword:
  """this class needs to be instantiated in order to find something
  on twitter related to keywords"""

  def __init__(self, keyword, until=datetime.today().strftime('%Y-%m-%d'),
  since=(datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")) -> None:
      self.keyword = keyword
      self.URL = "https://twitter.com/search?q=%23{}%20until%3A{}%20since%3A{}&src=typed_query&f=live".format(
          keyword, until, since)
      self.driver = ""

  def __start_driver(self):
    """changes the class member __driver value to driver on call"""
    self.__driver = Initializer(self.browser, self.proxy).init()

  def scrap(self):
    self.__start_driver()
    self.__driver.get(self.URL)
    Utilities._Utilities__wait_until_tweets_appear(self.__driver)




