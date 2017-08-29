'''
Stock Analylzer
Thomas Lockwood
8/29/2017

Goal: The purpose of this program is to take a csv file with the listed
stock index and the price at some given time. There will be a time line
for each stock index. I plan to calculate the volatility, average, and
any additional historical data that I can think of. My goal is to simulate
a "mock" stock trade to practice for the real dill.
'''

# Import all the external packages
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

# Read the CSV File
data = pd.read_csv("/Stock Data.csv")

# Add the average and std to the Table
data.loc["AVG"] = data.mean(axis=0)
data.loc["STD"] = data.std(axis=0)

# Print the data table
print(data)

# Plot the value of the portfolio
plt.plot(data.drop("AVG").drop("STD").loc[:,"Total"])
plt.ylabel("Value")
plt.show()
