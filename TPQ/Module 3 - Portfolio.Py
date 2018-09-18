'''
MODULE 3 - PORTFOLIO MANAGEMENT
 lesson by The Python Quants GmbH
 written by Thomas Lockwood
9/7/2017

Goal: The goal of this lesson is to learn how to manage a portfolio of
stocks and to manage progress based on the weighted stocks chosen.
'''

# Import Packages
import numpy as np  # array operations
import pandas as pd  # time series management
from pandas_datareader import data as web  # data retrieval
import matplotlib.pyplot as plt  # standard plotting library
from pylab import plt
plt.style.use('ggplot')

# Retrieving Stock Price Data
symbols = ['AAPL', 'MSFT', 'YHOO', 'AMZN', 'GOOG']  # our symbols
data = pd.DataFrame()  # empty DataFrame
for sym in symbols:
    data[sym] = web.DataReader(sym, data_source='google', start ='2010-01-01')['Open']

print(data.tail()) # print last 5 rows
(data / data.ix[0] * 100).plot(figsize=(10,6)) # normalize the values and plot
plt.show()

# Portfolio Returns
log_rets = np.log(data / data.shift(1)) # vectorized calc of log returns
rets = log_rets.mean() * 252 # annualized average log returns
print('Annualized Average Log Returns')
print(rets)

weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # equal weightings

# in mathematics the portfolio return is given as E[wE[S]] = wE[S]
# which is the the weight times the expectated return of the stock
np.dot(weights, rets) # annualized portfolio return
print('Annualized Portfolio Return')
print(np.dot(weights,rets))

# in mathematics the portfolio variance is much more involved...
log_rets.cov() * 252 # annualized covariance matrix
pvar = np.dot(weights.T, np.dot(log_rets.cov() * 252, weights)) # Porftolio variance
print('Annualized Portfolio Variances')
print(pvar)

# and so having the variance we can calc the annualized volatility
pvol = pvar ** 0.5 # annualized portfolio volatility
print('Annualized Portfolio Volatility')
print(pvol)

# Random Portfolio Compositions
weights = np.random.random(5) # random numbers
weights /= np.sum(weights) # normalization to 1
weights # random portfolio composition
np.dot(weights, rets) # portfolio return (random weights)
np.dot(weights.T, np.dot(log_rets.cov() * 252, weights)) # portfolio variance (random weights)

    # Monte Carlo Simulation
prets = []
pvols = []
for p in range(5000):
    weights = np.random.random(5)
    weights /= np.sum(weights)
    prets.append(np.sum(log_rets.mean() * weights) * 252)
    pvols.append(np.sqrt(np.dot(weights.T, 
                        np.dot(log_rets.cov() * 252, weights))))
prets = np.array(prets)
pvols = np.array(pvols)
portfolio = pd.DataFrame({'return': prets, 'volatility': pvols})
portfolio.plot(x='volatility', y='return', kind='scatter', figsize=(10,6))
plt.show()
