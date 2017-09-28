
import os
import pandas as pd
import numpy as np

product = 'acelga/'
pro = 'production/'
imp = 'import/'
pwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/producto'
aux = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/aux/'
dwd = '/Volumes/Macintosh HD/_GitHub/journey-of-food/data/source/'


os.chdir(dwd)
files = os.listdir(dwd)

dataOrg = pd.read_excel(files[-2], sheetname='2015', encoding ='utf-8',skiprows=[2],index_col=0,na_values='x')
data = dataOrg.fillna(0)


data.drop('%cuota',axis=0,inplace=True)
data.drop('TOTAL HORTALIZAS',axis=0,inplace=True)
data.drop('OTRAS HORTALIZAS',axis=0,inplace=True)
data.drop('OTROS CÍTRICOS',axis=0,inplace=True)
data.drop('OTRAS FRUTAS',axis=0,inplace=True)
data.drop('TOTAL FRUTAS',axis=0,inplace=True)
data.drop('TOTAL F. Y H.',axis=0,inplace=True)
data.drop('TOTAL',axis=1,inplace=True)
data.drop('TOTAL UE-27',axis=1,inplace=True)
data.drop('T. HORTALIZAS',axis=0,inplace=True)
data.drop('* Datos provisionales',axis=0,inplace=True)


data = data.loc[pd.notnull(data.index)]


data.index = [x.lower() for x in data.index.values.tolist()]

for producto in data.index.values:
    datos = data.loc[data.index==producto].transpose().sort_values(producto,ascending=False)
    datos.columns = ['Importado']
    datos[:3].to_csv(pwd+producto+'.csv')
    datos = pd.DataFrame(datos.sum())
    datos.columns = ['P-t']
    datos.to_csv(pwd+producto+'_total.csv')