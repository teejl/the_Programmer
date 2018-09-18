'''
Account Analysis
Thomas Lockwood
08-31-2017

Goal: The goal of this program is to do perform analytical functions
and data manipulation with python instead of excel. The pros of
python is that it runs much quicker, takes up less memory, and
if coded correctly can be used for multiple files.
'''

# Imports
import pandas as pd
import numpy as np
import os

# Below is some ways excel files can be open with Pandas and openpyxl
# Read the account information
# acc_data = pd.read_excel("export.xlsx", 'Sheet1')

# wb = load_workbook('export.xlsx')
# print(wb.get_sheet_names())
# df = pd.DataFrame(wb["Sheet1"].values)


'''
Thomas Lockwood
9/13/2017
The purpose of this file is to convert the consolidated tab on the 10 account
file into a csv file
'''
def xlsx_to_txt(file, save_to, account, period, year):
    #Import the excel file
    #data = pd.read_excel('P09 2017-10 Account Workbook-Dummy.xlsx', 'Consolidated')
    #print(data)
    
    MASTER = ['Reporting Year',
              'Reporting Period',
              'G/L Account', 
              'Year',
              'Period',
              'Vendor#',
              'Vendor Name',
              'Document#',
              'Entry Date',
              'Posting Date',
              'Document Date',
              'Age',
              'Aging Category',
              'Clearing Date',
              'Document Type',
              'Profit Center',
              'Division',
              'BU',
              'Blocked',
              'Clearing Document',
              'Reference',
              'Internal Order',
              'Material Group',
              'Material Group Desc',
              'Category',
              'Category Type',
              'Purchasing Document',
              'House Bank',
              'Amount',
              'DB/INV',
              'Last PO Activity',
              'PO act aging',
              'Item',
              'Material',
              'Cost Center',
              'Plant',
              'Short Text',
              'Quantity',
              'Requisitioner Name',
              'WBS Element',
              'Current',
              '30-59 days',
              '60-89 days',
              '90-179 days',
              '180 days plus',
              'QBSR Age',
              'QBSR Aging Category']
    
        
    # Import the 'Consolidated' tab from the 10 File
    log = pd.DataFrame()
    df = pd.read_excel(file, 'Consolidated')
    cols = df.columns.tolist()
    
    # Rename the Misnamed Columns
    ### df['G/L Account'] = '20100' + str(account)
    df.rename(columns= {'Type': 'Category Type',
                        ' Vendor':'Vendor#', 
                        'IN/DB': 'DB/INV',
                        'INV/DB': 'DB/INV',
                        'Sum of      Value': 'Amount',
                        'Material Group Description':'Material Group Desc',
                        'Aging':'Age',
                        'Vendor': 'Vendor#',
                        'VendorName': 'Vendor Name',
                        'Doc Type':'Document Type',
                        'Purchasing Doc.':'Purchasing Document',
                        'Profit Centre': 'Profit Center',
                        'Date of Last Activity': 'Last PO Activity',
                        'Last PO Activity Date': 'Last PO Activity',
                        'Last Posting Date': 'Last PO Activity',
                        'QBSR Aging Cat': 'QBSR Aging Category',
                        'Aging based on PO act': 'PO act aging',
                        'DocumentNo': 'Document#',
                        'Purch.Doc.': 'Purchasing Document',
                        'Last Activity': 'Last PO Activity',
                        'Profit Ctr': 'Profit Center',
                        'Pstng Date': 'Posting Date',
                        'Sum of LC amnt': 'Amount',
                        'Sum of          LC amnt': 'Amount',
                        'Aging ': 'Aging Category',
                        'QBSR Aging' : 'QBSR Aging Category',
                        'Requistioner' : 'Requisitioner Name',
                        'PO Based Age': 'PO act aging',
                        'Last Activity Date': 'Last PO Activity',
                        'Age Category': 'Aging Category',
                        'Sum of  Amount in local currency': 'Amount',
                        'Age Bracket' : 'Aging Category',
                        'Age since last activity' : 'PO act aging',
                        'Matl Group': 'Material Group',
                        'Cost Ctr' : 'Cost Center',
                        '         Current' : 'Current',
                        '   31 - 60 days' : '30-59 days',
                        '   61 - 90 days' : '60-89 days',
                        ' 91 - 180 days' : '90-179 days',
                        '      Over 180' : '180 days plus',
                        'Aging based on last posting' : 'PO act aging',
                        '      Quantity' : 'Quantity',
                        'Plnt' : 'Plant',
                        'PostingDate' : 'Posting Date',
                        ' Material Group Description' : 'Material Group Desc',
                        ' Category' : 'Category',
                        'PurchasingDocument' : 'Purchasing Document',
                        'ProfitCenter' : 'Profit Center',
                        'DocumentDate' : 'Document Date',
                        'HouseBank': 'House Bank',
                        'Sum of Value': 'Amount',
                        'Cost Centre' : 'Cost Center',
                        'CostCenter' : 'Cost Center',
                        'CostCentre' : 'Cost Center',
                        ' Over 180 days' : '180 days plus',
                        '  61 - 90 days': '60-89 days',
                        '  91 - 180 days': '90-179 days',
                        'WBS element' : 'WBS Element',
                        'Divison' : 'Division',
                        'QBSR' : 'QBSR Aging Category',
                        'Sum of  Amt in loc.cur.': 'Amount',
                        'Division ' : 'Division',
                        '        Current':'Current',
                        '    31 - 60 days':'30-59 days',
                        '      91 - 180': '90-179 days',
                        'WBS elem.': 'WBS Element',
                        '       61 - 90':'30-59 days',
                        'Vendor2': 'Vendor Name',
                        'Type2' : 'Category Type',
                        'Date of last activity': 'Last PO Activity',
                        'Last Posting Activity' : 'Last PO Activity',
                        'Category Description' : 'Material Group Desc',
                        'Category Descripton' : 'Material Group Desc',
                        'G/L' : 'G/L Account',
                        'GL' : 'G/L Account',
                        'PO Number' :'Purchasing Document',
                        'Total': 'Amount',
                        'aging days' : 'Age',
                        'bsr aging' : 'QBSR Aging Category',
                        '2016 Div' : 'Division',
                        '2016 BU' : 'BU',
                        'Sum of Amount' : 'Amount',
                        'Category ': 'Category',
                        'BSR Aging': 'QBSR Aging Category',
                        'Bu' : 'BU',
                        'Age Cat':'Aging Category',
                        'Dvision' : 'Division',
                        'G/L Acct': 'G/L Account',
                        'Document# ': 'Document#',
                        ' Vendor  ' : 'Vendor#',
                        'Vendor Name                                                           ': 'Vendor Name',
                        'Div' : 'Division',
                        'Clearing doc' : 'Clearing Document',
                        'Doc Date' : 'Document Date',
                        'GL ': 'G/L Account',
                        'Posting date': 'Posting Date',
                        'PD' : 'Posting Date',
                        'Sum of       Value ': 'Amount',
                        'Mat Group Desc' : 'Material Group Desc',
                        'bsr category' : 'QBSR Aging Category',
                        'Category Discription': 'Category Description',
                        'Sum of         LC amnt': 'Amount',
                        '  G/L Account' : 'G/L Account',
                        'Business Unit' : 'BU', 
                        'Sum of      Value      ' : 'Amount'
                        },
                        inplace=True)
    
    # Add the Missing Columns
    df['Reporting Year'] = year
    df['Reporting Period'] = period
    
    temp = []
    for item in MASTER:
        if item not in df:
            df[item] = ""
            temp.append(item)
            
    # Write the sorted columns to CSV file
    if period < 10:
        p = '0' + str(period)
    else:
        p = str(period)
        
    df[MASTER].to_csv(save_to + "/P" + p + " " + str(year) + "-" + str(account)
    + "-Formatted.txt", sep ='|', index=False )

    # Output the log
    diff = []
    for item in df:
        if item not in MASTER:
            diff.append(item)
    
    # Logging the progress
    print("The following columns were added")
    print(len(temp),temp)
    print()
    print("The following columns were not on the Master Header")
    print(len(diff), diff)
    #print(' ')
    
    # File completed!
    print()
    print(file + " COMPLETE!")
    
    
