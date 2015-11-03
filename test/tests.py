#!/usr/bin/env python
#
#  pyhoofinance - tests.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

# Uses PyTest
# To run: py.test tests.py

from datetime import date

from pyhoofinance.historicdata import get_number_of_historical_quotes, get_range_of_historical_quotes
from pyhoofinance import quotedata as q
from pyhoofinance import defs

def test_query_yahoo():
    result = q._query_yahoo(['YHOO'], 'n')
    assert ''.join(result).find('Yahoo') != -1

def test_get_range_of_historical_quotes():
    start_date = date(2015,1,23) # Friday
    end_date = date(2015,1,26) # Monday
    assert len(get_range_of_historical_quotes('YHOO', start_date, end_date)) == 2

def test_get_number_of_historical_quotes():    
    end_date = date(2015,1,26)  # Monday
    quotes = get_number_of_historical_quotes('YHOO', 5, end_date)
    assert len(quotes) == 5

def test_get_quote_block():
    quotes = q._get_quote_block(['YHOO'], [q.SYMBOL_STR], q.YAHOO_FINANCE_KEYS_DICT[q.SYMBOL_STR], [])
    assert len(quotes) == 1
    
def test_format_quote_data():
    quote = [{q.DAY_LOW_STR: '43.875', q.MARKET_CAPITALIZATION_STR : '33B', q.NAME_STR: 'Yahoo! Inc.', q.AVERAGE_DAILY_VOLUME_STR: '21070800', q.SYMBOL_STR: 'YHOO', q.VOLUME_STR: '16281358', q.LAST_TRADE_PRICE_ONLY_STR: '44.045', q.DAY_HIGH_STR: '44.975', q.OPEN_STR: '44.81', q.CHANGE_STR: '-0.655'}]
    result = q._format_quote_data(quote)
    assert result[0][q.DAY_LOW_STR] == 43.875
    assert result[0][q.MARKET_CAPITALIZATION_STR] == 33000000000
           
def test_get_quotes():
    list_size = 1626
    quote_list = ['YHOO' for i in range(list_size)]
    result = q.get_quotes(quote_list)
    assert len(result) == list_size
    # Make sure Error value is present
    assert result[0][q.ERROR_INDICATION_STR].upper() == 'N/A'
    
    # Check that Symbol and Name are inserted
    quote_list = ['YHOO']
    result1 = q.get_quotes(quote_list,[q.SYMBOL_STR, q.NAME_STR])
    result2 = q.get_quotes(quote_list,[])
    assert result1 == result2

    # Check that a bad symbol results in an error indication
    result = q.get_quotes(['N.VLD'],[])
    assert result[0][q.ERROR_INDICATION_STR].upper() != 'N/A'

def test_get_quote():
    #This test may fail if run doing trading hours
    result = q.get_quote('YHOO')
    assert result == q.get_quotes(['YHOO'])[0]