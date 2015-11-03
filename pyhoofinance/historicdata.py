#!/usr/bin/env python
#
#  pyhoofinance - historicdata.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

import urllib2
from datetime import timedelta
from datetime import datetime

from defs import *

def get_range_of_historical_quotes(symbol, start_date, end_date=datetime.today()):
    """
    Get historical quotes for the given ticker symbol for the range [start_date:end_date].
    Returns a list of dictionaries
    Args:
        symbol (string) ticker symbol for data being retrieved
        start_date (date) the first date to retrieve
        end_date (Optional[date]) the last (most recent_ date to retrieve
    """
    
    # URL should look like: http://real-chart.finance.yahoo.com/table.csv?s=AAPL&a=11&b=12&c=1980&d=06&e=11&f=2014&g=d&ignore=.csv
    url = 'http://real-chart.finance.yahoo.com/table.csv?s=%s&' % symbol + \
    'a=%s&' % str(int(start_date.month) -1 ) + \
    'b=%s&' % str(int(start_date.day)) + \
    'c=%s&' % str(int(start_date.year)) + \
    'd=%s&' % str(int(end_date.month) - 1 ) + \
    'e=%s&' % str(int(end_date.day)) + \
    'f=%s&' % str(int(end_date.year)) + \
    'g=d&ignore=.csv'
    
    historical_list = [] 
    try:
        response = urllib2.urlopen(url)
    except:
        print 'urlopen failed.'
        return []
    
    if response.msg != 'OK':
        print 'URL error: %s' % response.msg
        return []
    
    raw_data_block = response.read().splitlines()
        
    for data_line in raw_data_block[1:]:
        try:
            data = {}
            raw_data = data_line.strip().strip('"').split(',')

            data[TRADE_DATE_STR]                  = datetime.strptime(raw_data[0],'%Y-%m-%d').date()
            data[OPEN_STR]                        = float(raw_data[1])
            data[DAY_HIGH_STR]                    = float(raw_data[2])
            data[DAY_LOW_STR]                     = float(raw_data[3])
            data[LAST_TRADE_PRICE_ONLY_STR]       = float(raw_data[4])
            data[VOLUME_STR]                      = float(raw_data[5])
            data[ADJUSTED_CLOSE_STR]              = float(raw_data[6])
            data[SYMBOL_STR]                      = symbol

            historical_list.insert(0,data)
        except:
            print 'get_range_of_historical_quotes() error. Symbol: %s' % symbol
            return []

    return historical_list

def get_number_of_historical_quotes(symbol, num_days, end_date=datetime.today()):
    """
    Get historical prices for the given ticker symbol for a number of trading days ending
    with end_date. If end_date is not a trading day, the closest past trading day is the 
    starting point. Returns a list of dictionaries.
    Args:
        symbol (string) Ticker symbol for data being retrieved
        num_days (integer} Number of trading days of data to retrieve
        end_date (Optional[date]) Last (most recent) day for which data is retrieved
    """
    
    historical_list = []

    delta_date = timedelta(days = int(num_days * 1.5 + 5))
    historical_list = get_range_of_historical_quotes(symbol, end_date - delta_date, end_date)[-num_days:]
    
    return historical_list

