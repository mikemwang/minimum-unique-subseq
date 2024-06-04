import unittest

from common import get_all_subsequences

class TestGetAllSubsequences(unittest.TestCase):
    def test_empty_string(self):
        self.assertCountEqual(get_all_subsequences(''), [])
    
    def test_single_strings(self):
        self.assertCountEqual(get_all_subsequences('a'), ['a'])
    
    def test_repeat_chars(self):
        self.assertCountEqual(get_all_subsequences('aa'), ['a', 'a', 'aa'])
    
    def test_abc(self):
        self.assertCountEqual(
            get_all_subsequences('abc'), 
            ['a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
        )

if __name__=='__main__':
    unittest.main()