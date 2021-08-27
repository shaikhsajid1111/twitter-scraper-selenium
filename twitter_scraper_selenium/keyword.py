#!/usr/bin/env python3
try:
  from datetime import datetime,timedelta
  from .driver_initialization import Initializer
  from .driver_utils import Utilities
  from inspect import currentframe
  from .element_finder import Finder
  import re,json
  from urllib.parse import quote
except Exception as ex:
  print(ex)

frameinfo = currentframe()

class Keyword:
  """this class needs to be instantiated in order to find something
  on twitter related to keywords"""

  def __init__(self, keyword,browser,until=datetime.today().strftime('%Y-%m-%d'),
               since=(datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d"), proxy=None, posts_count=10) -> None:
      self.keyword = keyword
      self.URL = "https://twitter.com/search?q={}%20until%3A{}%20since%3A{}&src=typed_query&f=live".format(
          quote(keyword), until, since)
      self.driver = ""
      self.browser= browser
      self.proxy = proxy
      self.posts_count = posts_count
      self.posts_data = {}
      self.retry = 10
  def __start_driver(self):
    """changes the class member __driver value to driver on call"""
    self.__driver = Initializer(self.browser, self.proxy).init()

  def __close_driver(self):
    self.__driver.close()
    self.__driver.quit()

  def __check_tweets_presence(self, tweet_list):
    if len(tweet_list) <= 0:
      self.retry -= 1

  def __check_retry(self):
    return self.retry <= 0

  def __fetch_and_store_data(self):
    try:
      all_ready_fetched_posts = []
      present_tweets = Finder._Finder__fetch_all_tweets(self.__driver)
      self.__check_tweets_presence(present_tweets)
      all_ready_fetched_posts.extend(present_tweets)

      while len(self.posts_data) < self.posts_count:
        for tweet in present_tweets:
          name = Finder._Finder__find_name_from_post(tweet)
          status = Finder._Finder__find_status(tweet)
          replies = Finder._Finder__find_replies(tweet)
          retweets = Finder._Finder__find_shares(tweet)
          username = status[3]
          status = status[-1]
          is_retweet = Finder._Finder__is_retweet(tweet)
          posted_time = Finder._Finder__find_timestamp(tweet)
          content = Finder._Finder__find_content(tweet)
          likes = Finder._Finder__find_like(tweet)
          images = Finder._Finder__find_images(tweet)
          videos = Finder._Finder__find_videos(tweet)
          hashtags = re.findall(r"#(\w+)", content)
          mentions = re.findall(r"@(\w+)", content)
          profile_picture = "https://twitter.com/{}/photo".format(username)
          post_url = "https://twitter.com/{}/status/{}".format(username,status)
          self.posts_data[status] = {
            "post_id" : status,
            "username" : username,
            "name" : name,
            "profile_picture" : profile_picture,
            "replies" : replies,
            "retweets" : retweets,
            "likes":likes,
           "is_retweet" : is_retweet,
            "posted_time" : posted_time,
            "content" : content,
            "hashtags" : hashtags,
            "mentions" : mentions,
            "images" : images,
            "videos" : videos,
            "post_url" : post_url
          }

        Utilities._Utilities__scroll_down(self.__driver)
        Utilities._Utilities__wait_until_completion(self.__driver)
        Utilities._Utilities__wait_until_tweets_appear(self.__driver)
        present_tweets = Finder._Finder__fetch_all_tweets(self.__driver)
        present_tweets = [post for post in present_tweets if post not in all_ready_fetched_posts]
        self.__check_tweets_presence(present_tweets)
        all_ready_fetched_posts.extend(present_tweets)
        if self.__check_retry() is True:
          break

    except Exception as ex:
      print("Error at method scrap on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  def scrap(self):
    try:
      self.__start_driver()
      self.__driver.get(self.URL)
      Utilities._Utilities__wait_until_completion(self.__driver)
      Utilities._Utilities__wait_until_tweets_appear(self.__driver)
      self.__fetch_and_store_data()

      self.__close_driver()
      data = dict(list(self.posts_data.items())[0:int(self.posts_count)])
      return json.dumps(data)

    except Exception as ex:
      self.__close_driver()
      print("Error at method scrap on line no. {} : {}".format(frameinfo.f_lineno,ex))


