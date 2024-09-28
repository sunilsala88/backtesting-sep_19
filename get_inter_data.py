# from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook
# import datetime as dt
# import pandas as pd
# ib = IB()
# ib.connect('127.0.0.1', 7497, clientId=66)

# contract2=Stock('TSLA','NYSE','USD')
# bars = ib.reqHistoricalData(
#     contract2, endDateTime='', durationStr='1 Y',
#     barSizeSetting='1 hour', whatToShow='TRADES', useRTH=True,formatDate=2)
# df1 = util.df(bars)

# d1={'date':'Date','open':'Open','high':'High','low':'Low','close':'Close','volume':'Volume'}
# df1.rename(columns =d1, inplace = True) 
# df1.set_index('Date',inplace=True)
# data=df1
# print(data)
# data.to_csv('TSLA_1hour.csv')  


from alpaca.data.historical import StockHistoricalDataClient
from datetime import datetime,timedelta
from zoneinfo import ZoneInfo

from alpaca.data.requests import StockBarsRequest ,StockTradesRequest,StockQuotesRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

from alpaca.data.enums import Adjustment



# setup stock historical data client
stock_historical_data_client = StockHistoricalDataClient(api_key, secret_key)

symbol='SPY'

# get historical bars by symbol
# ref. https://docs.alpaca.markets/reference/stockbars-1
# now = datetime.now(ZoneInfo("America/New_York"))
# req = StockBarsRequest(
#     symbol_or_symbols = symbol,
#     timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Day), # specify timeframe
#     start = now - timedelta(days = 1000),                          # specify start datetime, default=the beginning of the current day.
#     # end_date=None,                                        # specify end datetime, default=now
#     # limit = 2,                                               # specify limit
# )
# data=stock_historical_data_client.get_stock_bars(req).df
# print(data)



now = datetime.now(ZoneInfo("America/New_York"))
req = StockBarsRequest(
    symbol_or_symbols = symbol,
    timeframe=TimeFrame(amount = 1, unit = TimeFrameUnit.Hour), # specify timeframe
    start = now - timedelta(days = 3000),                       # specify start datetime, default=the beginning of the current day.
    
    # end_date=datetime(2024,7,24),                                        # specify end datetime, default=now
    # limit = 2,                                               # specify limit
    adjustment=Adjustment.ALL
)
data=stock_historical_data_client.get_stock_bars(req).df
print(data)

data.to_csv('spy_hour.csv')

# get historical trades by symbol
# req = StockTradesRequest(
#     symbol_or_symbols = symbol,
#     start = now - timedelta(days = 3),                          # specify start datetime, default=the beginning of the current day.
#     # end=None,                                             # specify end datetime, default=now
#     # limit = 2,                                                # specify limit
# )
# data=stock_historical_data_client.get_stock_trades(req).df
# print(data)


# # get historical quotes by symbol
# req = StockQuotesRequest(
#     symbol_or_symbols = [symbol],
#     start = now - timedelta(days = 3),                      # specify start datetime, default=the beginning of the current day.
#     # end=None,                                             # specify end datetime, default=now
#     # limit = 2,                                              # specify limit
# )
# data=stock_historical_data_client.get_stock_quotes(req).df
# print(data)