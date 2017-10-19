#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:26:07 2017
@author: raimundoabrillopez

This file reads the export csv from typeform and transforms it in a file with the same structure
we use to generate calendars. You need to have your temporada-alimentos-report.csv in the raw folder.
Writes different calendar files to ../data/calendario/, one per answer.

To be improved> Add header with geodata.

"""
# Do the imports

import os
import pandas as pd
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Get paths

currentPWD = os.getcwd()
dwd = currentPWD[:-7]+'data/raw/'
aux = currentPWD[:-7]+'data/aux/'
cwd = currentPWD[:-7]+'data/calendario/'
hwd = currentPWD[:-7]+'data/'

#Get typeform file

os.chdir(dwd)
files = os.listdir(dwd)

data = pd.read_csv('temporada-alimentos-report.csv', encoding ='utf-8',index_col=1)
data.fillna(0,inplace=True)
data.drop('#',axis = 1,inplace=True)
data.drop('Fecha de entrada (UTC)',axis = 1,inplace=True)
data.drop('Fecha de envío (UTC)',axis = 1,inplace=True)
data.drop('Network ID',axis = 1,inplace=True)
data.drop('Puntúa esta web',axis = 1,inplace=True)
data.drop('¿Tienes comentarios?',axis = 1,inplace=True)

data.index.name='Producto'

# Generate valid column names
col_names = []

for i in range(int(len(data.columns)/12)):
    col_names.append('Ene.'+str(i))
    col_names.append('Feb.'+str(i))
    col_names.append('Mar.'+str(i))
    col_names.append('Abr.'+str(i))
    col_names.append('May.'+str(i))
    col_names.append('Jun.'+str(i))
    col_names.append('Jul.'+str(i))
    col_names.append('Ago.'+str(i))
    col_names.append('Sep.'+str(i))
    col_names.append('Oct.'+str(i))
    col_names.append('Nov.'+str(i))
    col_names.append('Dic.'+str(i))

# Transpose and map names to soydetemporada

data.columns = col_names
data = data.transpose()
names = pd.read_csv(aux+'typeform_names.csv',encoding ='utf-8',header=0,index_col=0)
data['_PRODUCTO']= data.index.map(lambda x: x.split('.')[1])
data['_Mes']= data.index.map(lambda x: x.split('.')[0])

# Assign X to answers

for column in data.columns.tolist()[:-2]:
    data[column] = data[column].apply(lambda x: 'X' if x else None)

data['_PRODUCTO'] = data['_PRODUCTO'].astype('int64')
data['_PRODUCTO'] = data['_PRODUCTO'].apply(lambda x: names.loc[x])
names.set_index('Producto',inplace=True)

os.chdir(cwd)

# Generate answer file per user, filtering and pivoting table.

for column in data.columns.tolist()[:-2]:
    datos = pd.DataFrame(index=data.index, data=data._Mes)
    datos['_PRODUCTO'] = data['_PRODUCTO']
    datos['Valor']= data[column]
    #datos['ID'] = datos['TIPO DE PRODUCTO'].apply(lambda x: names.loc[x])
    datos = datos.pivot(index='_PRODUCTO', columns='_Mes', values='Valor')
    datos.columns = ['ABR','AGO','DIC','ENE','FEB','JUL','JUN','MAR','MAY','NOV','OCT','SEP']
    datos['ID'] = names.CAL
    datos['TIPO DE PRODUCTO'] = names.index
    datos.set_index('ID',inplace=True)
    cols = datos.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    datos = datos[cols]
    cols = ['TIPO DE PRODUCTO', 'ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']
    datos = datos[cols]
    datos.to_csv(column+'.csv', encoding='utf-8')
