import unittest
from symbol import Symbol

class TestSymbol(unittest.TestCase):

    def test_empty_symbol(self):
        s = Symbol(None)
        self.assertEqual(s.value, None)
        
    def test_nonempty_symbol(self):
        values = ["NP", "S", "the", "banana"]
        for value in values:
            s = Symbol(value)
            self.assertEqual(s.value, value)
    
    def test_nonstring_symbol(self):
        value = 1
        s = Symbol(value)
        self.assertEqual(s.value, "1")

    def test_equals_true(self):
        values = ["NP", "S", "the", "banana", None]
        for value in values:
            s1 = Symbol(value)
            s2 = Symbol(value)
            self.assertTrue(s1==s2, True)

    def test_equals_false(self):
        s1_values = ["NP", "S", "the", "banana"]
        s2_values = [None, "VP", "walked"]
        for s1_value in s1_values:
            s1 = Symbol(s1_value)
            for s2_value in s2_values:
                s2 = Symbol(s2_value)
                self.assertFalse(s1 == s2)

    def test_equals_notimplemented(self):
        other_values = [7, 3.14, None, "abcde"]
        values = ["NP", "S", "the", "abcde", "banana", None]   
        for value in values:
            s = Symbol(value)
            for other in other_values:
                self.assertEqual(s.__eq__(other), NotImplemented)

    def test_hash(self):
        values = ["NP", None, "S", "abcde", "the", 1, 3.14]
        for value in values:
            s = Symbol(value)
            h = hash(s)
            if value is None:
                self.assertEqual(h, hash(None))
            else:
                self.assertEqual(h, hash(str(s.value)))

    def test_string_none(self):
        s = Symbol(None)
        self.assertEqual(str(s), "\u03b5")

    def test_string_nonnone(self):
        values = ["NP", "S", "abcde", "the", 1, 3.14]
        for value in values:
            s = Symbol(value)
            self.assertEqual(str(s), str(value))

    def test_bool_none(self):
        s = Symbol(None)
        self.assertFalse(bool(s))

    def test_bool_nonnone(self):
        values = ["NP", "S", "abcde", "the", 1, 3.14]
        for value in values:
            s = Symbol(value)
            self.assertTrue(bool(s))

    def test_len_none(self):
        s = Symbol(None)
        self.assertEqual(len(s), 0)

    def test_len_nonnone(self):
        values = ["NP", "S", "abcde", "the", 1, 3.14]
        for value in values:
            s = Symbol(value)
            self.assertEqual(len(s), len(s.value))
            self.assertEqual(len(s), len(str(s.value)))

    def test_isepsilon(self):
        s1 = Symbol(None)
        self.assertTrue(s1.isEpsilon())
        values = ["NP", "S", "abcde", "the", 1, 3.14]
        for value in values:
            s2 = Symbol(value)
            self.assertFalse(s2.isEpsilon())

    def test_isNonTerminal(self):
        s1 = Symbol(None)
        self.assertFalse(s1.isNonTerminal())
        terminals = ["abcde", "the", 1, 3.14]
        nt_values = ["NP", "S", "Hello"]
        for value in nt_values:
            s = Symbol(value)
            self.assertTrue(s.isNonTerminal())
            self.assertFalse(s.isTerminal())
        for value in terminals:
            s = Symbol(value)
            self.assertFalse(s.isNonTerminal())
            self.assertTrue(s.isTerminal())

if __name__ == '__main__':
    unittest.main()

