#!/usr/bin/env python3
try:
  from inspect import currentframe
  import re
except Exception as ex:
  frameinfo = currentframe()
  print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))


frameinfo = currentframe()

class Scraping_utilities:

  @staticmethod
  def __parse_name(string):
    try:
      return string.split("(")[0].strip()
    except:
      print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))

  @staticmethod
  def __extract_digits(string):
    try:
      return int(re.search(r'\d+', string).group(0))
    except Exception as ex:
      print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))
