#!/usr/bin/env python3
try:
    from selenium.common.exceptions import NoSuchElementException
    from .scraping_utilities import Scraping_utilities
    from inspect import currentframe
    from dateutil.parser import parse
except Exception as ex:
    frameinfo = currentframe()
    print("Error on line no. {} : {}".format(frameinfo.f_lineno,ex))

frameinfo = currentframe()

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
      return driver.find_elements_by_css_selector('div[data-testid="tweet"]')
    except:
      print("Error at method fetch_all_tweets on line no. {} : {}".format(frameinfo.f_lineno, ex))

  @staticmethod
  def __find_replies(tweet):
    try:
      replies_element = tweet.find_element_by_css_selector('div[data-testid="reply"]')
      replies = replies_element.get_attribute("aria-label")
      return Scraping_utilities._Scraping_utilities__extract_digits(replies)
    except Exception as ex:
      print("Error at method find_replies on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return ""

  @staticmethod
  def __find_shares(tweet):
    try:
      shares_element = tweet.find_element_by_css_selector('div[data-testid="retweet"]')
      shares =  shares_element.get_attribute("aria-label")
      return Scraping_utilities._Scraping_utilities__extract_digits(shares)
    except Exception as ex:
      print("Error at method find_shares on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return ""

  @staticmethod
  def __find_status(tweet):
    try:
      anchors = Finder.__find_all_anchor_tags(tweet)
      status = "NA"
      if len(anchors) > 2:
        status = anchors[2].get_attribute("href").split("/")
      return status
    except Exception as ex:
      print("Error at method find_status on line no. {} : {}".format(frameinfo.f_lineno, ex))
      return []

  @staticmethod
  def __find_all_anchor_tags(tweet):
    try:
      return tweet.find_elements_by_tag_name('a')
    except Exception as ex:
      print("Error at method find_all_anchor_tags on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_timestamp(tweet):
    try:
      timestamp = tweet.find_element_by_tag_name(
          "time").get_attribute("datetime")
      posted_time = parse(timestamp).isoformat()
      return posted_time
    except Exception as ex:
      print("Error at method find_timestamp on line no. {} : {}".format(
          frameinfo.f_lineno, ex))


  @staticmethod
  def __find_content(tweet):
    try:
      #content_element = tweet.find_element_by_css_selector('.//*[@dir="auto"]')[4]
      content_element = tweet.find_element_by_css_selector('div[lang]')
      return content_element.text
    except NoSuchElementException:
      return ""
    except Exception as ex:
      print("Error at method find_content on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_like(tweet):
    try:
      like_element = tweet.find_element_by_css_selector('div[data-testid="like"]')
      likes = like_element.get_attribute("aria-label")
      return Scraping_utilities._Scraping_utilities__extract_digits(likes)
    except Exception as ex:
      print("Error at method find_like on line no. {} : {}".format(
          frameinfo.f_lineno, ex))
  @staticmethod
  def __find_images(tweet):
    try:
      image_element = tweet.find_elements_by_css_selector(
          'div[data-testid="tweetPhoto"]')
      images = []
      for image_div in image_element:
        href = image_div.find_element_by_tag_name("img").get_attribute("src")
        images.append(href)
      return images
    except Exception as ex:
      print("Error at method __find_images on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_videos(tweet):
    try:
      image_element = tweet.find_elements_by_css_selector(
          'div[data-testid="videoPlayer"]')
      videos = []
      for video_div in image_element:
        href = video_div.find_element_by_tag_name("video").get_attribute("src")
        videos.append(href)
      return videos
    except Exception as ex:
      print("Error at method find_videos on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __is_retweet(tweet):
    try:
      tweet.find_element_by_css_selector('[role="presentation"]')
      return True
    except NoSuchElementException:
      return False
    except Exception as ex:
      print("Error at method is_retweet on line no. {} : {}".format(
          frameinfo.f_lineno, ex))
      return False

  @staticmethod
  def __find_name_from_post(tweet):
    try:
      name = "NA"
      anchors = Finder.__find_all_anchor_tags(tweet)
      if len(anchors) > 2:
        name = anchors[1].text.split("\n")[0]
      return name
    except Exception as ex:
      print("Error at method __find_name_from_post on line no. {} : {}".format(
          frameinfo.f_lineno, ex))

  @staticmethod
  def __find_external_link(tweet):
    try:
      card = tweet.find_element_by_css_selector('[data-testid="card.wrapper"]')
      href = card.find_element_by_tag_name('a')
      return href.get_attribute("href")

    except NoSuchElementException:
      return ""
    except Exception as ex:
      print("Error at method __find_external_link on line no. {} : {}".format(
          frameinfo.f_lineno, ex))
