# Import Stock Data
# by Thomas Lockwood
# 01-24-2019

# import packages
import numpy as np
import pandas as pd
import datetime as dt
#from pandas_datareader import data as web #could not connect to server
import fix_yahoo_finance as yf

start = dt.datetime(2010,1,1)
end = dt.datetime(2010,1,27)
end_date = str(dt.date.today())

# set up a connection to the stock data
# df = web.DataReader('AMZN', 'google', start, end) #could not connect to server
df = yf.download('FXAIX', '2000-01-01', end_date)
print(df.head())
print(df.tail())
