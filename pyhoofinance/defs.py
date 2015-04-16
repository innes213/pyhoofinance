#!/usr/bin/env python
#
#  pyhoofinance - defs.py
#
#  Copyright (c) 2014-2015, Rob Innes Hislop
#  email:robinneshislop__AT__gmail.com
#
# This library is distributed under the terms of the 
# GNU General Public License (or the Lesser GPL)
# version 3.

"""
Not currently used by pyhoofinance, may be moved to parent module
MEGACAPFLOOR  = 100000000000
LARGECAPFLOOR = 10000000000
MIDCAPFLOOR   = 2000000000
SMALLCAPFLOOR = 300000000
MICROCAPFLOOR = 50000000
"""

ASK_STR                                           =    'ask'
AVERAGE_DAILY_VOLUME_STR                          =    'average_daily_volume'
ASK_SIZE_STR                                      =    'ask_size'
BID_STR                                           =    'bid'
ASK_RT_STR                                        =    'ask_rt'
BID_RT_STR                                        =    'bid_rt'
BOOK_VALUE_STR                                    =    'book_value'
BID_SIZE_STR                                      =    'bid_size'
CHANGE_AND_PERCENT_CHANGE_STR                     =    'change_and_percent_change'
CHANGE_STR                                        =    'change'
COMMISSION_STR                                    =    'commission'
CURRENCY_STR                                      =    'currency'
CHANGE_RT_STR                                     =    'change_rt'
AFTER_HOURS_CHANGE_RT_STR                         =    'after_hours_change_rt'
TRAILING_DIVIDEND_PER_SHARE_STR                   =    'trailing_dividend_per_share'
LAST_TRADE_DATE_STR                               =    'last_trade_date'
TRADE_DATE_STR                                    =    'trade_date'
EARNINGS_PER_SHARE_STR                            =    'earnings_per_share'
ERROR_INDICATION_STR                              =    'error_indication'
EPS_ESTIMATE_CURRENT_YEAR_STR                     =    'eps_estimate_current_year'
EPS_ESTIMATE_NEXT_YEAR_STR                        =    'eps_estimate_next_year'
EPS_ESTIMATE_NEXT_QUARTER_STR                     =    'eps_estimate_next_quarter'
FLOAT_SHARES_STR                                  =    'float_shares'              
DAY_LOW_STR                                       =    'day_low'
DAY_HIGH_STR                                      =    'day_high'
FIFTYTWO_WEEK_LOW_STR                             =    '52_week_low'
FIFTYTWO_WEEK_HIGH_STR                            =    '52_week_high'
HOLDINGS_GAIN_PERCENT_STR                         =    'holdings_gain_percent'
ANNUALIZED_GAIN_STR                               =    'annualized_gain'
HOLDINGS_GAIN_STR                                 =    'holdings_gain'
HOLDINGS_GAIN_PERCENT_RT_STR                      =    'holdings_gain_percent_rt'
HOLDINGS_GAIN_RT_STR                              =    'holdings_gain_rt'
MORE_INFO_STR                                     =    'more_info'
ORDER_BOOK_RT_STR                                 =    'order_book_rt'
MARKET_CAPITALIZATION_STR                         =    'market_capitalization'
SHARES_OUTSTANDING_STR                            =    'shares_outstanding'
MARKET_CAP_RT_STR                                 =    'market_cap_rt'
EBITDA_STR                                        =    'ebitda'
CHANGE_FROM_52_WEEK_LOW_STR                       =    'change_from_52-week_low'
PERCENT_CHANGE_FROM_52_WEEK_LOW_STR               =    'percent_change_From_52-week_low'
LAST_TRADE_RT_WITH_TIME_STR                       =    'last_trade_rt_with_time'
CHANGE_PERCENT_RT_STR                             =    'change_percent_rt'
LAST_TRADE_SIZE_STR                               =    'last_trade_size'
CHANGE_FROM_52_WEEK_HIGH_STR                      =    'change_from_52-week_high'
PERCEBT_CHANGE_FROM_52_WEEK_HIGH_STR              =    'percebt_change_from_52-week_high'
LAST_TRADE_RT_STR                                 =    'last_trade_rt'
LAST_TRADE_PRICE_ONLY_STR                         =    'last_trade_price_only'
HIGH_LIMIT_STR                                    =    'high_limit'
LOW_LIMIT_STR                                     =    'low_limit'
DAY_RANGE_STR                                     =    'day_range'
DAY_RANGE_RT_STR                                  =    'day_range_rt'
FIFTY_DAY_MOVING_AVERAGE_STR                      =    '50-day_moving_average'
TWOHUNDRED_DAY_MOVING_AVERAGE_STR                 =    '200-day_moving_average'
CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR            =    'change_from_200-day_moving_average'
PERCENT_CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR    =    'percent_change_from_200-day_moving_average'
CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR             =    'change_from_50-day_moving_average'
PERCENT_CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR     =    'percent_change_rrom_50-day_moving_average'
NAME_STR                                          =    'name'
NOTES_STR                                         =    'notes'
OPEN_STR                                          =    'open'
PREVIOUS_CLOSE_STR                                =    'previous_close'
PRICE_PAID_STR                                    =    'price_paid'
CHANGE_IN_PERCENT_STR                             =    'change_in_percent'
PRICE_TO_SALES_STR                                =    'price_to_sales'
PRICE_TO_BOOK_STR                                 =    'price_to_book'
EX_DIVIDEND_DATE_STR                              =    'ex-dividend_date'
PE_RATIO_STR                                      =    'pe_ratio'
CHART_OVERLAYS_LINKS_STR                          =    'chart_overlays_links'
CHART_LOWER_INDICATORS_LINKS_STR                  =    'chart_lower_indicators_links'
DIVIDEND_PAY_DATE_STR                             =    'dividend_pay_date'
PE_RATIO_RT_STR                                   =    'pe_ratio_rt'
PEG_RATIO_STR                                     =    'peg_ratio'
PRICE_TO_EPS_ESTIMATE_CURRENT_YEAR_STR            =    'price_to_eps_estimate_current_year'
PRICE_TO_EPS_ESTIMATE_NEXT_YEAR_STR               =    'price_to_eps_estimate_next_year'
SYMBOL_STR                                        =    'symbol'
SHARES_OWNED_STR                                  =    'shares_owned'
SHORT_RATIO_STR                                   =    'short_ratio'
REVENUE_STR                                       =    'revenue'
LAST_TRADE_TIME_STR                               =    'last_trade_time'
TRADE_LINKS_STR                                   =    'trade_links'
TICKER_TREND_STR                                  =    'ticker_trend'
ONE_YR_TARGET_PRICE_STR                           =    '1_yr_target_price'
VOLUME_STR                                        =    'volume'
HOLDINGS_VALUE_STR                                =    'holdings_value'
HOLDINGS_VALUE_RT_STR                             =    'holdings_value_rt'
FIFTYTWO_WEEK_RANGE_STR                           =    '52-week_range'
DAY_VALUE_CHANGE_STR                              =    'day_value_change'
DAY_VALUE_CHANGE_RT_STR                           =    'day_value_change_rt'
STOCK_EXCHANGE_STR                                =    'stock_exchange'
DIVIDEND_YIELD_STR                                =    'dividend_yield'
ADJUSTED_CLOSE_STR                                =    'adjusted_close'

