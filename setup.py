from setuptools import setup


version = '0.2'

long_description  = """\
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

"""


setup(name='ParamUnittest',
      version=version,
      description="Simple extension to have parametrized unit tests.",
      long_description=long_description,
      classifiers=[
        'Topic :: Software Development :: Testing',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
      ],
      # Get strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='unittest',
      author='Enrico Franchi',
      author_email='enrico.franchi@gmail.com',
      url='https://github.com/rik0/ParamUnittest',
      license='BSD',
      py_modules = ['paramunittest', ],
      )
