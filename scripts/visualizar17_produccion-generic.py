
# coding: utf-8

# In[430]:

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


# In[1106]:

product = 'acelga'
tipo = 'production/'
pwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/producto/'
aux = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/aux/'


# In[1107]:

tipos = os.listdir(pwd)[1:]


# In[1108]:

dropdown = ipywidgets.Dropdown(
    options = tipos,
    value = 'ajo')
display(dropdown)

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print("changed to %s" % change['new'])
dropdown.observe(on_change)


# In[1841]:

product = dropdown.value
productPATH = product + '/'


# In[1842]:

products = os.listdir(pwd)
os.chdir(pwd+productPATH+tipo)
files = glob.glob(pwd+productPATH+tipo+'*.xlsx')
files


# In[1845]:

data = pd.read_excel(files[0],skiprows=[0,1,2,3,4,5], encoding ='utf-8')
data.fillna(0,inplace=True)


# In[1846]:

data.head(2)


# In[1847]:

data[data.columns[0]].head()


# In[1848]:

data = pd.DataFrame([data[data.columns[0]], data[data.columns[-1]]]).transpose()


# In[1849]:

data.head()


# In[1850]:

data.columns = ['Provincia','P-t']


# In[1851]:

data.Provincia.unique()


# In[1852]:

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
data = data.loc[data['Provincia'] != 'Las Palmas']
data = data.loc[data['Provincia'] != 'S.C. de Tenerife']


# In[1853]:

data['P-t'].replace('–',0,inplace=True)
data.head()


# In[1854]:

provincias = pd.read_csv(aux+'provincias.csv', delimiter='\t',index_col=1)


# In[1855]:

data.Provincia = data.Provincia.apply(lambda x: x.upper())


# In[1856]:

data.sort_values('P-t',ascending=False).head(1)


# In[1857]:

data['INE'] = data.Provincia.map(provincias.ID)


# In[1858]:

data.sort_values('P-t',ascending=False).head(1)


# In[1859]:

provincias_name = provincias = pd.read_csv(aux+'provincias_nombre.csv',index_col=1)


# In[1860]:

data.Provincia = data.INE.map(provincias_name.ID)


# In[1861]:

datos = data.sort_values('P-t',ascending=False).head(1)


# In[1862]:

datos.head()


# In[1863]:

datos.to_csv(pwd+productPATH+tipo+'principal_provincia_peninsula.csv',encoding='utf-8')


# In[1864]:

#data = data.loc[data.index<73]


# In[1865]:

data.sort_values('P-t',ascending=False,inplace=True)


# In[1866]:

head = data[:3]
tail = data[3:]


# In[1867]:

tail = pd.DataFrame(tail.sum()).transpose()
tail.Provincia = 'Otros'
tail.INE = 0
tail.head()


# In[1868]:

grafico = pd.concat([head,tail])


# In[1869]:

grafico.set_index('Provincia',inplace=True)


# In[1870]:

grafico['Percent'] = grafico['P-t']/sum(grafico['P-t'])*100.00
grafico.Percent = grafico.Percent.astype('float')
grafico.Percent = grafico.Percent.round(2)
grafico.head()


# In[1871]:

grafico.to_csv(pwd+productPATH+tipo+'grafico.csv', encoding='utf-8')


# In[1872]:

grafico['Percent'].plot('barh')
plt.xlabel('Percent')
plt.savefig(product+'.png')


# In[1873]:

data.to_csv(pwd+productPATH+tipo+'production_ready_INE.csv', encoding='utf-8')


# In[1874]:

data.head()


# In[1875]:

total = pd.DataFrame(pd.DataFrame(data.sum()).transpose())
total.Provincia = 'España'
total.INE = 0
total


# In[1876]:

total.to_csv(pwd+productPATH+tipo+'total.csv', encoding='utf-8')


# In[1877]:

#dataMelt = pd.melt(data, id_vars='Provincia', value_vars=['S-ha_15/12-15/4','P-t_15/12-15/4','S-ha_15/4-15/6','P-t_15/4-15/6','S-ha_15/6-15/9','P-t_15/6-15/9','S-ha_15/9-15/1','P-t_15/9-15/1'])


# In[1701]:

#dataMelt['Unit'] = dataMelt['variable']
#dataMelt['Unit'] = dataMelt['Unit'].apply(lambda x: x.split('_')[0])
#dataMelt['variable'] = dataMelt['variable'].apply(lambda x: x.split('_')[1])


# In[ ]:

#dataMelt.columns =['Provincia', 'Variable', 'Cantidad', 'Unit']


# In[ ]:

#dataMelt['nonumeric'] = dataMelt.Cantidad.apply(lambda x: isinstance(x, int))


# In[ ]:

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