#Handy pre-defined lists of quote data elements to pass to GetQuotes
#Note that Name is always last as the result may contain a comma

MINIQUOTE         = [SYMBOL_STR, \
                     OPEN_STR, \
                     DAY_HIGH_STR, \
                     DAY_LOW_STR, \
                     CHANGE_STR, \
                     LAST_TRADE_PRICE_ONLY_STR, \
                     VOLUME_STR, \
                     AVERAGE_DAILY_VOLUME_STR, \
                     NAME_STR]

STANDARDQUOTE     = [SYMBOL_STR, \
                     LAST_TRADE_PRICE_ONLY_STR, \
                     OPEN_STR, \
                     AVERAGE_DAILY_VOLUME_STR, \
                     VOLUME_STR, \
                     DAY_HIGH_STR, \
                     DAY_LOW_STR, \
                     CHANGE_STR, \
                     LAST_TRADE_DATE_STR, \
                     PREVIOUS_CLOSE_STR, \
                     MARKET_CAPITALIZATION_STR, \
                     PE_RATIO_STR, \
                     ONE_YR_TARGET_PRICE_STR, \
                     TRAILING_DIVIDEND_PER_SHARE_STR, \
                     DIVIDEND_YIELD_STR, \
                     EARNINGS_PER_SHARE_STR, \
                     FIFTYTWO_WEEK_LOW_STR, \
                     FIFTYTWO_WEEK_HIGH_STR, \
                     NAME_STR]