def execute(path):
    # This program will go through the files and create txt files
    # Get the path of the files
    directory = os.listdir(path)
    
    for file in directory:
        if file[-5:] == '.xlsx':
            period = int(file[1:3])
            year = int(file[4:8])
            account = file[9:11]
            print('\t____________________________________________________________')
            print('\t\t\tPeriod\t', 'Year\t', 'Account\t',)
            print('\t\t\t ', period, '\t', year, '\t', account, '\t')
            print()
            xlsx_to_txt(path + '/' + file, path.split('/')[0], account, period, year)

def bump():
    print('############################################################################')
    
def title():
    bump()
    print('\t\t\t PROGRAM: APRDB Formatting')
    print('\t\t\t created by TeeJ Lockwood')
    print()
    print('\t GOAL: The purpose of this program is to convert the .xlsx')
    print(' \t document consolidated tab to a .txt file with a | delimter')
    print(' \t it does this by looking into this current working directory')
    print(' \t for a folder 00 Account Workbook/2016 or of similar format.')
    print(' \t The out put will be saved to 00 Account Workbook or which')
    print(' \t ever that is used. Please keep the file names in the')
    print(' \t following format: P01 2016-10 or of the sort.')
    print()
    bump()

def end():
    bump()
    print()
    print('\t The Program has run successfully! Please enjoy :)')
    print()
    bump()
# Execute the Program  
def mag():
    # Header to the Magazine
    title()
    
    # Run the 00 Account
    execute('00 Account Workbook/2015')
    bump()
    print('\t 00 2015 Account Workbook Complete!')
    bump()
    
    ### execute('00 Account Workbook/2016') 
    bump()
    print('\t 00 2016 Account Workbook Complete!')
    bump()
    
    ### execute('00 Account Workbook/2017') 
    bump()
    print('\t 00 2017 Account Workbook Complete!')
    bump()
    
    # Run the 02 Account
    ### execute('02 Account Workbook/2015')
    bump()
    print('\t 02 2015 Account Workbook Complete!')
    bump()
    
    ### execute('02 Account Workbook/2016')
    bump()
    print('\t 02 2016 Account Workbook Complete!')
    bump()
    
    ### execute('02 Account Workbook/2017')
    bump()
    print('\t 02 2017 Account Workbook Complete!')
    bump()
    
    # Run the 10 Account
    ### execute('10 Account Workbook/2015')
    bump()
    print('\t 10 2015 Account Workbook Complete!')
    bump()
    
    ### execute('10 Account Workbook/2016')
    bump()
    print('\t 10 2016 Account Workbook Complete!')
    bump()
    
    execute('10 Account Workbook/2017')
    bump()
    print('\t 10 2017 Account Workbook Complete!')
    bump()
    
    # The End
    end()
    
# Executing the Program    
mag()


def rename(directory):
    # Rename the list of files in a directory
    for file in directory:
        if file[-4:] == ".txt":
            new_file = 'NASS_GL_Account_' + file[9:11] + '_' + file[0:3] 
            + '_' + file[4:8] + '.csv'
            os.rename(file, new_file)
            



