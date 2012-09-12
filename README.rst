This package allows to create parametrized unit-tests that work with the
standard unittest package. A parametrized test case is automatically
converted to multiple test cases. Since they are TestCase subclasses,
they work with other test suites that recognize TestCases.

Examples::

    import unittest
    import paramunittest
    
    @paramunittest.parametrized(
        ('1', '2'),
        #(4, 3),
        ('2', '3'),
        (('4', ), {'b': '5'}),
        ((), {'a': 5, 'b': 6}),
        {'a': 5, 'b': 6},
    )
    class TestFoo(paramunittest.ParametrizedTestCase):
        def setParameters(self, a, b):
            self.a = a
            self.b = b
    
        def testLess(self):
            self.assertLess(self.a, self.b)
    
    @paramunittest.parametrized(
        ('1', '2'),
        #(4, 3),
        ('2', '3'),
        (('4', ), {'b': '5'}),
        ((), {'a': 5, 'b': 6}),
        {'a': 5, 'b': 6},
    )
    class TestBar(unittest.TestCase):
        def setParameters(self, a, b):
            self.a = a
            self.b = b
    
        def testLess(self):
            self.assertLess(self.a, self.b)

