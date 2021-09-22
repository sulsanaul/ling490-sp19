#!/usr/bin/env python3


import unittest

from node import Node
from trie import Trie

class TestStringMethods(unittest.TestCase):

    def test_max_size(self):
        max_size = 256
        node = Node(max_size)
        self.assertEqual(node.max_size, max_size)


    def test_empty_length(self):
        max_size = 256
        node = Node(max_size)
        self.assertEqual(len(node), 0)


    def test_empty_children(self):
        max_size = 256
        node = Node(max_size)
        for i in range(0, max_size):
            self.assertEqual(i in node, False)


    def test_nonempty_children(self):
        max_size = 256
        node = Node(max_size)
        for i in range(0, max_size):
            self.assertEqual(i in node, False)
            self.assertEqual(len(node), i)
            self.assertTrue(isinstance(node[i], Node))
            self.assertEqual(i in node, True)
            self.assertEqual(len(node), i+1)



if __name__ == '__main__':


    print("Creating Trie...")
    x = Trie()

    print("Storing items...")
    x["hell"]  = 4
    x["he"]    = 7
    x["hi"]    = 8
    x["hello"] = 1

    print("Retrieving items...")

    for item in ["hell", "he", "hi", "hello"]:

        print(item, item in x)


    unittest.main()

