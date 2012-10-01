from paramunittest import ParametrizedTestCase, parametrized

@parametrized((1, ), (2, ))
class TestBase(ParametrizedTestCase):
    def setParameters(self, value):
        self.value = value

    def testOk(self):
        self.assert_(True)


class TestSubClass(TestBase):
    def testOk2(self):
        self.assert_(True)