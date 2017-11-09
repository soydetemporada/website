import pandas as pd
import os
import matplotlib.pyplot as plt
import datetime
import json

plt.style.use('ggplot')

currentPWD = os.getcwd()
#aux = currentPWD[:-7]+'data/aux/'
aux = '/Volumes/MacintoshHD/_GitHub/journey-of-food/data/aux/'
dwd = currentPWD[:-7]+'data/precios/'

#os.chdir(dwd)
os.chdir('/Volumes/MacintoshHD/_GitHub/journey-of-food/data/precios/')
fileList = [ f for f in os.listdir() if f.endswith(".tsv") ]

dataList = []
for file in fileList:
    data = pd.read_csv(file, delimiter='\t', header=None, decimal=',')
    year = file.split('_')[1]
    week = file.split('_')[2]
    data['Fecha'] = datetime.datetime.strptime(year+'-W'+week+'-0','%Y-W%W-%w')
    data.columns = ['Artículo','Unidades','Precio máximo semana actual','Precio frecuente semana actual','Precio mínimo semana actual','Precio frecuente semana anterior','Var. % semana anterior','Precio medio acumulado mes actual','Precio medio acumulado mes anterior','Var. %','Fecha']
    dataList.append(data)

data = pd.concat(dataList)
names = pd.read_csv(aux+'comercio_names.csv',index_col=0)
data.Artículo = data.Artículo.map(names.soydetemporada)
data.Fecha = data.Fecha.apply(lambda x: datetime.datetime.strftime(x,'%Y-%m'))

pivot = data.pivot_table(index='Artículo', columns = data.Fecha, values = 'Precio frecuente semana actual', aggfunc='mean').transpose()
pivot = pivot.round(2)
pivot = pivot.reset_index()
pivot.Fecha = pivot.Fecha.apply(lambda x: datetime.datetime.strptime(x+'-0','%Y-%m-%w'))
pivot.Fecha = pivot.Fecha.apply(lambda x: datetime.datetime.strftime(x,'%d-%m-%Y'))
pivot = pivot.set_index('Fecha')
pivot = pivot.round(2)
#dict(pivot.acelga.tail())

mydict = {}
for item in pivot.columns:
    mydict[item] = dict(pivot[item].tail(12))
#mydict

os.chdir('/Volumes/MacintoshHD/_GitHub/journey-of-food/_data/products/')
ficheros = [ f for f in os.listdir() if f.endswith(".json") ]
missing = []
for fichero in ficheros:
    name = fichero[:-5]
    print(name)
    with open(fichero, encoding = 'utf-8') as data_file:
        dataJson = json.load(data_file)
    data_file.close()

    try:
        dataJson['precio'] = mydict[name]
        with open(fichero, 'w', encoding='utf-8') as data_file:
            json.dump(dataJson,data_file,indent=4)
        data_file.close()

    except:
        missing.append(name)
print('Missing: {}'.format(missing))
