import importlib.util
import unittest
from pathlib import Path
from urllib.parse import parse_qs, urlparse


MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "twitter_scraper_selenium"
    / "xquik_api.py"
)
SPEC = importlib.util.spec_from_file_location("xquik_api", MODULE_PATH)
xquik_api = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(xquik_api)


class FakeResponse:
    def read(self):
        return b'{"data": [{"id": "1", "text": "hello"}]}'


class FakeOpener:
    def __init__(self):
        self.request = None
        self.timeout = None

    def __call__(self, request, timeout):
        self.request = request
        self.timeout = timeout
        return FakeResponse()


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

    def test_requires_api_key(self):
        with self.assertRaises(xquik_api.XquikApiError):
            xquik_api.search_tweets_with_xquik("xquik", api_key="")

    def test_validates_tweets_count(self):
        with self.assertRaises(ValueError):
            xquik_api.search_tweets_with_xquik(
                "xquik",
                tweets_count=0,
                api_key="test-key",
            )


if __name__ == "__main__":
    unittest.main()
