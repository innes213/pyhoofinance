#!/usr/bin/env python
#
#  pyhoofinance - example1.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

from pyhoofinance import quotedata     # Current stock data
from pyhoofinance import historicdata  # Historic stock data
from pyhoofinance import *             # Useful constants

# Print the Standard quote with data typedef'd for YHOO
print('YAHOO standard quote, typed data')
print(quotedata.get_quotes(['YHOO']))

# Print mini quotes for YHOO, GOOGL, AAPL, MSFT, SPY, and GLD with data as 
# raw strings (done with one query to Yahoo, not 6!).
print('\nMultiple Miniquotes, raw strings:')
for quote in quotedata.get_quotes(['YHOO','GOOGL','AAPL','MSFT','SPY','GLD'],MINIQUOTE,True):
    print (quote)

# Print the last 5 days' worth of historic quote data for YHOO
print('\nYHOO data for the 5 most recent trading days')
for day in historicdata.get_number_of_historical_quotes('YHOO',5):
        print(day)
