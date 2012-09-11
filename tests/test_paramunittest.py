import unittest
import paramunittest

@paramunittest.parametrized(
    ('1', '2'),
    #(4, 3),
    ('2', '3')
)
class Foo(paramunittest.ParametrizedTestCase):
    def setParameters(self, a, b):
        self.a = a
        self.b = b

    def testLess(self):
        self.assertLess(self.a, self.b)
