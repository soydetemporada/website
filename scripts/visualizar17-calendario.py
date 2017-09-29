import os
import pandas as pd
import numpy as np


YLIM = 0.3
XLIM = 0.5

dwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/temporadas/'
aux = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/aux/'
pwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/calendario/'
os.chdir(pwd)
files = os.listdir()
filesCSV = []
for file in files:
    if file.endswith('csv'):
        filesCSV.append(file)

dataList = []
data = pd.DataFrame()
for file in filesCSV:
    data = pd.read_csv(file, encoding ='utf-8', delimiter = ',',index_col=0)
    data['Ciudad'] = file.split('.')[0]
    dataList.append(data)
data = pd.concat(dataList)
data.fillna(0, inplace=True)

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

data['SCORE']=data.ENE+data.FEB+data.MAR+data.ABR+data.MAY+data.JUN+data.JUL+data.AGO+data.SEP+data.OCT+data.NOV+data.DIC

data = data.loc[data.SCORE>0]

pivot = data.groupby(data.index).mean()

pivot = pivot.round(2)

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

names = pd.read_csv(aux+'ID_name.csv', encoding ='utf-8', delimiter = ',', index_col=0)
serie = pd.Series(pivot.index.values)
serie = serie.map(names.NAME)
pivot.index = serie
pivot.index.name = 'PRODUCTO'
pivto = pivot.sort_index(inplace=True)
pivot.to_csv(dwd+'calendario_py.csv',encoding='utf-8')



