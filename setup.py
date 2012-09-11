from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ParamUnittest',
      version=version,
      description="Simple TestCase to have parametrized unit tests.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='unittest',
      author='Enrico Franchi',
      author_email='enrico.franchi@gmail.com',
      url='',
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
