import unittest

from paramunittest.core import _process_parameters

class TestProcessParametersSeq(unittest.TestCase):
    def testDictOnly(self):
        parameters = [
            dict(foo=1, bar=2),
            dict(a='a', b='b')
        ]

        self.assertListEqual(
            [(tuple(), p) for p in parameters], _process_parameters(parameters))

    def testArgOnly(self):
        parameters = [
            (dict(foo=1, bar=2), ),
            (dict(a='a', b='b'), ),
            ('a', 'b', 'c'),
            tuple('foo')
        ]

        self.assertListEqual(
            [(p, {}) for p in parameters], _process_parameters(parameters))

    def testShortSyntax(self):
        parameters = [
            ((1, 2), dict(foo=1, bar=2), ),
            (('a', 'b'), dict(a='a', b='b'), ),
            (('a', 'b', 'c'), {'foo': 'foo', 'bar': 'bar'}),
            (tuple('foo'), {})
        ]

        self.assertListEqual(parameters, _process_parameters(parameters))