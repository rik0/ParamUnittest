from unittest import skip
import paramunittest

@paramunittest.parametrized(
   (0, ),
   (1, ),
   (2, ),
)
class TrySkipMethod(paramunittest.ParametrizedTestCase):
    @skip("Method Always fails!")
    def testFalse(self):
        self.fail()
