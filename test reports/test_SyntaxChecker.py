import SyntaxChecker
import unittest


class test_syntaxChecker(unittest.TestCase):

    def test_check_syntax(self):
        good_url = "http://www.midwestcanine.com/"

        bad_url1 = "http://www.verndalecustombuilders,com"  # ,com instead of .com
        bad_url2 = "http://www.verndalecustombuilders.com;"  # have special character at the end
        bad_url3 = "http://www.verndalecustombuilderscom"  # No '.' before top level domain

        good_result = SyntaxChecker.check_syntax(good_url)

        bad_result1 = SyntaxChecker.check_syntax(bad_url1)
        bad_result2 = SyntaxChecker.check_syntax(bad_url2)
        bad_result3 = SyntaxChecker.check_syntax(bad_url3)

        self.assertTrue(good_result, "failed")

        self.assertFalse(bad_result1, "failed")
        self.assertFalse(bad_result2, "failed")
        self.assertFalse(bad_result3, "failed")

    def test_fix(self):
        bad_url1 = "http://www.verndalecustombuilders,com"
        bad_url2 = "http://www.verndalecustombuilders.com;"
        bad_url3 = "http://www.verndalecustombuilderscom"

        fixed_url1 = SyntaxChecker.fix(bad_url1)
        fixed_url2 = SyntaxChecker.fix(bad_url2)
        fixed_url3 = SyntaxChecker.fix(bad_url3)

        self.assertEqual(fixed_url1, "http://www.verndalecustombuilders.com")
        self.assertEqual(fixed_url2, "http://www.verndalecustombuilders.com")
        self.assertEqual(fixed_url3, "http://www.verndalecustombuilders.com")

    def test_verify(self):
        good_url = "http://www.verndalecustombuilders.com"

        bad_url1 = "http://www.verndalecustombuilders,com"
        bad_url2 = "http://www.verndalecustombuilders.com;"
        bad_url3 = "https://www.problem.com/search/results?_page=%PageNum%&sourcecategory=life%20events%20(bmds)&collection=civil%20births&lastname=%Letter%*&datasetname=irish%20births%201864-1958&sourcecountry=ireland&yearofbirth=1955&yearofbirth_offset=0&sid=999"

        result = SyntaxChecker.verify(good_url)

        result1 = SyntaxChecker.verify(bad_url1)
        result2 = SyntaxChecker.verify(bad_url2)
        result3 = SyntaxChecker.verify(bad_url3)

        self.assertEqual(result, (True, "http://www.verndalecustombuilders.com"))

        self.assertEqual(result1, (True, "http://www.verndalecustombuilders.com"))
        self.assertEqual(result2, (True, "http://www.verndalecustombuilders.com"))
        self.assertEqual(result3, (False,
                                   "https://www.problem.com/search/results?_page=%PageNum%&sourcecategory=life%20events%20(bmds)&collection=civil%20births&lastname=%Letter%*&datasetname=irish%20births%201864-1958&sourcecountry=ireland&yearofbirth=1955&yearofbirth_offset=0&sid=999"))


if __name__ == '__main__':
    unittest.main()
