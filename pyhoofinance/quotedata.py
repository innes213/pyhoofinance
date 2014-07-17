#!/usr/bin/env python
#
#  pyhoofinance - quotedata.py
#
#  Copyright (c) 2014, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

from datetime import datetime
import urllib2
from defs import *
    
def _query_yahoo(symbolList,tokenStr):
    """
    Returns raw data from Yahoo Finance
    """
    if tokenStr == '':
        return []
    
    # Retrieve block of quotes in the form of a CSV file
    url = 'http://finance.yahoo.com/d/quotes.csv?s='+'+'.join(symbolList)+'&f='+tokenStr
        
    # For each line of the CSV, extract quote data and store
    try:
        response = urllib2.urlopen(url)
    except:
        print('urlopen failed. Check network connection')
        return None
    return response.read().splitlines()  

def _get_quote_block(symbolList,quoteDescriptionList, tokenStr, tokenCommaList):
    """
    Queries Yahoo for quotes. List of symbols must be no
    greater than 200 per Yahoo limits
     
    Returns list of dictionaries
    """   
    columnList = []
    for token in tokenCommaList:
        dataColumn = []
        for item in _query_yahoo(symbolList,token):
            dataColumn.append(''.join(item.split(',')))
        columnList.append(dataColumn)
    
    # Transpose
    commaData = [list(row) for row in zip(*columnList)]
    
    # tokenStr should always contain at least the SYMBOL_STR token, so check isn't really necessary
    rawDataBlock = _query_yahoo(symbolList,tokenStr)
    
    # For each row, break into individual values and assign to dictionary
    quoteBlock = [] 
    count = 0
    
    for dataLine in rawDataBlock:
        rawdata = dataLine.strip().strip('"').split(',')         
       
        # Unite comma data in corresponding row
        if commaData:
            rawdata.extend(commaData[count])
        count += 1
        
        # Store data and descriptions in a dictionary
        data = {}
        try:
            for i in range(len(quoteDescriptionList)):
                data[quoteDescriptionList[i]] = rawdata[i].strip('"')
        
        except:
            print 'Error parsing quote:' + str(rawdata)
              
        quoteBlock.append(data)

    return quoteBlock

def _format_quote_data(quotes):
    """
    Formats quote data from all strings to floats, dates, and strings as appropriate
    """
        
    formattedQuotes = quotes
    
    #define multiplier characters. Ex: 2.7K = 2,700
    multipliers = {'%' : 1, 'K' : 1000, 'M' : 1000000, 'B': 1000000000, 'T': 1000000000000} #Use 1 instead of .01 for percent as data labels indicate percentage
    
    try:
        # Create a list of items that should be floating-point
        floatItemList = []
        for desc in QUOTE_DATA_FLOAT_LIST:
            if desc in quotes[0]:
                floatItemList.append(desc)       
    
        # Create a list of items that should be dates 
        dateItemList = []
        for desc in QUOTE_DATA_DATE_LIST:
            if desc in quotes[0]:
                dateItemList.append(desc) 
    
        # Go through quotes and convert items per each list 
        for quote in formattedQuotes:
            for item in floatItemList:
                # if Yahoo returned N/A, replace value with None
                if quote[item].find('N/A') != -1:
                    quote[item] = None
                else:
                    if quote[item][-1:] not in multipliers:
                        quote[item] = float(quote[item])
                    else:
                        quote[item] = float(quote[item][:-1]) * multipliers[quote[item][-1:]]           
            
            for item in dateItemList:
                if quote[item].find('N/A') != -1:
                    quote[item] = None
                else:
                    quote[item] = datetime.strptime(quote[item],'%m/%d/%Y').date()
    except:
        print 'Error formatting quotes. Symbol',quote[SYMBOL_STR],'Item:',item
        
    return formattedQuotes
                   
def get_quotes(symbols, quoteData = STANDARDQUOTE, raw = False):
    """
    Returns requested quote data (quoteData) for every valid symbol in the list 'symbols'
    If raw is true, the raw text values are returned, otherwise values are properly
    typecast.
    """
    blockSize=200 # Maximum number of quotes per request allowed by Yahoo finance API
    quoteList = []
    
    # Validate quote request desc and look up corresponding key     
    quoteDescriptionList = quoteData
    tokenList = []
    tokenCommaList = []
    
    # Make sure the symbol is requested
    if SYMBOL_STR not in quoteDescriptionList:
        quoteDescriptionList.append(SYMBOL_STR)
            
    # Move request items that may return data with commas to end of list
    for desc in quoteDescriptionList:
        if desc in QUOTE_DATA_WITH_COMMAS_LIST:
            quoteDescriptionList.remove(desc)
            quoteDescriptionList.append(desc)
        
    # Create token lists for query        
    for desc in quoteDescriptionList:
        key = YAHOO_FINANCE_KEYS_DICT[desc]
        if (key):
            if desc not in QUOTE_DATA_WITH_COMMAS_LIST:
                tokenList.append(key)
            else: 
                tokenCommaList.append(key)
        else:
            # Toss out bad requests
            quoteDescriptionList.remove(desc)
            print('{0} is unsupported or an invalid quote request. Removing from request.'.format(desc))
    
    # if there are no valid data requests, return now
    if (quoteDescriptionList == []):
        return []
    
    # Calulate the number of blocks and the remainder symbols
    numFullBlocks, lenPartialBlock = divmod(len(symbols), blockSize)
    
    # Retreive quotes from Yahoo, up to 200 at a time
    for i in range(numFullBlocks):
        symbolBlock = symbols[i * blockSize:(i + 1) * blockSize]
        quoteList.extend(_get_quote_block(symbolBlock,quoteDescriptionList, ''.join(tokenList), tokenCommaList))
    
    # Add the last block of quotes (< 200)
    quoteList.extend(_get_quote_block(symbols[-lenPartialBlock:],quoteDescriptionList, ''.join(tokenList), tokenCommaList))

    # Type date strings and dates and numeric strings as floats
    if (quoteList != []) and (not raw):
        quoteList = _format_quote_data(quoteList)
    return quoteList
   
   
if (__name__ == '__main__'):
    
    try:
        print(get_quotes(['YHOO']))
        print(get_quotes(['YHOO'],MINIQUOTE,True))
    except:
        exit(1)
    """
    try:
        print(get_quotes(['YHOO'],[SYMBOL_STR,FLOAT_SHARES_STR,SHARES_OUTSTANDING_STR,NAME_STR]))
        print(get_quotes(['YHOO','GOOGL','AAPL'],[SYMBOL_STR,FLOAT_SHARES_STR,SHARES_OUTSTANDING_STR,NAME_STR]))
    except:
        exit(1)
    """