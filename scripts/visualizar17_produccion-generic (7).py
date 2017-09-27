
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
import glob

import ipywidgets
from IPython.display import display


# In[2]:

product = 'acelga'
tipo = 'production/'
pwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/producto/'
aux = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/aux/'


# In[3]:

tipos = os.listdir(pwd)[1:]


# In[4]:

dropdown = ipywidgets.Dropdown(
    options = tipos,
    value = 'ajo')
display(dropdown)

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print("changed to %s" % change['new'])
dropdown.observe(on_change)


# In[269]:

product = dropdown.value
productPATH = product + '/'


# In[270]:

products = os.listdir(pwd)
os.chdir(pwd+productPATH+tipo)
files = glob.glob(pwd+productPATH+tipo+'*.xlsx')
files


# In[277]:

data = pd.read_excel(files[0],skiprows=[0,1,2,3,4,5,6], encoding ='utf-8')
data.fillna(0,inplace=True)


# In[278]:

data.head(2)


# In[279]:

data[data.columns[0]].head()


# In[280]:

data = pd.DataFrame([data[data.columns[0]], data[data.columns[-1]]]).transpose()


# In[281]:

data.head()


# In[282]:

data.columns = ['Provincia','P-t']


# In[283]:

data.Provincia.unique()


# In[284]:

data = data.loc[data.Provincia!=0]
data = data.loc[data['Provincia'] != ' GALICIA']
data = data.loc[data['Provincia'] != ' PAÍS VASCO']
data = data.loc[data['Provincia'] != ' PAIS VASCO']
data = data.loc[data['Provincia'] != ' ARAGÓN']
data = data.loc[data['Provincia'] != ' ARAGON']
data = data.loc[data['Provincia'] != ' CATALUÑA']
data = data.loc[data['Provincia'] != ' CASTILLA Y LEÓN']
data = data.loc[data['Provincia'] != ' CASTILLA Y LEON']
data = data.loc[data['Provincia'] != ' CASTILLA-LA MANCHA']
data = data.loc[data['Provincia'] != ' C. VALENCIANA']
data = data.loc[data['Provincia'] != ' EXTREMADURA']
data = data.loc[data['Provincia'] != ' ANDALUCÍA']
data = data.loc[data['Provincia'] != ' ANDALUCIA']
data = data.loc[data['Provincia'] != ' CANARIAS']
data = data.loc[data['Provincia'] != ' C. VALENCIANA']
data = data.loc[data['Provincia'] != 'ESPAÑA']
#data = data.loc[data['Provincia'] != 'Las Palmas']
#data = data.loc[data['Provincia'] != 'S.C. de Tenerife']


# In[285]:

data['P-t'].replace('–',0,inplace=True)
data.head()


# In[286]:

data.Provincia.values


# In[287]:

dataCanarias = data[(data.Provincia =='Las Palmas') | (data.Provincia == 'S.C. de Tenerife')]
data = data[(data.Provincia !='Las Palmas') & (data.Provincia != 'S.C. de Tenerife')]
dataCanarias.head()


# In[288]:

provincias = pd.read_csv(aux+'provincias.csv', delimiter='\t',index_col=1)


# In[289]:

data.Provincia = data.Provincia.apply(lambda x: x.upper())


# In[290]:

data.sort_values('P-t',ascending=False).head(1)


# In[291]:

data['INE'] = data.Provincia.map(provincias.ID)


# In[292]:

data.sort_values('P-t',ascending=False).head(1)


# In[293]:

provincias_name = provincias = pd.read_csv(aux+'provincias_nombre.csv',index_col=1)


# In[294]:

data.Provincia = data.INE.map(provincias_name.ID)


# In[295]:

datos = data.sort_values('P-t',ascending=False).head(1)


# In[296]:

datos.head()


# In[297]:

datos.to_csv(pwd+productPATH+tipo+'principal_provincia_peninsula.csv',encoding='utf-8')


# In[298]:

#data = data.loc[data.index<73]


# In[299]:

data.sort_values('P-t',ascending=False,inplace=True)


# In[300]:

head = data[:3]
tail = data[3:]


# In[301]:

tail = pd.DataFrame(tail.sum()).transpose()
tail.Provincia = 'Resto de España'
tail.INE = 0
tail.head()


# In[302]:

grafico = pd.concat([head,tail])


# In[303]:

grafico.set_index('Provincia',inplace=True)


# In[304]:

grafico['Percent'] = grafico['P-t']/sum(grafico['P-t'])*100.00
grafico.Percent = grafico.Percent.astype('float')
grafico.Percent = grafico.Percent.round(2)
grafico.head()


# In[305]:

grafico.to_csv(pwd+productPATH+tipo+'grafico.csv', encoding='utf-8')


# In[306]:

grafico['Percent'].plot('barh')
plt.xlabel('Percent')
plt.savefig(product+'.png')


# In[307]:

data.to_csv(pwd+productPATH+tipo+'production_ready_INE.csv', encoding='utf-8')


# In[308]:

data.head()


# In[309]:

total = pd.DataFrame(pd.DataFrame(data.sum()).transpose())
total.Provincia = 'España'
total.INE = 0
total.drop('INE',axis = 1, inplace=True)
total


# In[310]:

try:
    dataCanarias = pd.DataFrame(dataCanarias.sum()).transpose()
except:
    print('No datos canarias')


# In[311]:

dataCanarias.Provincia = 'Canarias'


# In[312]:

total = total.append(dataCanarias)


# In[313]:

total.set_index('Provincia',inplace=True)


# In[314]:

total.head()


# In[315]:

total.to_csv(pwd+productPATH+tipo+'total.csv', encoding='utf-8')


# In[316]:

#dataMelt = pd.melt(data, id_vars='Provincia', value_vars=['S-ha_15/12-15/4','P-t_15/12-15/4','S-ha_15/4-15/6','P-t_15/4-15/6','S-ha_15/6-15/9','P-t_15/6-15/9','S-ha_15/9-15/1','P-t_15/9-15/1'])


# In[171]:

#dataMelt['Unit'] = dataMelt['variable']
#dataMelt['Unit'] = dataMelt['Unit'].apply(lambda x: x.split('_')[0])
#dataMelt['variable'] = dataMelt['variable'].apply(lambda x: x.split('_')[1])


# In[172]:

#dataMelt.columns =['Provincia', 'Variable', 'Cantidad', 'Unit']


# In[173]:

#dataMelt['nonumeric'] = dataMelt.Cantidad.apply(lambda x: isinstance(x, int))


# In[174]:

#dataMelt = dataMelt.loc[dataMelt.nonumeric == True]


# In[ ]:

#dataMelt.drop('nonumeric', axis=1, inplace=True)


# In[ ]:

#dataMelt.to_csv(product+'_production_ready_melt.csv', encoding='utf-8')


# In[ ]:

#dataMelt['Cantidad'] = dataMelt['Cantidad'].astype('int')*1000.0


# In[ ]:

#dataMelt.pivot_table(index='Variable', values='Cantidad', aggfunc='sum').Cantidad.plot('bar')


# In[ ]:

#dataMelt.info()


# In[ ]:




# In[ ]:




# In[ ]:



