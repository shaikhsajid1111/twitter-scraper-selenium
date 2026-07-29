import importlib.util
import unittest
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlparse


MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "twitter_scraper_selenium" / "xquik_api.py"
)
SPEC = importlib.util.spec_from_file_location("xquik_api", MODULE_PATH)
xquik_api = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(xquik_api)


class FakeResponse:
    def __init__(self, body=b'{"data": [{"id": "1", "text": "hello"}]}'):
        self.body = body
        self.closed = False

    def read(self):
        return self.body

    def close(self):
        self.closed = True


class FakeOpener:
    def __init__(self, response=None, error=None):
        self.request = None
        self.timeout = None
        self.response = response if response is not None else FakeResponse()
        self.error = error

    def __call__(self, request, timeout):
        self.request = request
        self.timeout = timeout
        if self.error is not None:
            raise self.error
        return self.response


class XquikApiTests(unittest.TestCase):
    def test_builds_search_request(self):
        opener = FakeOpener()

        result = xquik_api.search_tweets_with_xquik(
            "python",
            tweets_count=15,
            api_key="test-key",
            opener=opener,
        )

        parsed_url = urlparse(opener.request.full_url)
        query = parse_qs(parsed_url.query)
        self.assertEqual("xquik.com", parsed_url.netloc)
        self.assertEqual(["python"], query["q"])
        self.assertEqual(["Latest"], query["queryType"])
        self.assertEqual(["15"], query["limit"])
        self.assertEqual("test-key", opener.request.headers["X-api-key"])
        self.assertEqual(30, opener.timeout)
        self.assertEqual({"data": [{"id": "1", "text": "hello"}]}, result)
        self.assertTrue(opener.response.closed)

    def test_includes_optional_search_parameters(self):
        opener = FakeOpener()

        xquik_api.search_tweets_with_xquik(
            "from:python",
            tweets_count=200,
            query_type="Top",
            cursor="next-page",
            since_time="2026-07-01",
            until_time="2026-07-29",
            api_key="test-key",
            opener=opener,
        )

        query = parse_qs(urlparse(opener.request.full_url).query)
        self.assertEqual(["200"], query["limit"])
        self.assertEqual(["Top"], query["queryType"])
        self.assertEqual(["next-page"], query["cursor"])
        self.assertEqual(["2026-07-01"], query["sinceTime"])
        self.assertEqual(["2026-07-29"], query["untilTime"])

    def test_requires_api_key(self):
        with self.assertRaises(xquik_api.XquikApiError):
            xquik_api.search_tweets_with_xquik("xquik", api_key=" ")

    def test_validates_search_parameters(self):
        invalid_arguments = (
            {"query": " ", "api_key": "test-key"},
            {"query": "xquik", "tweets_count": 0, "api_key": "test-key"},
            {"query": "xquik", "tweets_count": 201, "api_key": "test-key"},
            {
                "query": "xquik",
                "query_type": "Popular",
                "api_key": "test-key",
            },
        )
        for arguments in invalid_arguments:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    xquik_api.search_tweets_with_xquik(**arguments)

    def test_wraps_invalid_json_and_closes_response(self):
        opener = FakeOpener(response=FakeResponse(b"not-json"))

        with self.assertRaisesRegex(
            xquik_api.XquikApiError,
            "invalid JSON",
        ):
            xquik_api.search_tweets_with_xquik(
                "xquik",
                api_key="test-key",
                opener=opener,
            )

        self.assertTrue(opener.response.closed)

    def test_wraps_http_errors(self):
        response = FakeResponse()
        error = HTTPError(
            xquik_api.XQUIK_SEARCH_URL,
            429,
            "Too Many Requests",
            None,
            response,
        )

        with self.assertRaisesRegex(xquik_api.XquikApiError, "HTTP 429"):
            xquik_api.search_tweets_with_xquik(
                "xquik",
                api_key="test-key",
                opener=FakeOpener(error=error),
            )

        self.assertTrue(response.closed)

    def test_wraps_network_errors(self):
        with self.assertRaisesRegex(
            xquik_api.XquikApiError,
            "network connection",
        ):
            xquik_api.search_tweets_with_xquik(
                "xquik",
                api_key="test-key",
                opener=FakeOpener(error=URLError("offline")),
            )


if __name__ == "__main__":
    unittest.main()
