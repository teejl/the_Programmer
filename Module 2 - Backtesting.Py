'''
MODULE 2 - BACKTESTING
 lesson by The Python Quants GmbH
 written by Thomas Lockwood
9/7/2017

Goal: The goal of this lesson is to learn how to create trading strats and
simulate these strats against historical data.
'''

# Import Packages
import numpy as np  # array operations
import pandas as pd  # time series management
from pandas_datareader import data as web  # data retrieval
import matplotlib.pyplot as plt  # standard plotting library
from pylab import plt

# Getting Index Level Data
SPY = web.DataReader('SPY', data_source='google', start='2005-1-1')
SPY.tail() # last 5 rows

# Generating Trading Signals
# We are going to use SMAx - simple moving averages for x days
# Our method is if SMA42>SMA252 long elif > we short (nothing if equal)

SPY['SMA42'] = SPY['Open'].rolling(window=42).mean() # calc SMAs
SPY['SMA252'] = SPY['Open'].rolling(window=252).mean()
SPY.dropna(inplace = True)  # drop rows with NaN values

#SPY[['Open', 'SMA42', 'SMA252']].plot(figsize=(10,6)) # visual

SPY['position'] = np.where(SPY['SMA42'] > SPY['SMA252'], 1, -1) # vector position
SPY[['Open', 'position']].plot(subplots = True, figsize=(10,6)) # visual
plt.ylim(-1.1, 1.1) # adjust y-axis
#plt.show()

# Backtesting = Judging Performance
SPY['market'] = np.log(SPY['Open']/SPY['Open'].shift(1)) # log returns
SPY['strat'] = SPY['position'].shift(1) * SPY['market'] # our returns
SPY[['market', 'strat']].cumsum().apply(np.exp).tail()# measure returns
SPY[['market', 'strat']].cumsum().apply(np.exp).plot(figsize=(10,6)) # visual
#plt.show()

# Risk and Return
print('Anualized Returns')
arets = SPY[['market', 'strat']].mean() * 252
print(arets) # print annualized return
print('Anualized Volatility')
astds = SPY[['market', 'strat']].std() *252 ** 0.5
print(astds) # print annualized volatility





