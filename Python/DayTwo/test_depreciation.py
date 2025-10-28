import unittest
from depreciation_functions import get_depreciated_value


class MyDepreciationFunction(unittest.TestCase):

	def test_for_percentage_in_the_first_year(self):
		result = get_depreciated_value(8)
		self.assertEqual(result,4000)

	def test_for_percentage_in_the_second_year(self):
		result = get_depreciated_value(16)
		self.assertEqual(result,7360)
	
	def test_for_percentage_in_the_third_year(self):
		result = get_depreciated_value(24)
		self.assertEqual(result,9273.6)

	def test_for_percentage_in_the_fourth_year(self):
		result = get_depreciated_value(32)
		self.assertEqual(result,9397.12)

	def test_for_percentage_in_the_fift_year(self):
		result = get_depreciated_value(40)
		self.assertEqual(result,7987.2)