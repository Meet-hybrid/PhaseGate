import unittest
from palindrome_flags import get_palindrome

class palindromeFlags(unittest.TestCase):

    def test_true_palindromes(self):
        self.assertTrue(get_palindrome("madam"))
        self.assertTrue(get_palindrome("racecar"))
        self.assertTrue(get_palindrome("a"))
        self.assertTrue(get_palindrome("noon"))

    def test_false_palindromes(self):
        self.assertFalse(get_palindrome("hello"))
        self.assertFalse(get_palindrome("world"))
        self.assertFalse(get_palindrome("python"))

    def test_case_sensitivity(self):
        self.assertFalse(get_palindrome("Madam"))

    def test_empty_string(self):
        self.assertTrue(get_palindrome(""))

