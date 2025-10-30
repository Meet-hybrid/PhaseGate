import unittest
from word_reverse import reverse_until_d

class TestReverseUntilD(unittest.TestCase):

	def test_basic(self):
        	result = reverse_until_d("abcddefd")
        	self.assertEqual(result, "dcbadefd") 

    	def test_if_there_is_no_d(self):
        	result = reverse_until_d("mic")
        	self.assertEqual(result, "mic") 

    	def test_if_it_starts_with_d(self):
        	result = reverse_until_d("dmic")
        	self.assertEqual(result, "dmic") 

    	def test_if_it_end_with_d(self):
        	result = reverse_until_d("micd")
        	self.assertEqual(result, "dcim")  
