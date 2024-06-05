import unittest

from common import get_all_subsequences

from algorithm import get_minimum_substrings_brute_force

from data import lol

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

def create_solution_test(fn):
    class TestSolution(unittest.TestCase):
        def test_empty_input(self):
            self.assertDictEqual(fn([]), {})

        def test_ignore_empty_string(self):
            self.assertDictEqual(fn([""]), {})

        def test_simple_string(self):
            self.assertDictEqual(
                fn(['a']), {'a': {'a'}}
            )

        def test_len1_strings(self):
            self.assertDictEqual(
                fn( ['a', 'b']),
                {'a': {'a'}, 'b': {'b'}}
            )
        
        def test_len1_strings_overlap(self):
            self.assertDictEqual(
                fn(['a', 'a']), {'a': {'a'}}
            )
        
        def test_len2_strings_overlap(self):
            self.assertDictEqual(
                fn(['a', 'ab']),
                {'a': set(), 'ab': {'b'}}
            )
            self.assertDictEqual(
                fn(['ac', 'ab']),
                {'ac': {'c'}, 'ab': {'b'}}
            )
        
        def test_len3_strings(self):
            self.assertDictEqual(
                fn(['abc', 'cba']),
                {'abc': {'ab', 'bc', 'ac'} , 'cba': {'cb', 'ba', 'ca'}}
            )
        
        def test_lol(self):
            self.maxDiff = None
            res = fn(lol.CHAMPS)
            self.assertDictEqual(res , lol.EXPECTED)

    return TestSolution

class TestBruteForceSolution(create_solution_test(get_minimum_substrings_brute_force)):
    pass

if __name__=='__main__':
    unittest.main()