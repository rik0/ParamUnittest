from unittest import skip
import paramunittest

@paramunittest.parametrized(
   (0, ),
   (1, ),
   (2, ),
)
class TrySkipMethod(paramunittest.ParametrizedTestCase):
    @skip("Always fails!")
    def testFalse(self):
        self.assert_(False)