EXTENDEDQUOTE = [SYMBOL_STR, \
                 LAST_TRADE_PRICE_ONLY_STR, \
                 OPEN_STR, \
                 AVERAGE_DAILY_VOLUME_STR, \
                 VOLUME_STR, \
                 DAY_HIGH_STR, \
                 DAY_LOW_STR, \
                 CHANGE_STR, \
                 LAST_TRADE_DATE_STR, \
                 PREVIOUS_CLOSE_STR, \
                 MARKET_CAPITALIZATION_STR, \
                 PE_RATIO_STR, \
                 EARNINGS_PER_SHARE_STR, \
                 EPS_ESTIMATE_NEXT_YEAR_STR, \
                 EPS_ESTIMATE_NEXT_QUARTER_STR, \
                 EBITDA_STR, \
                 TWOHUNDRED_DAY_MOVING_AVERAGE_STR, \
                 PRICE_TO_SALES_STR, \
                 PRICE_TO_BOOK_STR, \
                 EX_DIVIDEND_DATE_STR, \
                 DIVIDEND_PAY_DATE_STR, \
                 ONE_YR_TARGET_PRICE_STR, \
                 DIVIDEND_YIELD_STR, \
                 PEG_RATIO_STR, \
                 TRAILING_DIVIDEND_PER_SHARE_STR, \
                 STOCK_EXCHANGE_STR, \
                 NAME_STR]

"""
Internal global constants
"""

YAHOO_FINANCE_KEYS_DICT =  {ASK_STR                                         : 'a'  , \
                            AVERAGE_DAILY_VOLUME_STR                        : 'a2' , \
                            ASK_SIZE_STR                                    : 'a5' , \
                            BID_STR                                         : 'b'  , \
                            BOOK_VALUE_STR                                  : 'b4' , \
                            BID_SIZE_STR                                    : 'b6' , \
                            CHANGE_AND_PERCENT_CHANGE_STR                   : 'c'  , \
                            CHANGE_STR                                      : 'c1' , \
                            CURRENCY_STR                                    : 'c4' , \
                            TRAILING_DIVIDEND_PER_SHARE_STR                 : 'd' , \
                            LAST_TRADE_DATE_STR                             : 'd1' , \
                            EARNINGS_PER_SHARE_STR                          : 'e' , \
                            EPS_ESTIMATE_CURRENT_YEAR_STR                   : 'e7' , \
                            EPS_ESTIMATE_NEXT_YEAR_STR                      : 'e8' , \
                            EPS_ESTIMATE_NEXT_QUARTER_STR                   : 'e9' , \
                            FLOAT_SHARES_STR                                : 'f6' , \
                            DAY_LOW_STR                                     : 'g' , \
                            DAY_HIGH_STR                                    : 'h' , \
                            FIFTYTWO_WEEK_LOW_STR                           : 'j' , \
                            FIFTYTWO_WEEK_HIGH_STR                          : 'k' , \
                            MARKET_CAPITALIZATION_STR                       : 'j1' , \
                            SHARES_OUTSTANDING_STR                          : 'j2' , \
                            EBITDA_STR                                      : 'j4' , \
                            CHANGE_FROM_52_WEEK_LOW_STR                     : 'j5' , \
                            PERCENT_CHANGE_FROM_52_WEEK_LOW_STR             : 'j6' , \
                            LAST_TRADE_SIZE_STR                             : 'k3' , \
                            CHANGE_FROM_52_WEEK_HIGH_STR                    : 'k4' , \
                            PERCEBT_CHANGE_FROM_52_WEEK_HIGH_STR            : 'k5' , \
                            LAST_TRADE_RT_STR                               : 'l' , \
                            LAST_TRADE_PRICE_ONLY_STR                       : 'l1' , \
                            DAY_RANGE_STR                                   : 'm' , \
                            FIFTY_DAY_MOVING_AVERAGE_STR                    : 'm3' , \
                            TWOHUNDRED_DAY_MOVING_AVERAGE_STR               : 'm4' , \
                            CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR          : 'm5' , \
                            PERCENT_CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR  : 'm6' , \
                            CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR           : 'm7' , \
                            PERCENT_CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR   : 'm8' , \
                            NAME_STR                                        : 'n' , \
                            OPEN_STR                                        : 'o' , \
                            PREVIOUS_CLOSE_STR                              : 'p' , \
                            CHANGE_IN_PERCENT_STR                           : 'p2' , \
                            PRICE_TO_SALES_STR                              : 'p5' , \
                            PRICE_TO_BOOK_STR                               : 'p6' , \
                            EX_DIVIDEND_DATE_STR                            : 'q' , \
                            PE_RATIO_STR                                    : 'r' , \
                            DIVIDEND_PAY_DATE_STR                           : 'r1' , \
                            PEG_RATIO_STR                                   : 'r5' , \
                            PRICE_TO_EPS_ESTIMATE_CURRENT_YEAR_STR          : 'r6' , \
                            PRICE_TO_EPS_ESTIMATE_NEXT_YEAR_STR             : 'r7' , \
                            SYMBOL_STR                                      : 's' , \
                            REVENUE_STR                                     : 's6' , \
                            SHORT_RATIO_STR                                 : 's7' , \
                            LAST_TRADE_TIME_STR                             : 't1' , \
                            ONE_YR_TARGET_PRICE_STR                         : 't8' , \
                            VOLUME_STR                                      : 'v' , \
                            FIFTYTWO_WEEK_RANGE_STR                         : 'w' , \
                            STOCK_EXCHANGE_STR                              : 'x' , \
                            DIVIDEND_YIELD_STR                              : 'y'   }

