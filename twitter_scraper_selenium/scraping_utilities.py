#!/usr/bin/env python3
import re
from typing import Union
from urllib.parse import quote
import logging
import requests
from fake_headers import Headers
import json

logger = logging.getLogger(__name__)
format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(format)
logger.addHandler(ch)


class Scraping_utilities:
    """
    This class contains all utility methods that help cleaning or extracting
    data from raw data.

    @staticmethod
    def method_name(parameters)
    """

    @staticmethod
    def parse_name(string) -> Union[str, None]:
        """Extract name from the given string.
           Example:
           Input: jack(@jack)
           Output: jack
        """
        try:
            return string.split("(")[0].strip()
        except Exception as ex:
            logger.exception("Error at parse_name : {}".format(ex))

    @staticmethod
    def extract_digits(string) -> Union[int, None]:
        """Extracts first digits from the string.

        Args:
          string (str): string containing digits.

        Returns:
          int: digit that was extracted from the passed string
        """
        try:
            return int(re.search(r'\d+', string).group(0))
        except Exception as ex:
            logger.exception("Error at extract_digits : {}".format(ex))

    @staticmethod
    def set_value_or_none(value, string) -> Union[str, None]:
        return string+str(value)+" " if value is not None else None

    @staticmethod
    def url_generator(keyword: str, since: Union[int, None] = None, until: Union[str, None] = None,
                      since_id: Union[int, None] = None, max_id: Union[int, None] = None,
                      within_time: Union[str, None] = None) -> str:
        """Generates Twitter URL for passed keyword

        Args:
            keyword (str): Keyword to search on twitter.
            since (Union[int, None], optional): Optional parameter,Since date for scraping,a past date from where to search from. Format for date is YYYY-MM-DD or unix timestamp in seconds. Defaults to None.
            until (Union[str, None], optional): Optional parameter,Until date for scraping,a end date from where search ends. Format for date is YYYY-MM-DD or unix timestamp in seconds. Defaults to None.
            since_id (Union[int, None], optional): After (NOT inclusive) a specified Snowflake ID. Defaults to None.
            max_id (Union[int, None], optional): At or before (inclusive) a specified Snowflake ID. Defaults to None.
            within_time (Union[str, None], optional): Search within the last number of days, hours, minutes, or seconds. Defaults to None.

        Returns:
            str: Twitter URL
        """
        base_url = "https://twitter.com/search?q="
        if within_time is None:
            words = [Scraping_utilities.set_value_or_none(since, "since:"),
                     Scraping_utilities.set_value_or_none(
                until, "until:"),
                Scraping_utilities.set_value_or_none(
                since_id, "since_id:"), Scraping_utilities.set_value_or_none(max_id, "max_id:")]
            query = ""
            for word in words:
                if word is not None:
                    query += word
            query += keyword
            query = quote(query)
            base_url = base_url + query + "&src=typed_query&f=live"
        else:
            word = Scraping_utilities.set_value_or_none(
                within_time, "within_time:")
            query = keyword + " " + word
            base_url = base_url + quote(query) + "&src=typed_query&f=live"
        return base_url

    @staticmethod
    def make_http_request_with_params(URL, params, headers, proxy=None):
        try:
            response = None
            if proxy:
                proxy_dict = {
                    "http": "http://{}".format(proxy),
                    "https": "http://{}".format(proxy)
                }
                response = requests.get(URL, params=params, headers=headers,
                                        proxies=proxy_dict)
            else:
                response = requests.get(URL, params=params, headers=headers)
            if response and response.status_code == 200:
                return response.json()
        except Exception as ex:
            logger.warning("Error at make_http_request: {}".format(ex))

    @staticmethod
    def make_http_request(URL, headers, proxy=None):
        try:
            response = None
            if proxy:
                proxy_dict = {
                    "http": "http://{}".format(proxy),
                    "https": "http://{}".format(proxy)
                }
                response = requests.get(URL, headers=headers,
                                        proxies=proxy_dict)
            else:
                response = requests.get(URL, headers=headers)
            if response and response.status_code == 200:
                return response.json()
        except Exception as ex:
            logger.warning("Error at make_http_request: {}".format(ex))

    @staticmethod
    def build_params(query, cursor=None):
        params = {
            'include_profile_interstitial_type': '1',
            'include_blocking': '1',
            'include_blocked_by': '1',
            'include_followed_by': '1',
            'include_want_retweets': '1',
            'include_mute_edge': '1',
            'include_can_dm': '1',
            'include_can_media_tag': '1',
            'include_ext_has_nft_avatar': '1',
            'skip_status': '1',
            'cards_platform': 'Web-12',
            'include_cards': '1',
            'include_ext_alt_text': 'true',
            'include_ext_limited_action_results': 'false',
            'include_quote_count': 'true',
            'include_reply_count': '1',
            'tweet_mode': 'extended',
            'include_ext_collab_control': 'true',
            'include_entities': 'true',
            'include_user_entities': 'true',
            'include_ext_media_color': 'true',
            'include_ext_media_availability': 'true',
            'include_ext_sensitive_media_warning': 'true',
            'include_ext_trusted_friends_metadata': 'true',
            'send_error_codes': 'true',
            'simple_quoted_tweet': 'true',
            'q': query,
            'vertical': 'trends',
            'count': '20',
            'query_source': 'typed_query',
            'pc': '1',
            'spelling_corrections': '1',
            'include_ext_edit_control': 'true',
            'ext': 'mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collab_control,vibe',
        }
        if cursor:
            params['cursor'] = cursor
        return params

    @staticmethod
    def build_keyword_headers(x_guest_token, authorization_key, query=None):
        headers = {
            'authority': 'twitter.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': authorization_key,
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': Headers().generate()['User-Agent'],
            'x-guest-token': x_guest_token,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en',
        }
        if query:
            headers['referer'] = "https://twitter.com/search?q={}".format(
                query)
        return headers

    @staticmethod
    def build_topic_headers(x_guest_token, authorization_key, rest_id=None):
        headers = {
            'authority': 'twitter.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': authorization_key,
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': Headers().generate()['User-Agent'],
            'x-guest-token': x_guest_token,
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en',
        }
        if rest_id:
            headers['referer'] = "https://twitter.com/i/topics/{}".format(
                rest_id)
        return headers

    @staticmethod
    def find_x_guest_token(authorization_key, proxy=None):
        try:
            headers = {
                'authorization': authorization_key,
            }
            response = None
            if proxy:
                proxy_dict = {
                    "http": "http://{}".format(proxy),
                    "https": "http://{}".format(proxy),
                }
                response = requests.post(
                    'https://api.twitter.com/1.1/guest/activate.json', headers=headers, proxies=proxy_dict)
                return response.json()['guest_token']

            response = requests.post(
                'https://api.twitter.com/1.1/guest/activate.json', headers=headers)
            return response.json()['guest_token']
        except Exception as ex:
            logger.warning("Error at find_x_guest_token: {}".format(ex))

    @staticmethod
    def build_topic_params(rest_id, cursor):
        variables = {"rest_id": rest_id, "context": "{}", "withSuperFollowsUserFields": True, "withDownvotePerspective": False,
                     "withReactionsMetadata": False, "withReactionsPerspective": False, "withSuperFollowsTweetFields": True}
        if cursor:
            variables["cursor"] = cursor
        params = {
            'variables': json.dumps(variables),
            'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"verified_phone_label_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"unified_cards_ad_metadata_container_dynamic_card_content_query_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_uc_gql_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"responsive_web_enhance_cards_enabled":true}',
        }
        return params

    @staticmethod
    def build_params_for_profile(user_id, cursor=None):
     variables = {
         "userId": str(user_id),
         "count": 40,
         "includePromotedContent": True,
         "withQuickPromoteEligibilityTweetFields": True,
         "withSuperFollowsUserFields": True,
         "withDownvotePerspective": False,
         "withReactionsMetadata": False,
         "withReactionsPerspective": False,
         "withSuperFollowsTweetFields": True,
         "withVoice": True,
         "withV2Timeline": True,
     }
     if cursor:
         variables["cursor"] = cursor
     params = {
         "variables": json.dumps(variables),
          'features': '{"responsive_web_twitter_blue_verified_badge_is_enabled":true,"verified_phone_label_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"view_counts_public_visibility_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":false,"tweetypie_unmention_optimization_enabled":true,"responsive_web_uc_gql_enabled":true,"vibe_api_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":false,"interactive_text_enabled":true,"responsive_web_text_conversations_enabled":false,"responsive_web_enhance_cards_enabled":false}',
     }
     return params