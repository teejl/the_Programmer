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
data = pd.read_csv("C:/Users/80053507/Stocks/Stock Data.csv")

# Add the average, std, profit, and days to the Table
data.loc["AVG"] = round(data.mean(axis=0),2)
data.loc["STD"] = round(data.std(axis=0),2)
data.index.name = "Days"

# Print the data table
# print(data)

# Plot the value of the portfolio
plt.plot(data.drop("AVG").drop("STD").loc[:,"Total"])
plt.ylabel("Value")
plt.xlabel("Days")
rows = data.shape[0] - 2
plt.xticks(np.arange(1,rows , 1.0))


# Print the progress of the portfolio
earnings = data.loc[:,"Total"][-3] - data.loc[:,"Total"][0]
df = (data.ix[-2] - data.ix[0])[1:-1]
best_stock = df.idxmax()
best_profit = round(df.max(),2)
worst_stock = df.idxmin()
worst_profit = round(df.min(),2)

print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~     Portfolio Analysis    ~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("")
print(data.loc[:,["Total"]])
print("Earnings as of today: " + str(earnings) + ".")
print("This is about " + str(round(earnings/(data.shape[0]-2),2)) + " per day.")
print("")
print("We have the following earnings per share:")
print((data.ix[-2] - data.ix[0])[1:])
print("")
print("Most profitable stock is " + str(best_stock) + " with a profit of " + str(best_profit) + ".")
print("Least profitable stock is " + str(worst_stock) + " with a profit of " + str(worst_profit) + ".")
print("")
print("The profitable stocks are:")
print(df[df>0])
#print("The list of non profitable stocks:")
#print(df[df<0])
plt.show()
