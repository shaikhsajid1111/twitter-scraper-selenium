import importlib.util
import sys
import types
import unittest
from pathlib import Path


PACKAGE_NAME = "profile_cleanup_test_package"
PACKAGE_PATH = Path(__file__).resolve().parents[1] / "twitter_scraper_selenium"


def load_profile_module():
    package = types.ModuleType(PACKAGE_NAME)
    package.__path__ = [str(PACKAGE_PATH)]
    sys.modules[PACKAGE_NAME] = package

    dependencies = (
        ("driver_initialization", "Initializer"),
        ("driver_utils", "Utilities"),
        ("element_finder", "Finder"),
    )
    for module_name, attribute_name in dependencies:
        module = types.ModuleType("{}.{}".format(PACKAGE_NAME, module_name))
        setattr(module, attribute_name, object)
        sys.modules[module.__name__] = module

    spec = importlib.util.spec_from_file_location(
        "{}.profile".format(PACKAGE_NAME),
        PACKAGE_PATH / "profile.py",
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


profile_module = load_profile_module()


class FailingInitializer:
    def __init__(self, browser, headless, proxy):
        pass

    def init(self):
        raise RuntimeError("driver start failed")


class FakeDriver:
    def __init__(self):
        self.close_calls = 0
        self.quit_calls = 0

    def close(self):
        self.close_calls += 1

    def quit(self):
        self.quit_calls += 1


class ProfileDriverCleanupTests(unittest.TestCase):
    def test_startup_failure_does_not_raise_cleanup_attribute_error(self):
        profile_module.Initializer = FailingInitializer
        profile = profile_module.Profile("xquik", "firefox", None, 1, True)

        with self.assertLogs(profile_module.logger, level="ERROR") as logs:
            result = profile.scrap()

        self.assertIsNone(result)
        self.assertIn("driver start failed", logs.output[0])

    def test_cleanup_closes_an_active_driver_once(self):
        profile = profile_module.Profile("xquik", "firefox", None, 1, True)
        driver = FakeDriver()
        profile._Profile__driver = driver

        profile._Profile__close_driver()
        profile._Profile__close_driver()

        self.assertEqual(1, driver.close_calls)
        self.assertEqual(1, driver.quit_calls)


if __name__ == "__main__":
    unittest.main()
