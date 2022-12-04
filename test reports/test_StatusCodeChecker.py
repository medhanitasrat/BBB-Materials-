import StatusCodeChecker
import unittest

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/74.0.3729.169 Safari/537.36 '
}
timeout = 5

class test_statusCodeChecker(unittest.TestCase):
    def test_statusCode(self):
        url1 = "https://www.discountplumbers.com"
        url2 = "http://www.mnintegrity.com"
        url3 = "https://www.ablemovingcorp.com/"

        result1 = StatusCodeChecker.status_code(url1, headers, timeout)
        result2 = StatusCodeChecker.status_code(url2, headers, timeout)
        result3 = StatusCodeChecker.status_code(url3, headers, timeout)

        self.assertEqual(result1, 200)
        self.assertEqual(result2, 404)
        self.assertEqual(result3, -1)


if __name__ == '__main__':
    unittest.main()
