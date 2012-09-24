from unittest import skip
import paramunittest

@skip("Always fails!")
@paramunittest.parametrized(
   (0, ),
   (1, ),
   (2, ),
)
class TrySkipWhole(paramunittest.ParametrizedTestCase):
    def testFalse(self):
        self.assert_(False)