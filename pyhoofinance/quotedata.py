#!/usr/bin/env python
#
#  pyhoofinance - quote_data.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

from datetime import datetime
import urllib2
from defs import *
    
def _query_yahoo(symbol_list, token_str):
    """
    Hits Yahoo Finance API endpoint for quote data for single or multiple symbols
    @params:
        symbol_list (list( List of symbol strings
        token_str (string) tokens corresponding to data key
    Returns list of quote data
    """
    if token_str == '':
        return []
    
    # Retrieve block of quotes in the form of a CSV file
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % ('+'.join(symbol_list), token_str)
        
    # For each line of the CSV, extract quote data and store
    try:
        response = urllib2.urlopen(url)
    except:
        print 'urlopen failed. Check network connection'
        return None
    return response.read().splitlines()  

def _get_quote_block(symbol_list, quote_description_list, token_str, token_comma_list):
    """
    Queries Yahoo for quotes. List of symbols must be no
    greater than 1000 per Yahoo limits
    Returns list of dictionaries
    Args:
        symbol_list (list) List of ticker symbol strings
        quote_description_list (list) list of data description strings to retrieve
        token_str (string) string of tokens corresponding to data descriptions
        token_comma_list (list) List of strings corresponding to data that may return values with commas
    """
       
    column_list = []
    for token in token_comma_list:
        dataColumn = []
        for item in _query_yahoo(symbol_list,token):
            dataColumn.append(''.join(item.split(',')))
        column_list.append(dataColumn)
    
    # Transpose
    comma_data = [list(row) for row in zip(*column_list)]

    raw_data_block = _query_yahoo(symbol_list, token_str)
    
    # For each row, break into individual values and assign to dictionary
    quote_block = [] 
    count = 0
    
    for dataLine in raw_data_block:
        rawdata = dataLine.strip().strip('"').split(',')         
       
        # Unite comma data in corresponding row
        if comma_data:
            rawdata.extend(comma_data[count])
        count += 1
        
        # Store data and descriptions in a dictionary
        data = {}
        try:
            for i in range(len(quote_description_list)):
                data[quote_description_list[i]] = rawdata[i].strip('"')
            if data[NAME_STR].upper().find('N/A') != -1:
                data[ERROR_INDICATION_STR] = 'Bad Symbol'
            else:
                data[ERROR_INDICATION_STR] = 'N/A'
        except:
            print 'Error parsing quote: %s' % str(rawdata)

        quote_block.append(data)

    return quote_block

def _format_quote_data(quotes):
    """
    Formats quote data from all strings to floats, dates, and strings as appropriate
    """
        
    formatted_quotes = quotes
    
    #define multiplier characters. Ex: 2.7K = 2,700
    multipliers = {'%' : 1, 'K' : 1000, 'M' : 1000000, 'B': 1000000000, 'T': 1000000000000} #Use 1 instead of .01 for percent as data labels indicate percentage
    
    try:
        # Create a list of items that should be floating-point
        float_item_list = []
        for desc in QUOTE_DATA_FLOAT_LIST:
            if desc in quotes[0]:
                float_item_list.append(desc)       
    
        # Create a list of items that should be dates 
        date_item_list = []
        for desc in QUOTE_DATA_DATE_LIST:
            if desc in quotes[0]:
                date_item_list.append(desc) 
    
        # Go through quotes and convert items per each list 
        for quote in formatted_quotes:
            for item in float_item_list:
                # if Yahoo returned N/A, replace value with None
                if quote[item].find('N/A') != -1:
                    quote[item] = None
                else:
                    if quote[item][-1:] not in multipliers:
                        quote[item] = float(quote[item])
                    else:
                        quote[item] = float(quote[item][:-1]) * multipliers[quote[item][-1:]]           
            
            for item in date_item_list:
                if quote[item].find('N/A') != -1:
                    quote[item] = None
                else:
                    quote[item] = datetime.strptime(quote[item],'%m/%d/%Y').date()
    except:
        print 'Error formatting quotes. Symbol',quote[SYMBOL_STR],'Item:',item
        
    return formatted_quotes
                   
def get_quotes(symbols, quote_data=STANDARDQUOTE, raw=False):
    """
    Returns requested quote data (quote_data) for every valid symbol in the list 'symbols'
    The company name is always returned with the quote data, as is the symbol. If the list
    of symbols is larger than the max allowed by Yahoo, multiple calls are made until all
    all data for all symbols has been retreived.
    Args:
        symbols {list} List of strings for ticker symbols
        quote_data (Optional[list]) list of requested data (descriptions)
        raw (Optional[Boolean]) whether or not to type the data
    """
    
    block_size = 1625 # Maximum number of quotes per request allowed by Yahoo finance API
    quote_list = []
    
    # Validate quote request desc and look up corresponding key     
    quote_description_list = quote_data
    token_list = []
    token_comma_list = []
    
    # Make sure the symbol is requested
    if SYMBOL_STR not in quote_description_list:
        quote_description_list.append(SYMBOL_STR)
    
    # Make sure the name is requested
    if NAME_STR not in quote_description_list:
        quote_description_list.append(NAME_STR)
            
    # Move request items that may return data with commas to end of list
    for desc in quote_description_list:
        if desc in QUOTE_DATA_WITH_COMMAS_LIST:
            quote_description_list.remove(desc)
            quote_description_list.append(desc)
        
    # Create token lists for query        
    for desc in quote_description_list:
        key = YAHOO_FINANCE_KEYS_DICT[desc]
        if key:
            if desc not in QUOTE_DATA_WITH_COMMAS_LIST:
                token_list.append(key)
            else: 
                token_comma_list.append(key)
        else:
            # Toss out bad requests
            quote_description_list.remove(desc)

            print '%s is unsupported or an invalid quote request. Removing from request.' % desc
    
    # if there are no valid data requests, return now
    if (quote_description_list == []):
        return []
    
    # Calulate the number of blocks and the remainder symbols
    number_of_blocks, partial_block_length = divmod(len(symbols), block_size)
    
    # Retreive quotes from Yahoo, up to block_size at a time
    for i in range(number_of_blocks):
        symbol_block = symbols[i * block_size:(i + 1) * block_size]
        quote_list.extend(_get_quote_block(symbol_block,quote_description_list, ''.join(token_list), token_comma_list))
    
    # Add the last block of quotes (< block_size)
    quote_list.extend(_get_quote_block(symbols[-partial_block_length:],quote_description_list, ''.join(token_list), token_comma_list))

    # Type date strings and dates and numeric strings as floats
    if quote_list != [] and not raw:
        quote_list = _format_quote_data(quote_list)
    return quote_list

def get_quote(symbol, quote_data = STANDARDQUOTE, raw = False):
    """
    Returns requested quote data (quote_data) for the symbol 'symbol'
    The company name is always returned with the quote data, as is the symbol.
    Args:
        symbols (string) List of strings for ticker symbols
        quote_data (Optional[list]) list of requested data (descriptions)
        raw (Optional[Boolean]) whether or not to type the data
    """
    symbol_list = [symbol]
    return get_quotes(symbol_list,quote_data, raw)[0]

