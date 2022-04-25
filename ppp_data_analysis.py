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
top_5_industries = ppp['loan_amount'].groupby(ppp['industry']).sum()[:10].sort_values(ascending=False).astype(int)
top_5_industries
print(top_5_industries.sum())

# Creating the labels and graph setup for top_10 industries.
labels = ['Health Care and Social Assistance', 'Educational Services', 
          'Construction', 'Administrative Services', 
          'Agriculture, Forestry, Fishing and Hunting']

# Using `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=top_5_industries, hole=.4)])

fig.update_layout(
    title_text="Top 5 Industries vs Loan Amount",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='$2,235,195,484', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=900,
        height=900,)
fig.show()
plot(fig, auto_open=True)

#%%4.Creating the graph for top_15 lenders, printing it anf then graphing the output.
top_15_lenders = ppp['loan_amount'].groupby(ppp['lender']).sum()[:15].sort_values(ascending=False).astype(int)
top_15_lenders
print(top_15_lenders.sum())

# Creating the labels for the top 15 lenders to then graph the output.
lenders = ['JP Morgan Chase', 'Alma Bank', 'Amboy Bank ', 'Accion',           
           'Alpine Capital Bank ', '1st Constitution Bank ', 'Allegiance Bank',           
           'Abacus Federal Savings Bank ', 'Affinity FCU ', 'Access Bank',           
           'Accion East, Inc.', '1st Choice CU ', 'Adams Community Bank',           
           'Academy Bank, National Association ', 'Allied First Bank ']

fig = go.Figure(data=[go.Pie(labels=lenders, values=top_15_lenders, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="Top 15 Lenders vs Loan Amount",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='$7,804,574', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=900,
        height=900,) 
fig.show()
plot(fig, auto_open=True)

#%%5. Creating the graph for jobs reported by SB by borough and printing it
boroughs = ppp['loan_amount'].groupby(ppp['borough']).sum().sort_values(ascending=False)
print(boroughs.sum())

borough_labels = ['BROOKLYN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'MANHATTAN']
fig = go.Figure(data=[go.Pie(labels=borough_labels, values=boroughs, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="Top Boroughs vs Loan Amount",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='$3,800,799,121', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=700,
        height=700,)
plot(fig, auto_open=True)

# Checking the total number of jobs reported in each city
jobs_reported_by_borough = ppp.groupby('borough')['jobs_reported'].sum()
jobs_reported_by_borough

ax = jobs_reported_by_borough.plot(kind='bar', title='Total Jobs reported in each Borough', xlabel='Borough',
               ylabel='Jobs reported', figsize=(15, 8));
#
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() * 1.05, p.get_height() * 1.01))

#Rotating x-axis ticks vertically
plt.xticks(rotation=0);

#%%6.Checking and graphingh the number of lenders in each borough
borough_vs_lender = ppp.groupby('borough')['lender'].count().sort_values(ascending=False)
borough_vs_lender

print(ppp['lender'].count())

borough_labels = ['BROOKLYN', 'BRONX','STATEN ISLAND', 'QUEENS', 'MANHATTAN']
fig = go.Figure(data=[go.Pie(labels=borough_labels, values=borough_vs_lender, textinfo='label+percent', hole=.4)])

fig.update_layout(
    title_text="No. of Lenders in each Borough",
    # Adding annotations in the center of the donut pies.
    annotations=[dict(text='43,421', x=0.50, y=0.5, font_size=15, showarrow=False)],
    autosize=False,
        width=600,
        height=600,)
plot(fig, auto_open=True)


