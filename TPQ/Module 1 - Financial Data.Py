'''
MODULE 1 - FINANCIAL DATA
 lesson by The Python Quants GmbH
 written by Thomas Lockwood
9/7/2017

Goal: The goal of this lesson is to learn how to pull stock information
to be used for models and algorithmic trading strategies.
'''


# Import Packages
import numpy as np # array operations
import pandas as pd # time sereies management
from pandas_datareader import data as web # data retrieval
from pylab import plt
plt.style.use('ggplot')

# Retrieve stock price
AMZN = web.DataReader('AMZN', data_source='google')
print(type(AMZN)) # print type
print(AMZN.info()) # print meta information

# Data Manipulation
AMZN.tail() # select last 5 rows
AMZN.head() # select first 5 rows

AMZN['Open'].tail() # select last 5 rows of the column 'Open'
AMZN['Close'].tail()
AMZN[['Open', 'Close']].tail()

AMZN.loc['2016-05-02'] # single row index value
AMZN.iloc[:2] # select rows 1 and 2 via index numbers

# Data Visualization
AMZN['Open'].plot(figsize=(10,6)) # a time series plot
#plt.show()

rets = np.log(AMZN['Open']/AMZN['Open'].shift(1)) # calc log returns
rets.hist(figsize = (10,6), bins=35)
#plt.show()

# Adding and Calculating Moving Average
AMZN['MA50'] = AMZN['Close'].rolling(50).mean() # create new column
AMZN[['Close', 'MA50']].plot(figsize=(10,6)) # plot the time series


