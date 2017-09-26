
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
import numpy as np
get_ipython().magic('matplotlib inline')
matplotlib.style.use('ggplot')
import datetime
import locale
import time
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


# In[2]:

product = input('Producto: ')+'/'
tipo = 'production/'
pwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/producto/'
aux = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/aux/'


# In[3]:

products = os.listdir(pwd)


# In[4]:

os.chdir(pwd+product+'/'+tipo)
files = os.listdir()
files


# In[5]:

data = pd.read_excel(files[1],skiprows=[0,1,2,3,4,5,6,7], encoding ='utf-8')
data.fillna(0,inplace=True)


# In[6]:

data.head(2)


# In[7]:

data[data.columns[0]]


# In[8]:

data = pd.DataFrame([data[data.columns[0]], data[data.columns[-1]]]).transpose()


# In[9]:

data.head(10)


# In[10]:

data.columns = ['Provincia','P-t']


# In[11]:

data = data.loc[data.Provincia!=0]
data = data.loc[data['Provincia'] != ' GALICIA']
data = data.loc[data['Provincia'] != ' PAÍS VASCO']
data = data.loc[data['Provincia'] != ' ARAGÓN']
data = data.loc[data['Provincia'] != ' CATALUÑA']
data = data.loc[data['Provincia'] != ' CASTILLA Y LEÓN']
data = data.loc[data['Provincia'] != ' CASTILLA-LA MANCHA']
data = data.loc[data['Provincia'] != ' C. VALENCIANA']
data = data.loc[data['Provincia'] != ' EXTREMADURA']
data = data.loc[data['Provincia'] != ' ANDALUCÍA']
data = data.loc[data['Provincia'] != ' CANARIAS']
data = data.loc[data['Provincia'] != ' C. VALENCIANA']
data = data.loc[data['Provincia'] != 'ESPAÑA']
#data = data.loc[data['Provincia'] != 'Las Palmas']
#data = data.loc[data['Provincia'] != 'S.C. de Tenerife']


# In[12]:

provincias = pd.read_csv(aux+'provincias.csv', delimiter='\t',index_col=1)


# In[13]:

data.Provincia = data.Provincia.apply(lambda x: x.upper())


# In[14]:

data['INE'] = data.Provincia.map(provincias.ID)


# In[15]:

data


# In[16]:

data.replace('–',0,inplace=True)


# In[17]:

provincias_name = provincias = pd.read_csv(aux+'provincias_nombre.csv',index_col=1)


# In[18]:

data.Provincia = data.INE.map(provincias_name.ID)


# In[19]:

datos = data.sort_values('P-t',ascending=False).head(1)


# In[30]:

datos.head()


# In[21]:

datos.to_csv(pwd+product+tipo+'principal_provincia_peninsula.csv',encoding='utf-8')


# In[22]:

#data = data.loc[data.index<73]


# In[56]:

data.sort_values('P-t',ascending=False,inplace=True)


# In[57]:

head = data[:3]
tail = data[3:]


# In[66]:

tail = pd.DataFrame(tail.sum()).transpose()
tail.Provincia = 'Otros'
tail.INE = 0
tail


# In[70]:

grafico = pd.concat([head,tail])


# In[81]:

grafico.set_index('Provincia',inplace=True)


# In[87]:

grafico['Percent'] = grafico['P-t']/sum(grafico['P-t'])*100


# In[91]:

grafico.to_csv(pwd+product+tipo+'grafico.csv', encoding='utf-8')


# In[88]:

grafico['Percent'].plot('barh')


# In[23]:

data.to_csv(pwd+product+tipo+'production_ready_INE.csv', encoding='utf-8')


# In[24]:

data


# In[292]:

dataMelt = pd.melt(data, id_vars='Provincia', value_vars=['S-ha_15/12-15/4','P-t_15/12-15/4','S-ha_15/4-15/6','P-t_15/4-15/6','S-ha_15/6-15/9','P-t_15/6-15/9','S-ha_15/9-15/1','P-t_15/9-15/1'])


# In[293]:

dataMelt['Unit'] = dataMelt['variable']
dataMelt['Unit'] = dataMelt['Unit'].apply(lambda x: x.split('_')[0])
dataMelt['variable'] = dataMelt['variable'].apply(lambda x: x.split('_')[1])


# In[294]:

dataMelt.columns =['Provincia', 'Variable', 'Cantidad', 'Unit']


# In[295]:

dataMelt['nonumeric'] = dataMelt.Cantidad.apply(lambda x: isinstance(x, int))


# In[296]:

dataMelt = dataMelt.loc[dataMelt.nonumeric == True]


# In[297]:

dataMelt.drop('nonumeric', axis=1, inplace=True)


# In[298]:

dataMelt.to_csv(product+'_production_ready_melt.csv', encoding='utf-8')


# In[299]:

dataMelt['Cantidad'] = dataMelt['Cantidad'].astype('int')*1000.0


# In[300]:

dataMelt.pivot_table(index='Variable', values='Cantidad', aggfunc='sum').Cantidad.plot('bar')


# In[301]:

dataMelt.info()


# In[ ]:



