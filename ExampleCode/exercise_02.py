# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:31:09 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para cada varible
nominal, encontrar las frecuencias de cada valor y porcentaje. 
Imprimir los valores en orden decendente por porcentaje.

en cualquier variable, convierte los valores a minúsculas para evitar irregularidades.

Hacer una funcion que tome el nombre de una variable e imprima los datos y
genere las graficas.
p. ej. Salamanca --> salamanca
"""

import matplotlib.pyplot as plt
import pandas as pd

def summary(df, var):
    vals = df[var].tolist() #creo una lista
    d = {}  #Diccionario vacio
    n = 0
    for val in vals:
        for v in val.split('/'):
            v = v.lower().strip()
            d[v] = d.get(v, 0) + 1
            n += 1
        
    freqs = []
    for v,f in d.items():
        freqs.append((f, f/n*100, v))
        
    freqs.sort(reverse=True)
    lab =[]
    val =[]
    for f,p,v in freqs:
        print(f'{v}:{f}:{p:.2f}%')
        lab.append(v)
        val.append(f)
        
    plt.figure()
    plt.pie(val, labels=lab) #Grafica de pay
    plt.figure() #nueva figura sino ensima la graficas
    plt.bar(lab, val)

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#summary(df, 'sex')
#summary(df, 'city_origin')

# Lista de varibales nominales
l_v = ['name', 'sex', 'pet', 'city_origin', 'videogame_console']

for v in l_v:
    print(f'***** {v} *****')
    summary(df, v)
    print('****************')


