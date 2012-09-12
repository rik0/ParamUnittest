from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ParamUnittest',
      version=version,
      description="Simple extension to have parametrized unit tests.",
      long_description="""\
      This package allows to create parametrized
      unit-tests that work with the standard unittest package. A
      parametrized test case is automatically converted to multiple test
      cases. Since they are TestCase subclasses, they work with other
      test suites that recognize TestCases.
      """,
      classifiers=[
        'Topic :: Software Development :: Testing',
      ],
      # Get strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='unittest',
      author='Enrico Franchi',
      author_email='enrico.franchi@gmail.com',
      url='https://github.com/rik0/ParamUnittest',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
