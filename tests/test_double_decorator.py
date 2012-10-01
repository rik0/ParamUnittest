import unittest
from paramunittest import parametrized, ParametrizedTestCase

@parametrized((1, ), (2, ))
@unittest.skipIf(True, "Should skip it.")
class TestSkipLast(ParametrizedTestCase):
    '''Test set and dict comprehension code blocks.'''

    def setParameters(self, value):
        self.value = value

    def testFalse(self):
        self.fail()

#@unittest.skip("Always fails!")
#@parametrized(
#   (0, ),
#   (1, ),
#   (2, ),
#)
#class TestSkipFirst(ParametrizedTestCase):
#    def testFalse(self):
#        self.fail()