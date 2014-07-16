#!/usr/bin/env python

#  Copyright (c) 2014, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com

"""
This module queries the Yahoo Finance API
with every allowable data key, one at a time
and prints the raw output
"""
import urllib2
from pyhoofinance import *
    
def get_quote(symbol, dataKey):
    """
    Queries Yahoo for quotes. List of symbols must be no
    greater than 200 per Yahoo limits
     
    Returns list of dictionaries
    """

    # Retrieve block of quotes in the form of a CSV file
    url = 'http://finance.yahoo.com/d/quotes.csv?s='+symbol+'&f='+dataKey
        
    # For each line of the CSV, extract quote data and store
    try:
        rawData = urllib2.urlopen(url)
    except:
        print('urlopen failed')
        return []

    if (rawData.msg != 'OK'):
        print ('URL request failed: {}'.format(rawData.msg))
        return []
    rawData = rawData.read().splitlines()

    return rawData

if __name__=='__main__':
    
    knownTokens = {}
    for key in YAHOO_FINANCE_KEYS_DICT:
        knownTokens[YAHOO_FINANCE_KEYS_DICT[key]] = key;
    
    print('{0:>45} : {1:5} --> {2}'.format('Data Description','Token', 'Result'))
                    
    for letter in range(ord('A'),ord('Z') +1):
        token = chr(letter)
        if token not in knownTokens:
            desc = 'UNKNOWN'
        else: 
            desc = knownTokens[token]
        result = get_quote('AAPL',token)
        print('{0:>45} : {1:5} --> {2}'.format(desc,token, result))
        for num in range(0,10):
            token = chr(letter) + str(num)
            if token not in knownTokens:
                desc = 'UNKNOWN'
            else:
                desc = knownTokens[token]                
            result = get_quote('AAPL',token)
            print('{0:>45} : {1:5} --> {2}'.format(desc, token, result))
            