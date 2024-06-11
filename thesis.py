#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 16:55:25 2024

@author: dangtranquangduy
"""

!pip install pandas_datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import cufflinks as cf
import seaborn as sns
from pandas_datareader import data as wb
from datetime import datetime

!pip install yfinance
import yfinance as yfin
yfin.pdr_override()

''' DATA IMPORT AND FORMATTING '''

hose_df = pd.read_csv('/Users/dangtranquangduy/Desktop/Thesis/stock_data.csv')
#Trim the dataframe to only keep Stock symbol, Close price, and Date
hose_df.drop(hose_df.iloc[:,[2, 3, 4, 6]], axis = 1, inplace = True)
#Convert Date format
date_str = hose_df.iloc[:,1].astype(str)
proper_date = pd.to_datetime(date_str, format='%Y%m%d')
hose_df.iloc[:,1] = proper_date.dt.strftime('%Y-%m-%d')
#Set stock tickers as columns
hose_df = hose_df.pivot(index = '<DTYYYYMMDD>', columns = '<Ticker>', values = '<Close>')
hose_df.reset_index(inplace=True)
#Rename the Date column
hose_df.rename(columns = {'<DTYYYYMMDD>':'Date'}, inplace = True)
#Remove stock data from before Feb 06, 2012
hose_df = hose_df[hose_df['Date'] >= '2012-02-06']
#Remove covered warrants from stock data
cw = hose_df.columns[hose_df.columns.str.contains('|'.join(['CACB', 'CCTD', 'CDPM', 'CGMD', 'CEIB', 'CFPT',\
                                                            'CHDB', 'CHPG','CKDH', 'CMBB', 'CMSN', 'CMWG', \
                                                            'CNVL', 'CPDR', 'CPNJ', 'CPOW', 'CREE', 'CROS', \
                                                            'CSBT', 'CSHB', 'CSTB','CTCB', 'CTCH', 'CTPB', \
                                                            'CVHM', 'CVIB', 'CVIC', 'CVJC', 'CVNM', 'CVPB', 'CVRE']))]
cw = cw.drop(cw[1078])
hose_df.drop(columns=cw, inplace=True)
hose_df.set_index('Date', inplace = True )
''' THE ANALYSIS START HERE '''

