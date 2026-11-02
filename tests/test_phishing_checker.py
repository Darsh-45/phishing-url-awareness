
import os
import sys
import unittest

sys.path.insert(
    0, os.path.dirname(os.path.dirname(__file__))
)

from phishing_checker import inspect_url


class TestPhishingChecker(unittest.TestCase):

    def test_normal_https_url(self):
        result = inspect_url("https://www.example.com/login")
        self.assertIn("does NOT prove", result[0])

    def test_ip_address(self):
        result = inspect_url("http://192.0.2.10/account")
        self.assertTrue(any("IPv4-style" in x for x in result))

    def test_at_symbol(self):
        result = inspect_url(
            "http://example.com@sample.invalid/login"
        )
        self.assertTrue(any("@ symbol" in x for x in result))

    def test_many_hostname_segments(self):
        result = inspect_url(
            "https://a.b.c.d.e.example.invalid/path"
        )
        self.assertTrue(any("five or more" in x for x in result))

    def test_punycode(self):
        result = inspect_url("https://xn--example.invalid/")
        self.assertTrue(any("xn--" in x for x in result))

    def test_long_url(self):
        url = "https://example.com/" + ("a" * 110)
        result = inspect_url(url)
        self.assertTrue(any("longer than 100" in x for x in result))

    def test_empty_input(self):
        self.assertEqual(inspect_url(""), ["No URL entered."])

    def test_malformed_url(self):
        self.assertEqual(
            inspect_url("http://[invalid"),
            ["This text is not a valid URL format."]
        )


if __name__ == "__main__":
    unittest.main()
