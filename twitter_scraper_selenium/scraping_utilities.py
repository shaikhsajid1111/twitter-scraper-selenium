#!/usr/bin/env python3
try:
  from inspect import currentframe
except Exception as ex:
  frameinfo = currentframe()
  print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))


frameinfo = currentframe()

class Scraping_utlities:

  @staticmethod
  def __parse_name(string):
    try:
      return string.split("(")[0].strip()
    except:
      print("Error on line no. {} : {}".format(frameinfo.f_lineno, ex))

  @staticmethod
  def __value_to_float(x):
    try:
        x = float(x)
        return x
    except:
        pass
    x = x.lower()
    if 'k' in x:
        if len(x) > 1:
            return float(x.replace('k', '')) * 1000
        return 1000
    if 'm' in x:
        if len(x) > 1:
            return float(x.replace('m', '')) * 1000000
        return 1000000
    if 'b' in x:
        return float(x.replace('b', '')) * 1000000000
    return 0