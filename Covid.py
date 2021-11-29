# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 22:08:32 2021

@author: Usuario
"""

import pandas as pd
url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

"""
Número de casos de Contagiados en el País.
"""
 n_casos = data.shape[0]
print(f'El numero de contagiado en Colombi es de: {n_casos}')
