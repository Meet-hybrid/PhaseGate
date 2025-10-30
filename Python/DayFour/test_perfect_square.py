import unittest
from perfect_square import is_perfect_square, all_perfect_squares

class TestPerfectSquareFunctions(unittest.TestCase):

    def test_is_perfect_square_true(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(100))

    def test_is_perfect_square_false(self):
        self.assertFalse(is_perfect_square(-1))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(99))

    def test_all_perfect_squares(self):
        self.assertTrue(all_perfect_squares(25))
        self.assertFalse(all_perfect_squares(26))


