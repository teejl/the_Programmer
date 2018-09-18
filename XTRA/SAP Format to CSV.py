# -*- coding: utf-8 -*-
'''
Thomas Lockwood
9/13/2017
The goal of this file is to convert the ECC files into a CSV file
'''

import pandas as pd
import numpy as np


def main(file):
    # Import the txt file as a dataframe
    raw = pd.read_table(file, header = None) # import as a table
    
    # Pull Data, Split data and clean
    head = raw.iloc[15].str.replace('"', "").str.split("|", expand=True)
    dlist = raw[raw[0].str[3:5] == '20'][0].str.replace('"', "").str.split("|", expand=True)
    
    # Take off spaces on outside
    for i in range(dlist.shape[1]):
        dlist[dlist.columns[i]] = dlist[dlist.columns[i]].str.replace('"', '').str.strip()
    
    # Add column headers to data
    dlist.columns = head.iloc[0].str.strip()
    del dlist[dlist.columns[0]]

    # Fill in missing PCs
    key = dlist[dlist['Profit Center'] != ""][['Document#', 'Profit Center']]
    key.set_index('Document#', inplace=True)
    dlist['Profit Center'] = pd.merge(dlist, key, left_on='Document#', right_index=True,
                       how='left' , sort=False).columns[3]
    
    # PC's not found check
    empty = dlist[dlist['Profit Center'] == ""][['Document#', 'Profit Center']]
    print(empty)
    
    # Change values parity
    dlist.loc[dlist['Value'].str[-1] != "-", 'Value'] = '-' + dlist['Value'].str[:]
    dlist.loc[dlist['Value'].str[-1] == "-", 'Value'] = dlist['Value'].str[:-1]
    
    # Turn the Value column into a string and find total
    dlist['Value'] = dlist['Value'].str.replace(",","").apply(pd.to_numeric)
    print(dlist.Value.sum())
    
    # Add BUs and split shared
    
    # Add Categories
    
    # Add Aging and Aging Category
    
    # Output the csv file
    dlist.to_csv(file[:-4] + '-Formatted.csv', sep="|", index=False)
    
    # Save to Excel File
   
main('P8 2017-Dummy.txt')
