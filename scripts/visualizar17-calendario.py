
# coding: utf-8

# In[1]:

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
get_ipython().magic('matplotlib inline')
matplotlib.style.use('ggplot')


# In[9]:

dwd = '/Volumes/Macintosh HD/_Github/journey-of-food/data/temporadas/'
aux = '/Volumes/Macintosh HD/_Github/journey-of-food/data/aux/'
pwd = '/Volumes/Macintosh HD/_Github/journey-of-food/data/calendario/'
os.chdir(pwd)
files = os.listdir()
filesCSV = []
for file in files:
    if file.endswith('csv'):
        filesCSV.append(file)


# In[10]:

dataList = []
data = pd.DataFrame()
for file in filesCSV:
    data = pd.read_csv(file, encoding ='utf-8', delimiter = ',', index_col=0)
    data['Ciudad'] = file.split('.')[0]
    dataList.append(data)
    
data = pd.concat(dataList)
data.fillna(0, inplace=True)


# In[11]:

data.ENE.unique()


# In[14]:

weight = pd.read_csv(aux+'weight.csv', encoding ='utf-8', delimiter = ',', index_col=0)


# In[15]:

data.loc[data['TIPO DE PRODUCTO'] == 'ACELGA']


# In[16]:

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


# In[17]:

data.fillna(0,inplace=True)


# In[18]:

data['SCORE'] = data.ENE+data.FEB+data.MAR+data.ABR+data.MAY+data.JUN+data.JUL+data.AGO+data.SEP+data.OCT+data.NOV+data.DIC


# In[19]:

data.head(10)


# In[20]:

data = data.loc[data.SCORE>0]


# In[21]:

data.head(3)


# In[22]:

pivot = data.groupby('TIPO DE PRODUCTO').mean()
pivot = pivot.round(2)


# In[23]:

pivot.head(5)


# In[24]:

pivot.transpose().UVA.plot('bar',ylim=[0,1])


# In[25]:

def mapear(x):
    if x > 0.5:
        return 'X'
    elif x > 0.3:
        return 'Y'
    else:
        return None


# In[26]:

pivot.ENE = pivot.ENE.apply(lambda x: mapear(x))
pivot.FEB = pivot.FEB.apply(lambda x: mapear(x))
pivot.MAR = pivot.MAR.apply(lambda x: mapear(x))
pivot.ABR = pivot.ABR.apply(lambda x: mapear(x))
pivot.MAY = pivot.MAY.apply(lambda x: mapear(x))
pivot.JUN = pivot.JUN.apply(lambda x: mapear(x))
pivot.JUL = pivot.JUL.apply(lambda x: mapear(x))
pivot.AGO = pivot.AGO.apply(lambda x: mapear(x))
pivot.SEP = pivot.SEP.apply(lambda x: mapear(x))
pivot.OCT = pivot.OCT.apply(lambda x: mapear(x))
pivot.NOV = pivot.NOV.apply(lambda x: mapear(x))
pivot.DIC = pivot.DIC.apply(lambda x: mapear(x))


# In[27]:

pivot


# In[28]:

pivot.to_csv(dwd+'calendario_py.csv')


# In[ ]:




# In[ ]:




# In[ ]:



