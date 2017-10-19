#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:26:07 2017
@author: raimundoabrillopez

This file reads the csv files located in ../data/calendario, cleans and organize them
and then apply a mean so an "average" calendar is obtained.

Writes a calendario_py file that must get the _py trimmed after revision.

To be improved> Generate different calendars depending on geoData.

"""

# Do the imports
import os
import pandas as pd

#Set limits for mapping, Y corresponds to Warning Zone and X full production.
#Trigger for function, if weight more than this value, will assign Y or X.

YLIM = 0.3
XLIM = 0.5

# Get paths

currentPWD = os.getcwd()
dwd = currentPWD[:-7]+'data/temporadas/'
aux = currentPWD[:-7]+'data/aux/'
pwd = currentPWD[:-7]+'data/calendario/'

# List calendar files available

os.chdir(pwd)
files = os.listdir()
filesCSV = []
for file in files:
    if file.endswith('csv'):
        filesCSV.append(file)

# Create Dataframe from files

dataList = []
data = pd.DataFrame()
for file in filesCSV:
    data = pd.read_csv(file, encoding ='utf-8', delimiter = ',',index_col=0)
    data['Ciudad'] = file.split('.')[0]
    dataList.append(data)
data = pd.concat(dataList)
data.fillna(0, inplace=True)

# Find differences of x,X,y,Y and assign y=0.5, x=1

weight = pd.read_csv(aux+'weight.csv', encoding ='utf-8', delimiter = ',', index_col=0)
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

data.fillna(0,inplace=True)

#Name columns

data['SCORE']=data.ENE+data.FEB+data.MAR+data.ABR+data.MAY+data.JUN+data.JUL+data.AGO+data.SEP+data.OCT+data.NOV+data.DIC

#Only use answers with values

data = data.loc[data.SCORE>0]

# Pivot table

pivot = data.groupby(data.index).mean()

pivot = pivot.round(2)

# Map according to limits

def mapear(x):
    if x > XLIM:
        return 'X'
    elif x > YLIM:
        return 'Y'
    else:
        return None

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


# Fix names
names = pd.read_csv(aux+'ID_name.csv', encoding ='utf-8', delimiter = ',', index_col=0)
serie = pd.Series(pivot.index.values)
serie = serie.map(names.NAME)
pivot.index = serie
pivot.index.name = 'PRODUCTO'
pivto = pivot.sort_index(inplace=True)

# Save to file
pivot.to_csv(dwd+'calendario_py.csv',encoding='utf-8')
