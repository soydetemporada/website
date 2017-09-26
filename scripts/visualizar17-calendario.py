
# coding: utf-8

# In[95]:

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
get_ipython().magic('matplotlib inline')
matplotlib.style.use('ggplot')


# In[96]:

pwd = '/Volumes/Macintosh HD/_Drive/journey-of-food/data/calendario/'
os.chdir(pwd)
files = os.listdir()
filesCSV = []
for file in files:
    if file.endswith('csv'):
        filesCSV.append(file)


# In[97]:

dataList = []
data = pd.DataFrame()
for file in filesCSV:
    data = pd.read_csv(file, encoding ='utf-8', delimiter = ',', index_col=0)
    dataList.append(data)
    
data = pd.concat(dataList)
data.fillna(0, inplace=True)


# In[98]:

data.ENE.unique()


# In[99]:

weight = pd.read_csv(pwd+'aux/weight.csv', encoding ='utf-8', delimiter = ',', index_col=0)


# In[100]:

data.loc[data['TIPO DE PRODUCTO'] == 'ACELGA']


# In[101]:

data.ENE = data.ENE.map(weight.score) 
data.FEB = data.FEB.map(weight.score) 
data.MAR = data.MAR.map(weight.score) 
data.ABR = data.ABR.map(weight.score) 
data.MAY = data.MAY.map(weight.score) 
data.JUN = data.JUN.map(weight.score) 
data.JUL = data.JUL.map(weight.score) 
data.AGO = data.AGO.map(weight.score) 
data.SEP = data.SEP.map(weight.score) 
data.OCT = data.OCT.map(weight.score)
data.NOV = data.NOV.map(weight.score) 
data.DIC = data.DIC.map(weight.score) 


# In[102]:

data.fillna(0,inplace=True)


# In[103]:

data['SCORE'] = data.ENE+data.FEB+data.MAR+data.ABR+data.MAY+data.JUN+data.JUL+data.AGO+data.SEP+data.OCT+data.NOV+data.DIC


# In[104]:

data.head(10)


# In[105]:

data = data.loc[data.SCORE>0]


# In[106]:

data.head(10)


# In[107]:

pivot = data.groupby('TIPO DE PRODUCTO').mean()
pivot = pivot.round(2)


# In[108]:

pivot


# In[109]:

pivot.columns = [1,2,3,4,5,6,7,8,9,10,11,12,'SCORE']


# In[110]:

pivot.transpose().UVA.plot('bar',ylim=[0,1])


# In[111]:

pivot.to_csv(pwd+'results/full.csv')

