#!/usr/bin/env python3
try:
    from inspect import currentframe
    import re
    from urllib.parse import quote
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

    @staticmethod
    def __set_value_or_none(value, string):
        return string+str(value)+" " if value is not None else None

    @staticmethod
    def __url_generator(keyword, since=None, until=None,
                        since_id=None, max_id=None, within_time=None):
        base_url = "https://twitter.com/search?q="
        if within_time is None:
            words = [Scraping_utilities.__set_value_or_none(since, "since:"),
                     Scraping_utilities.__set_value_or_none(
                until, "until:"),
                Scraping_utilities.__set_value_or_none(
                since_id, "since_id:"), Scraping_utilities.__set_value_or_none(max_id, "max_id:")]
            query = ""
            for word in words:
                if word is not None:
                    query += word
            query += keyword
            query = quote(query)
            base_url = base_url + query + "&src=typed_query&f=live"
        else:
            word = Scraping_utilities.__set_value_or_none(
                within_time, "within_time:")
            query = keyword + " " + word
            base_url = base_url + quote(query) + "&src=typed_query&f=live"
        return base_url
