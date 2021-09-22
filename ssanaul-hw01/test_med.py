#!/usr/bin/env python3

# tests for min_edit_distance.py
import unittest

from min_edit_distance import *


class TestMinEditDistance(unittest.TestCase):

    def test_identical(self):
        self.assertEqual(min_edit_distance("ab", "ab"), 0)

    def test_empty_string(self):
        self.assertEqual(min_edit_distance("", ""), 0)
        self.assertEqual(min_edit_distance("", "ab"), 2)
        self.assertEqual(min_edit_distance("abc", ""), 3)
				
    def test_substring(self):
        self.assertEqual(min_edit_distance("ab", "abc"), 1)
        self.assertEqual(min_edit_distance("cranberry", "err"), 6)
		
    def test_upperbound(self):
        self.assertEqual(min_edit_distance("asdf", "qwerty"), 10)
		
    def test_commutativity(self):
        self.assertEqual(min_edit_distance("asdf", "qwerty"), min_edit_distance("qwerty", "asdf"))
		
if __name__ == '__main__':
	unittest.main()
