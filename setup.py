#!/usr/bin/env python
#
#  pyhoofinance - setup.py
#
#  Copyright (c) 2014-2016, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the
# GNU General Public License (or the Lesser GPL)
# version 3.

from setuptools import setup, find_packages

__version__ = '0.2.3'
setup(
    name='pyhoofinance',
    version=__version__,
    author='Rob Innes Hislop',
    author_email='robinneshislop_at_gmail.com',
    packages=find_packages(),
    license='GNU LGPL License',
    url = 'https://github.com/innes213/pyhoofinance',
    description='Set of functions for retreiving equity data from Yahoo finance',
    long_description='This module queries Yahoo Finance for multiple tickers and rapidly returns typed data. It will also retrieve historic information, formatted into the proper data type. It is designed for performing analysis quickly with large numbers of symbols.'
)
