# This should gauge how my retirement fund is doing.

# import packages
import numpy as np
import pandas as pd
from pylab import plt
from math import sqrt
plt.style.use('ggplot')
from pandas_datareader import data as web

# Find prices of stocks from yahoo
#SPY = web.DataReader('SPY', data_source='yahoo')
BLCK = web.DataReader('STLFX', data_source='yahoo')
Start = BLCK['Close'].loc['2017-06-01']
Current = BLCK['Close'].iloc[-1]
rets = np.log(BLCK['Close'].loc['2017-06-01':]/BLCK['Close'].loc['2017-06-01':].shift(1))

# Prompt to the user the prices
print('You are currently investing in Black Rock mutual fund (STLFX) target retirement date of 2050. ')
print()
print('The price per share whenever you started around 6-1-2017 was around ' + str(Start) + '.')
print('The most recent price is ' + str(Current) + '.')
print()

# find loss/growth indicator
change = (round(Current/Start,4)-1)*100
if change < 0:
    c_ind = 'loss'
else:
    c_ind = 'growth'

# compute annual expected growth and volatility
anngrow = (round(np.exp(rets.mean()*(252)),4)-1)*100
annvol = round((np.exp(rets.std())-1)*sqrt(252),4)*100

# report the results
print('The performance of the stock is ' + str(change) + '% ' + c_ind + '.') 
print('The expected growth is ' + str(anngrow) + '% annually.')
print('The volatility of the fund is ' + str(annvol) + '% annually.')

# map the performance of the stock since i started workign
BLCK['Close'].loc['2017-06-01':].plot()
#SPY['Close'].loc['2017-06-01':].plot(figsize=(10,6))
plt.show()

# Plot the frequency chart
# rets.hist(bins=35)
# plt.show()

# Plot the noise chart
rets.plot()
plt.show()





rets.plot()

rets.hist(bins=35)


#input_var = input("Press enter to close the program.")
