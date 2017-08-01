#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='lecroyreader',
      version='0.1',
      description='Small tool for reading binary .trc files from LeCroy oscilloscopes',
      long_description=readme(),
      url='https://github.com/jneer/lecroy-reader',
      author='Jonas S. Neergaard-Nielsen',
      author_email='j@neer.dk',
      license='MIT',
      packages=['lecroyreader'])
