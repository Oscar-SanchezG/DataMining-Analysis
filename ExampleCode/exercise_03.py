# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:59:19 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para la varible
de intervalo/razon, obtener una grafica de dispersion natural y otra ordenada 
"""

import matplotlib.pyplot as plt
import pandas as pd

def summary(df, var):
    vals = df[var].tolist()
    n = len(vals)
    index = list(range(n))
    #Dispersion natural
    plt.figure()
    plt.scatter(index, vals)
    plt.title(f'{var}')
    #Dispersion ordenada
    vals.sort()
    plt.figure()
    plt.scatter(index, vals)
    plt.title(f'{var}')

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Lista de intervalo y razon
# in-ter-v[a]-lo -- Palabra grave
# in-ter-va-lo --> INCORRECTO

l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']

for v in l_v:
    print(f'***** {v} *****')
    summary(df, v)
    print('****************')
    