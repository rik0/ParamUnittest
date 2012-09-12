from setuptools import setup, find_packages
import sys, os
from os import path


version = '0.1'

examples_directory = 'examples'
example_filename = 'example.py'

def example_text(examples_directory=examples_directory,
                 example_filename=example_filename):
    rel_path = path.join(examples_directory, example_filename)
    with open(rel_path) as fh:
        return fh.read()

long_description  = """\
This package allows to create parametrized unit-tests that work with the
standard unittest package. A parametrized test case is automatically
converted to multiple test cases. Since they are TestCase subclasses,
they work with other test suites that recognize TestCases.


== Examples ==

%s
      """ % example_text()


setup(name='ParamUnittest',
      version=version,
      description="Simple extension to have parametrized unit tests.",
      long_description=long_description,
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
