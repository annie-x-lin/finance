# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:07:44 2021

@author: annie
"""
#%%

deal_value="$123,456,789"
deal_value=deal_value.strip("$")
list1=deal_value.split(",")
deal_value="".join(list1)

#%%
grades={'Bob':71, 'Alice':65, 'Jim':70, 'Jen':90, 'Tim':86, 'Trish':85, 'Tony':75}

letter_Grades={}
for key in grades.keys():
    x = grades[key]
    if x > 90:
        letter_Grades[key]="A+"
    elif x > 80:
        letter_Grades[key]="A"
    else:
        letter_Grades[key]="B"
        
print (letter_Grades)

#%%
mylist=['A', 'B','D', 'C', 'D', 'D', 'D']
while "D" in mylist:
    mylist.remove('D')
for x in mylist:
    if x == 'D':
        mylist.remove(x)
        
#%%
tickers={'AAPL':100.0, 'CAT':50.0, 'MSFT':150}
import numpy as np
output1="${:.2f}"
def function1(tick):
    price={}
    for key in tick.keys():
        var1=np.random.normal(tick[key],1,5)
        var2=[]
        for x in range(0,len(var1)):
            var2.append(output1.format(var1[x]))
        price[key]=var2
    print(price)

function1(tickers)

#%%
list3=[]
for x in range (0,25):
        x = np.random.randint(1,6)
        y=np.random.randint(1,6)
        list4=np.random.normal(x,y,60)
        list3.append(list4)
arr1=np.array(list3)
arr1=arr1.transpose()
covarianceM=np.cov(arr1)
covarianceI=np.linalg.inv(covarianceM)
lol=np.dot(covarianceM ,covarianceI)


#%% 
import pandas as pd
sp500=pd.read_csv("StockData/sp500.csv")
dfs = pd.read_html("https://www.iposcoop.com/last-100-ipos/")

sales = [100,200,300]
cos=['A','B','C']
coData= {"Company":cos,"Sales":sales}
df = pd.DataFrame(coData)

