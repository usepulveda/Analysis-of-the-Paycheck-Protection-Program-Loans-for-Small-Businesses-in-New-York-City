#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 22:04:39 2022

@author: ulisessepulveda
"""
#%%1.Importing libraries
import pandas as pd

#%%2.Loading and reading the data in the csv file for PPP's loans in NY State
ppp_loans = pd.read_csv('ppp_loans_state_NY.csv')
ppp_loans.head()

# Checking columns in our data
ppp_loans.columns

# Creating a new dataframe and taking only the required columns for the analysis
ppp_loans = ppp_loans[[' loan_amount ', 'zip', 'naics_code', 'jobs_reported', 'lender', 'city_clean']]
ppp_loans.head()

# Eliminating unnecessary spaces in column 'loan_amount' 
ppp_loans.rename(columns = {' loan_amount ':'loan_amount', 'city_clean':'borough'}, inplace = True)

# Checking the data type and null values in each column
ppp_loans.info()

# Fixing the column "loan_amount" contains an incorrect values
ppp_loans[ppp_loans['loan_amount'] ==  ' -   '].count()

# Updating the dataframe with the correction
ppp_loans = ppp_loans[ppp_loans['loan_amount'] != ' -   ']
ppp_loans.info()

# Removing commas from loan_amount values, which will convert it from string to float
ppp_loans['loan_amount']=ppp_loans['loan_amount'].str.replace(',','').astype(float)
ppp_loans.head()

#%%3. Dropping all of the null values
ppp_loans.dropna(inplace=True)
ppp_loans.isnull().sum()

#%%4.Converting the columns jobs_reported and naics_code into intergers and strings
ppp_loans['jobs_reported'] = ppp_loans['jobs_reported'].astype(int)
ppp_loans['naics_code'] = ppp_loans['naics_code'].astype(str)

#%%5. Selecting thethe required boroughs and updating the dataframe
borough = ['BROOKLYN', 'BRONX', 'MANHATTAN', 'QUEENS', 'STATEN ISLAND']

ppp_loans = ppp_loans[ppp_loans['borough'].isin(borough)]
ppp_loans.head()
ppp_loans.info()

#%%6. Getting the first two digits of naics_code and converting the column to int, 
# to later map each naics_code with its corresponding industry
ppp_loans['naics_code'] = ppp_loans['naics_code'].str[:2].astype(int)
ppp_loans.head()

#%%7. Creating a dictionary of naics code to assign to the corresponding industry.
naics_map = {11: 'Agriculture, Forestry, Fishing and Hunting',
            21: 'Mining, Quarrying, and Oil and Gas Extraction',
            22: 'Utilities', 
            23: 'Construction',
            31: 'Manufacturing', 
            32: 'Manufacturing', 
            33: 'Manufacturing',
            42: 'Wholesale Trade',
            44: 'Retail Trade', 
            45: 'Retail Trade',
            48: 'Transportation and Warehousing', 
            49: 'Transportation and Warehousing',
            51: 'Information',
            52: 'Finance and Insurance',
            53: 'Real Estate and Rental and Leasing',
            54: 'Professional, Scientific, and Technical Services',
            55: 'Management of Companies and Enterprises',
            56: 'Administrative Services',
            61: 'Educational Services',
            62: 'Health Care and Social Assistance',
            71: 'Arts and Recreation',
            72: 'Accommodation and Food Services',
            81: 'Other Services',
            92: 'Public Administration'}

# Mapping naics codes and associating these with their respective numeric series and name.
ppp_loans['naics_code'] = ppp_loans['naics_code'].map(naics_map)

#%%7. Renaming naics_code column to industry.
ppp_loans.rename(columns = {'naics_code':'industry'}, inplace = True)
ppp_loans.head()

#Dropping all of the null values
ppp_loans.isnull().sum()

ppp_loans = ppp_loans.dropna()
ppp_loans.isnull().sum()

ppp_loans.to_csv('cleaned_ppp_nyc_data.csv')