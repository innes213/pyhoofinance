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

from defs import *
import urllib2
from datetime import timedelta
from datetime import datetime

def get_range_of_historical_quotes(symbol, startDate, endDate = datetime.today()):
    """
    Get historical prices for the given ticker symbol.
    startDate and endDate is date type
    Returns a nested list.
    """
    # URL should look like: http://real-chart.finance.yahoo.com/table.csv?s=AAPL&a=11&b=12&c=1980&d=06&e=11&f=2014&g=d&ignore=.csv
    url = 'http://real-chart.finance.yahoo.com/table.csv?s=%s&' % symbol + \
    'a=%s&' % str(int(startDate.month) -1 ) + \
    'b=%s&' % str(int(startDate.day)) + \
    'c=%s&' % str(int(startDate.year)) + \
    'd=%s&' % str(int(endDate.month) - 1 ) + \
    'e=%s&' % str(int(endDate.day)) + \
    'f=%s&' % str(int(endDate.year)) + \
    'g=d&ignore=.csv'
    
    historicalList = [] 
    try:
        response = urllib2.urlopen(url)
    except:
        print 'urlopen failed.'
        return []
    
    if (response.msg != 'OK'):
        print 'URL error: %s' % response.msg
        return []
    
    rawDataBlock = response.read().splitlines()
        
    for dataLine in rawDataBlock[1:]:
        try:
            data = {}
            rawData = dataLine.strip().strip('"').split(',')

            data[TRADE_DATE_STR]                  = datetime.strptime(rawData[0],'%Y-%m-%d').date()
            data[OPEN_STR]                        = float(rawData[1])
            data[DAY_HIGH_STR]                    = float(rawData[2])
            data[DAY_LOW_STR]                     = float(rawData[3])
            data[LAST_TRADE_PRICE_ONLY_STR]       = float(rawData[4])
            data[VOLUME_STR]                      = float(rawData[5])
            data[ADJUSTED_CLOSE_STR]              = float(rawData[6])
            data[SYMBOL_STR]                      = symbol

            historicalList.insert(0,data)
        except:
            print 'get_range_of_historical_quotes() error. Symbol: %s' % symbol
            return []

    return historicalList

def get_number_of_historical_quotes(symbol, numDays, endDate=datetime.today()):
    """
    Get historical prices for the given ticker symbol.
    endDate is date type
    Returns a nested list.
    """
    
    historicalList = []

    #Figure out how many days to request. Add extra days to account for weekends, holidays, etc)
    #try:
    deltaDate = timedelta(days = int(numDays * 1.5 + 5))
    historicalList = get_range_of_historical_quotes(symbol, endDate - deltaDate, endDate)[-numDays:]

    #except:
    #   print 'get_number_of_historic_quotes() error. Symbol:',symbol
    #   return []
    
    return historicalList

if __name__=='__main__':
    for day in get_number_of_historical_quotes('YHOO',5):
        print day