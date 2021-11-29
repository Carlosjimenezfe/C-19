# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:08:32 2021

@author: Usuario
"""

import pandas as pd
url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

"""
1. Número de casos de Contagiados en el País.
"""
n_Casos = data.shape[0]
print(f'El numero de casos de contagios en Colombia es de: {n_Casos}')


"""
2. Número de Municipios Afectados
"""
n_Municipio = len(data.groupby('Nombre municipio').size())
print(f'El numero de municipio afectado es de : {n_Municipio}')