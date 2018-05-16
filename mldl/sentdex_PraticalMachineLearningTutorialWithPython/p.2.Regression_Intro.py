#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# regression: take continuous data and figure out a best fit line to that data
import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

#print(df.head())

# the margin of high and low tell us a little bit about volatility for the day
# let's do the high minus the low percent is like the percent volatility [波动率]
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0 # percent volatility 波动率百分比
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0 # percent volatility 波动率百分比

df = df[['Adj. Close','HL_PCT']]