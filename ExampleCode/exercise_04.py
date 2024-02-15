# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 14:14:58 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y hacer una 
funcion para obtener el resumen de los cinco numeros (minimo, maximo, 1er
cuartil, mediana, 3er cuartil) para cada variable de tipo intervalo/razon.

sin utilizar imports, excepto pandas para leer los datos (exclusivamente)
"""
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

def percentil(values, p):
    pos = (len(values) -1) * p
    pl = mt.floor(pos)
    pu = mt.ceil(pos)
    return values[pl]+(values[pu]-values[pl])*p

def summary(df, var):
    values = df[var].tolist()
    n = len(values)
    index = list(range(n))
    #Dispersion natural
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    #Dispersion ordenada
    values.sort()
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    # Resumen de los cinco numeros
    mi = values[0]
    mx = values[-1]
    fq = percentil(values, 0.25)
    med = percentil(values, 0.50)
    tq = percentil(values, 0.75)
    print(f'Mínimo = {mi:.2f}')
    print(f'Máximo = {mx:.2f}')
    print(f'1er cuártil = {fq:.2f}')
    print(f'Mediana = {med:.2f}')
    print(f'3er cuártil = {tq:.2f}')
    # Boxplot
    plt.figure()
    plt.boxplot(values)
    plt.title(f'{var}')
    
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Lista de intervalo y razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
#l_v = ['semester']
# Iterar sobre la lista de variables
for v in l_v:
    print(f'***** {v} *****')
    summary(df, v)
    print('****************')
