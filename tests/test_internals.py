import unittest

from paramunittest import _process_parameters, ParametrizedTestCase, parametrized

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

class TestParametrizeRequiresSetParameters(unittest.TestCase):
    def testWithTestCaseNoSetParameters(self):
        with self.assertRaises(Exception):
            @parametrized()
            class NonParametrized(unittest.TestCase):
                def test(self):
                    self.fail()

    def testWithTestCaseSetParameters(self):
        @parametrized()
        class NonParametrized(unittest.TestCase):
            def setParameters(self):
                pass

            def test(self):
                self.fail()
        self.assertIsNone(NonParametrized)

    def testWithParametrizedTestCase(self):
        @parametrized()
        class Parametrized(ParametrizedTestCase):
            def test(self):
                self.fail()
        self.assertIsNone(Parametrized)

