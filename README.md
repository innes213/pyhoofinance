# pyhoofinance

pyhoofinance is a set of tools to query Yahoo Finance's
API. These tools are designed for applications which need 
to grab large numbers of quotes. Additionally, data, by 
default, is properly typecast for easy analysis. It is 
designed for flexibility and to minimize server queries.

## Installation

```
pip install pyhoofinance
```

## Example Usage

```python
#!/usr/bin/env python

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
```

**Results:**

```
YAHOO standard quote, typed data
[{'previous_close': 35.43, '1_yr_target_price': 41.23, 'day_low': 35.45, 'error_indication': 'N/A', 'name': 'Yahoo! Inc.', '52_week_high': 41.72, 'average_daily_volume': 19843500.0, 'pe_ratio': 29.55, 'symbol': 'YHOO', 'earnings_per_share': 1.199, 'volume': 18688504.0, 'trailing_dividend_per_share': 0.0, 'market_capitalization': 35943000000.0, 'last_trade_date': datetime.date(2014, 7, 14), 'last_trade_price_only': 35.7, 'day_high': 35.95, 'dividend_yield': None, 'open': 35.74, '52_week_low': 26.73, 'change': 0.27}]
```

```
Multiple Miniquotes, raw strings:
{'day_low': '35.45', 'error_indication': 'N/A', 'name': 'Yahoo! Inc.', 'average_daily_volume': '19843500', 'symbol': 'YHOO', 'volume': '18688504', 'last_trade_price_only': '35.70', 'day_high': '35.95', 'open': '35.74', 'change': '+0.27'}
{'day_low': '586.693', 'error_indication': 'N/A', 'name': 'Google Inc.', 'average_daily_volume': '2075450', 'symbol': 'GOOGL', 'volume': '1954612', 'last_trade_price_only': '594.26', 'day_high': '594.86', 'open': '590.70', 'change': '+7.61'}
{'day_low': '95.65', 'error_indication': 'N/A', 'name': 'Apple Inc.', 'average_daily_volume': '65240800', 'symbol': 'AAPL', 'volume': '42810156', 'last_trade_price_only': '96.45', 'day_high': '96.89', 'open': '95.86', 'change': '+1.23'}
{'day_low': '42.04', 'error_indication': 'N/A', 'name': 'Microsoft Corpora', 'average_daily_volume': '27786900', 'symbol': 'MSFT', 'volume': '21882944', 'last_trade_price_only': '42.14', 'day_high': '42.45', 'open': '42.22', 'change': '+0.05'}
{'day_low': '197.44', 'error_indication': 'N/A', 'name': 'SPDR S&P 500', 'average_daily_volume': '84223000', 'symbol': 'SPY', 'volume': '58657920', 'last_trade_price_only': '197.60', 'day_high': '197.86', 'open': '197.61', 'change': '+0.99'}
{'day_low': '125.45', 'error_indication': 'N/A', 'name': 'SPDR Gold Trust', 'average_daily_volume': '6160990', 'symbol': 'GLD', 'volume': '11469917', 'last_trade_price_only': '125.72', 'day_high': '126.10', 'open': '125.50', 'change': '-3.06'}
```

```
YHOO data for the 5 most recent trading days
{'day_low': 34.28, 'symbol': 'YHOO', 'trade_date': datetime.date(2014, 7, 8), 'volume': 23096900.0, 'last_trade_price_only': 34.53, 'day_high': 35.66, 'open': 35.64, 'adjusted_close': 34.53}
{'day_low': 34.68, 'symbol': 'YHOO', 'trade_date': datetime.date(2014, 7, 9), 'volume': 12626900.0, 'last_trade_price_only': 34.85, 'day_high': 35.07, 'open': 34.68, 'adjusted_close': 34.85}
{'day_low': 34.1, 'symbol': 'YHOO', 'trade_date': datetime.date(2014, 7, 10), 'volume': 18064800.0, 'last_trade_price_only': 34.93, 'day_high': 34.97, 'open': 34.33, 'adjusted_close': 34.93}
{'day_low': 34.78, 'symbol': 'YHOO', 'trade_date': datetime.date(2014, 7, 11), 'volume': 18303700.0, 'last_trade_price_only': 35.43, 'day_high': 35.56, 'open': 34.95, 'adjusted_close': 35.43}
{'day_low': 35.45, 'symbol': 'YHOO', 'trade_date': datetime.date(2014, 7, 14), 'volume': 18680500.0, 'last_trade_price_only': 35.7, 'day_high': 35.95, 'open': 35.8, 'adjusted_close': 35.7}
```

## Getting Current Stock Data

### Getting Data for Multiple Symbols

To get current stock data for multiple symbols, use the method `get_quotes()` in quotedata.py. Using this method for multiple symbols is up to 200 times faster than querying for each symbol individually.

```python
get_quotes(symbolList,dataList,raw)
```

`symbolList`: List of symbols. For example `[‘YHOO','GOOGL’]`.
`dataList`: List of requested data (like `[VOLUME_STR, LAST_TRADE_PRICE_ONLY_STR]` or some predefined list like `MINIQUOTE`. Default is `STANDARDQUOTE`. 
`raw`: Boolean declaring whether to return raw or typed data. Default is `false` (typed data).

### Getting Data for Single Symbol

To query for data for a single symbol, the method `get_quote()` in quotedata.py
can be used although it simply creates a single item list and calls `get_quotes`.

```python
get_quote(symbol,dataList,raw)
```

`symbol`: Symbol string. For example `’YHOO’`. 
`dataList`: List of requested data (like `[VOLUME_STR, LAST_TRADE_PRICE_ONLY_STR]` or some predefined list like `MINIQUOTE`. Default is `STANDARDQUOTE`.
`raw`: Boolean declaring whether to return raw or typed data. Default is `false` (typed data).

## Getting Historic Data

Yahoo's historic stock data API is a little different. There is no way to grab
data for more than one symbol at a time. pyhoofinance does offer two options 
for retrieving data which are described in this section.

Note: there is currently no option to return data as raw strings.

### Stock Data For Range of Days

To get data for a range of days from a start date to an enddate (inclusive), use
`get_range_of_historical_prices()`.

```python                                  
get_range_of_historical_quotes(symbol, startDate, endDate)
```

`symbol`: Symbol string. For example `’YHOO’`.
`startDate`: First date to grab. Date type.
`endDate`: Last date (date type) to grab. Default is `datetime.today()`.

### Stock Data For Number of Days

This is an incredibly useful building block for calculating averages. In order
to get historic stock data for a number of days, use 
`get_number_of_historic_quotes()`.

```python
get_number_of_historical_quotes(symbol, numDays, endDate)
```

`symbol`: Symbol string. For example `’YHOO’`.
`numDays`: Integer number of days of data to retrieve.
`endDate`: Last date (date type) to grab. Default is `datetime.today()`.

