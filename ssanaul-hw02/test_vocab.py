#!/usr/bin/env python3

import unittest
from vocab import Vocabulary

class TestVocabulary(unittest.TestCase):

    def test_empty(self):
        """Assert that a newly constructed vocabulary has size zero"""
        v = Vocabulary()
        self.assertEqual(len(v), 0)

    def test_empty_word2int(self):
        """Assert that a newly constructed vocabulary contains an empty dictionary called word2int"""
        v = Vocabulary()
        self.assertTrue(isinstance(v.word2int, dict))
        self.assertEqual(len(v.word2int), 0)

    def test_empty_int2word(self):
        """Assert that a newly constructed vocabulary contains an empty list called int2word"""
        v = Vocabulary()
        self.assertTrue(isinstance(v.int2word, list))
        self.assertEqual(len(v.int2word), 0)


    def test_empty_errors(self):
        """Assert that a newly constructed vocabulary raises appropriate errors"""
        v = Vocabulary()
        with self.assertRaises(IndexError):
            v[0]
        with self.assertRaises(IndexError):
            v[1]
        with self.assertRaises(IndexError):
            v[-1]


    def test_add_one_word(self):
        """Assert that adding a single word to a newly constructed Vocabulary works as expected"""
        v = Vocabulary()
        v += "hello"
        self.assertEqual(len(v), 1)
        self.assertEqual(v["hello"], 0)
        self.assertEqual(v[0], "hello")


    def test_adding_words(self):
        """Assert that words are properly added to the vocabulary"""
        v = Vocabulary()
        tokens = "Four score and seven years ago".split()

        for i, token in enumerate(tokens):
            self.assertEqual(len(v), i)
            with self.assertRaises(IndexError):
                v[i]
            with self.assertRaises(KeyError):
                v[token]
            with self.assertRaises(TypeError):
                v[float(i)]
            v += token
            self.assertEqual(len(v), i+1)
            self.assertEqual(v[i], token)
            self.assertEqual(v[token], i)

        for i, token in enumerate(tokens):
            self.assertEqual(len(v), len(tokens))
            self.assertEqual(v[i], token)
            self.assertEqual(v[token], i)


if __name__ == '__main__':
    unittest.main()
