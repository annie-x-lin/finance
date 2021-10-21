# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:44:23 2021

@author: annie
"""

#%% Importing Packages
import pandas as pd
import numpy as np

#%%
data = pd.read_csv("stock_prices_latest.csv",parse_dates=["date"],index_col="date")
del data["open"]
del data["high"]
del data["close_adjusted"]
del data["low"]
del data["volume"]
del data["split_coefficient"]
#%%
esp = pd.read_csv("earnings_latest.csv",parse_dates=["date"],index_col="date")
del esp["qtr"]
del esp["eps_est"]
del esp["release_time"]
#%%
stocks = list(data["symbol"].unique())
#%%
mylist=[]
faulty=[]
mylist2=[]
for i in stocks:
    try:
        dummy = data.groupby("symbol").get_group(i).merge(esp.groupby("symbol").get_group(i), how="outer", left_index=True, right_index=True).fillna(method="ffill").dropna()
        dummy=dummy.loc[dummy.index.is_quarter_end]
        mylist.append(dummy["close"].corr(dummy["eps"]))
        dummy["close1"]=dummy["close"].pct_change()
        dummy["eps1"]=dummy["eps"].pct_change()
        dummy=dummy.dropna()
        mylist.append(dummy["close1"].corr(dummy["eps1"]))
    except:
        faulty.append(i)
        
