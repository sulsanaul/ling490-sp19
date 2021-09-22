import unittest
from rule import Rule
from symbol import Symbol

class TestRule(unittest.TestCase):

    def test_constructor(self):
        lhs = Symbol('S')
        rhs = [Symbol('NP'), Symbol('VP')]
        r   = Rule(lhs, rhs)
        self.assertEqual(lhs, r.lhs)
        self.assertEqual(rhs, r.rhs)
        self.assertRaises(RuntimeError, lambda: Rule('not a symbol', rhs))
        self.assertRaises(RuntimeError, lambda: Rule(lhs, ['not a symbol']))
        self.assertRaises(RuntimeError, lambda: Rule(lhs, [Symbol(None), 'not a symbol']))

    def test_equals(self):
        r1 = Rule(Symbol('S'), [Symbol('NP'), Symbol('VP')])
        r2 = Rule(Symbol('S'), [Symbol('NP'), Symbol('VP')])
        self.assertEqual(r1.__eq__('not a rule'), NotImplemented)
        self.assertTrue(r1 == r2)

    def test_bool(self):
        r1 = Rule(Symbol('S'), [Symbol(None)])
        self.assertFalse(bool(r1))
        r2 = Rule(Symbol('S'), [Symbol('NP')])
        self.assertTrue(bool(r2))
if __name__ == '__main__':
    unittest.main()