QUOTE_DATA_WITH_COMMAS_LIST = [NAME_STR]

#THIS SECTION LISTS QUOTE DATA BY TYPE FOR FORMAT CONVERSION
QUOTE_DATA_DATE_LIST = [
LAST_TRADE_DATE_STR, \
TRADE_DATE_STR \
#EX_DIVIDEND_DATE_STR, \ TODO: Handle date strings in this format
#DIVIDEND_PAY_DATE_STR \
]

#TODO: clean out unused values
QUOTE_DATA_FLOAT_LIST = [
ASK_STR, \
AVERAGE_DAILY_VOLUME_STR, \
ASK_SIZE_STR, \
BID_STR, \
ASK_RT_STR, \
BID_RT_STR, \
BOOK_VALUE_STR, \
BID_SIZE_STR, \
CHANGE_STR, \
COMMISSION_STR, \
CHANGE_RT_STR, \
AFTER_HOURS_CHANGE_RT_STR, \
TRAILING_DIVIDEND_PER_SHARE_STR, \
EARNINGS_PER_SHARE_STR, \
EPS_ESTIMATE_CURRENT_YEAR_STR, \
EPS_ESTIMATE_NEXT_YEAR_STR, \
EPS_ESTIMATE_NEXT_QUARTER_STR, \
FLOAT_SHARES_STR, \
DAY_LOW_STR, \
DAY_HIGH_STR, \
FIFTYTWO_WEEK_LOW_STR, \
FIFTYTWO_WEEK_HIGH_STR, \
CHANGE_FROM_52_WEEK_LOW_STR, \
PERCENT_CHANGE_FROM_52_WEEK_LOW_STR, \
CHANGE_PERCENT_RT_STR, \
LAST_TRADE_SIZE_STR, \
CHANGE_FROM_52_WEEK_HIGH_STR, \
PERCEBT_CHANGE_FROM_52_WEEK_HIGH_STR, \
LAST_TRADE_RT_STR, \
LAST_TRADE_PRICE_ONLY_STR, \
TWOHUNDRED_DAY_MOVING_AVERAGE_STR, \
FIFTY_DAY_MOVING_AVERAGE_STR, \
CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR, \
PERCENT_CHANGE_FROM_200_DAY_MOVING_AVERAGE_STR, \
CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR, \
PERCENT_CHANGE_FROM_50_DAY_MOVING_AVERAGE_STR, \
OPEN_STR, \
PREVIOUS_CLOSE_STR, \
PRICE_PAID_STR, \
CHANGE_IN_PERCENT_STR, \
PRICE_TO_SALES_STR, \
PRICE_TO_BOOK_STR, \
PE_RATIO_STR, \
PE_RATIO_RT_STR, \
PEG_RATIO_STR, \
PRICE_TO_EPS_ESTIMATE_CURRENT_YEAR_STR, \
PRICE_TO_EPS_ESTIMATE_NEXT_YEAR_STR, \
REVENUE_STR, \
SHORT_RATIO_STR, \
ONE_YR_TARGET_PRICE_STR, \
VOLUME_STR, \
DAY_VALUE_CHANGE_STR, \
DIVIDEND_YIELD_STR, \
MARKET_CAPITALIZATION_STR, \
SHARES_OUTSTANDING_STR, \
MARKET_CAP_RT_STR, \
EBITDA_STR]


