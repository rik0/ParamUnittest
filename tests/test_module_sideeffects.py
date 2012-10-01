import importlib
import unittest
from paramunittest import parametrized, ParametrizedTestCase, _build_name


class TestSideEffects(unittest.TestCase):
    @classmethod
    def getModule(cls):
        module_name = cls.__module__
        return importlib.import_module(module_name)

    def setUp(self):
        self.parameters_tuple = (
            (1, ),
            (2, ),
            (3, )
        )
        @parametrized(*self.parameters_tuple)
        class IntegerTest(ParametrizedTestCase):
            def testFail(self):
                self.fail()
        self.integer_test_name = 'IntegerTest'
        self.integer_test = IntegerTest
        self.module = self.getModule()

    def assertHasAttr(self, obj, name):
        self.assert_(hasattr(obj, name),
                     '%s has not attribute %s' % (obj, name))

    def testModuleGotMoreTests(self):
        for index, _param in enumerate(self.parameters_tuple):
            test_name = _build_name(self.integer_test_name, index)
            self.assertHasAttr(self.module, test_name)


