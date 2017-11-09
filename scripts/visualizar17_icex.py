import os
import pandas as pd
import numpy as np
import datetime
import locale
import time
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
import glob

icex = '/icex/'
pwd = '/Volumes/MacintoshHD/_GitHub/journey-of-food/data/products/'
aux = '/Volumes/MacintoshHD/_GitHub/journey-of-food/data/aux/'
dwd = '/Volumes/MacintoshHD/_GitHub/journey-of-food/data/raw/'

for product in os.listdir(pwd)[1:]:
    try:
        os.chdir(pwd+product+icex)
        datos = pd.read_csv('icex.csv', header=None, skiprows=2, delimiter=';', index_col=0)
        datos = datos.transpose()
        datos.columns=['01-Ene-2015','01-Feb-2015','01-Mar-2015','01-Abr-2015','01-May-2015','01-Jun-2015','01-Jul-2015','01-Ago-2015','01-Sep-2015','01-Oct-2015','01-Nov-2015','01-Dic-2015']
        datos = datos.transpose()
        datos.columns = ['Exportado','Importado']
        datos.index.name = 'Mes'
        datos[['Importado','Exportado']].to_csv(pwd+product+'/'+product+'_import_export_mes.csv')
    except:
        pass
