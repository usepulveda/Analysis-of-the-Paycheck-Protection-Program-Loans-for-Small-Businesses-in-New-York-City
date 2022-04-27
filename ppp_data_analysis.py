#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:00:12 2022

@author: ulisessepulveda
"""

#%%1.Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from plotly.offline import plot
import plotly.graph_objects as go
plt.style.use('ggplot')

#%%2.Loading our data and checking first five rows
ppp = pd.read_csv('cleaned_ppp_nyc_data.csv')
ppp.head()

#%%3. Checking the number of industries in each subcategory for the first graph:.
ppp['industry'].value_counts()

#. Grouping loan_amount by industry and taking only the top 10 industries with loan amount 
#summing the total by industry and printing the outcome.
top_10_industries = ppp['loan_amount'].groupby(ppp['industry']).sum()[:10].sort_values(ascending=False).astype(int)
top_10_industries
print(top_10_industries.sum())

# Creating the labels and graph setup for top_10 industries.
labels = ['Health Care and Social Assistance','Construction',
          'Educational Services', 'Accommodation and Food Services',
          'Administrative Services', 'Arts and Recreation',
          'Information', 'Finance and Insurance',
          'Agriculture, Forestry, Fishing and Hunting', 'Management of Companies and Enterprise']

# Using `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=top_10_industries, hole=.4)])

fig.update_layout(
    title_text="Top 10 Industries vs Loan Amount",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='$2,770,068,025', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=900,
        height=900,)
fig.show()
plot(fig, auto_open=True)

#%%4.Creating the graph for top_15 lenders, printing it anf then graphing the output.
top_10_lenders = ppp.groupby('lender')['loan_amount'].sum()
top_10_lenders = top_10_lenders.sort_values(ascending=False)[:10].astype(int)
top_10_lenders

# Creating the labels for the top 15 lenders to then graph the output.
lenders = ['JPMorgan Chase Bank, National Association ', 'Signature Bank ', \
           'TD Bank, National Association', 'Cross River Bank', 'Bank of America, National Association', \
          'Citibank, N.A. ', 'Northfield Bank', 'Valley National Bank',  \
          'Manufacturers and Traders Trust Company', 'Kabbage, Inc.', 'HSBC Bank USA, National Association', \
          'Harvest Small Business Finance, LLC', 'The Bank of Princeton', 'Santander Bank, National Association ', \
          'Dime Community Bank']

fig = go.Figure(data=[go.Pie(labels=lenders, values=top_10_lenders, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="Top 10 Lenders vs Loan Amount",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='$3,800,799,121', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=900,
        height=900,)
                 
fig.show()
plot(fig, auto_open=True)

#%%5. Creating the graph for jobs reported by SBA by borough and printing it
boroughs = ppp['loan_amount'].groupby(ppp['borough']).sum().sort_values(ascending=False)
print(boroughs.sum())

borough_labels = ['BROOKLYN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'MANHATTAN']
fig = go.Figure(data=[go.Pie(labels=borough_labels, values=boroughs, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="NYC Boroughs vs Loan Amount",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='$4,754,806,357', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=700,
        height=700,)
plot(fig, auto_open=True)

#%%6. Checking the total number of jobs reported in each city and graphing it.
jobs_reported_by_borough = ppp.groupby('borough')['jobs_reported'].sum()
jobs_reported_by_borough
print(jobs_reported_by_borough.sum())

ax = jobs_reported_by_borough.plot(kind='bar', title='Total Jobs reported in each Borough', xlabel='Borough',
               ylabel='Jobs reported', figsize=(15, 8));
#
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.05, p.get_height() * 1.01))

#Rotating x-axis ticks vertically
plt.xticks(rotation=0);

#%%7.Checking and graphing the number of lenders in each borough
borough_vs_lender = ppp.groupby('borough')['lender'].count().sort_values(ascending=False)
borough_vs_lender
print(ppp['lender'].count())

borough_labels = ['BROOKLYN', 'BRONX','STATEN ISLAND', 'QUEENS', 'MANHATTAN']
fig = go.Figure(data=[go.Pie(labels=borough_labels, values=borough_vs_lender, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="No. of Lenders for each Borough",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='52,903', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=600,
        height=600,)
plot(fig, auto_open=True)


