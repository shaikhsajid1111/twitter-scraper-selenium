#!/usr/bin/env python3

import json
import os
from typing import Any, Callable, Dict, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


XQUIK_SEARCH_URL = "https://xquik.com/api/v1/x/tweets/search"
XQUIK_QUERY_TYPES = ("Latest", "Top")


class XquikApiError(Exception):
    """Raised when Xquik search cannot run."""


def _resolve_api_key(api_key: Optional[str]) -> str:
    resolved = api_key if api_key is not None else os.getenv("XQUIK_API_KEY")
    if resolved is None or not resolved.strip():
        raise XquikApiError("XQUIK_API_KEY is required for Xquik search")
    return resolved.strip()


def _decode_json_response(response: Any) -> Any:
    """Decode one JSON response from the Xquik API."""
    payload = response.read()
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8")
    return json.loads(payload)


def _close_response(response: Any) -> None:
    """Close a response when its transport exposes a close method."""
    close = getattr(response, "close", None)
    if callable(close):
        close()


def search_tweets_with_xquik(
    query: str,
    tweets_count: int = 10,
    query_type: str = "Latest",
    cursor: Optional[str] = None,
    since_time: Optional[str] = None,
    until_time: Optional[str] = None,
    api_key: Optional[str] = None,
    opener: Optional[Callable[..., Any]] = None,
) -> Any:
    """Return one paginated Xquik search response without launching Selenium."""

    if not query or not query.strip():
        raise ValueError("query is required")
    if tweets_count < 1 or tweets_count > 200:
        raise ValueError("tweets_count must be between 1 and 200")
    if query_type not in XQUIK_QUERY_TYPES:
        raise ValueError("query_type must be Latest or Top")

    params: Dict[str, str] = {
        "q": query.strip(),
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
    response = None
    try:
        response = transport(request, timeout=30)
        return _decode_json_response(response)
    except HTTPError as error:
        _close_response(error)
        raise XquikApiError(
            "Xquik request failed with HTTP {}".format(error.code)
        ) from error
    except (URLError, TimeoutError) as error:
        raise XquikApiError(
            "Xquik request failed. Check your network connection."
        ) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise XquikApiError("Xquik returned an invalid JSON response") from error
    finally:
        if response is not None:
            _close_response(response)
