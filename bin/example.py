#!/usr/bin/env python
#
#  pyhoofinance - bin/example.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

"""
This example gets quotes for the entire S&P500 and prints out
the ratio of volume : avg volume as a percentage, sorted low
to high
"""

from pyhoofinance import quotedata
from pyhoofinance import * # This makes some useful constants available, like AVERAGE_DAILY_VOLUME_STR
from operator import itemgetter

# Load symbols into a list
symbollistfile="./input/SandP500.csv" #actually 501 symbols as Google has 2 tickers: GOOG and GOOGL (http://www.cnbc.com/id/101535041)
f = open(symbollistfile)
symbols = f.read().splitlines()
f.close()

# Append a bad symbol for demo purposes
symbols.append('N.VLD')

# Define exactly what data we want (we don't have to do this but it will save a little memory
# Requested item strings are defined in pyhoofinance * 
myQuoteDataRequest = [ERROR_INDICATION_STR, AVERAGE_DAILY_VOLUME_STR, VOLUME_STR]

# Retrieve quotes for entire S&P500
quoteList = quotedata.get_quotes(symbols,myQuoteDataRequest)

# Check for bad symbols, then print their trading volume as a percentage
invalidQuotes = []
validQuotes = []

for quote in quoteList:
    
    # Check if Yahoo reported an error regarding the symbol
    if quote[ERROR_INDICATION_STR].find('N/A') == -1:
        invalidQuotes.append(quote)
    else:
        # Do something with the data!
        quote['volumeAsPercentage'] = 100 * quote[VOLUME_STR] / quote[AVERAGE_DAILY_VOLUME_STR]
        validQuotes.append(quote)

# Sort and display the valid results by volume ratio
validQuotes = sorted(validQuotes, key=itemgetter('volumeAsPercentage'),reverse = False)
for quote in validQuotes:
    print('{:5} volume to average volume percentage = {:.2f}%'.format(quote[SYMBOL_STR],quote['volumeAsPercentage']))
        
# Display bad symbols
if len(invalidQuotes) > 0:
    print('\n\nThe following symbols are invalid:')
    for quote in invalidQuotes:
        print('{0} Error: {1}'.format(quote[SYMBOL_STR],quote[ERROR_INDICATION_STR]))        
        