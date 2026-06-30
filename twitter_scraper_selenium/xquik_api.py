#!/usr/bin/env python3

import json
import os
from typing import Callable, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen


XQUIK_SEARCH_URL = "https://xquik.com/api/v1/x/tweets/search"


class XquikApiError(Exception):
    """Raised when Xquik search cannot run."""


def _resolve_api_key(api_key: Optional[str]) -> str:
    resolved = api_key or os.getenv("XQUIK_API_KEY")
    if not resolved:
        raise XquikApiError("XQUIK_API_KEY is required for Xquik search")
    return resolved


def _decode_json_response(response):
    payload = response.read()
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8")
    return json.loads(payload)


def search_tweets_with_xquik(
    query: str,
    tweets_count: int = 10,
    query_type: str = "Latest",
    cursor: Optional[str] = None,
    since_time: Optional[str] = None,
    until_time: Optional[str] = None,
    api_key: Optional[str] = None,
    opener: Optional[Callable] = None,
):
    """Search X posts through Xquik without launching Selenium."""

    if not query:
        raise ValueError("query is required")
    if tweets_count < 1 or tweets_count > 100:
        raise ValueError("tweets_count must be between 1 and 100")

    params = {
        "q": query,
        "queryType": query_type,
        "limit": str(tweets_count),
    }
    optional_params = {
        "cursor": cursor,
        "sinceTime": since_time,
        "untilTime": until_time,
    }
    for key, value in optional_params.items():
        if value is not None:
            params[key] = value

    request = Request(
        "{}?{}".format(XQUIK_SEARCH_URL, urlencode(params)),
        headers={
            "Accept": "application/json",
            "x-api-key": _resolve_api_key(api_key),
        },
    )
    transport = opener or urlopen
    response = transport(request, timeout=30)
    return _decode_json_response(response)
