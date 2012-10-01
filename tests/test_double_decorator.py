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

# TODO: Fix this, because it is broken!

@unittest.skip("Always fails!")
@parametrized(
   (0, ),
   (1, ),
   (2, ),
)
class TestSkipFirst(ParametrizedTestCase):
    def setParameters(self, value):
        self.value = value

    def testFalse(self):
        self.fail()