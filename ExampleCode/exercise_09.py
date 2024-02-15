# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:51:59 2021

@author: EDUARDO

@Description: Hacer una funcion que calcule el coeficiente de correlacion de
Perarson para dos variables. Pasar como paremetros las listas de valores para
cada variable.

leer el archivo con los datos de los estudiantes y para cada par de las 
variables intervalo/razon calcular el coeficiente de correlación.

def coef_pearson(values_1, values_2)
    return coef_pearson

                            sumatoria((x_i - x_md)(y_i - y_md))
r = ------------------------------------------------------------------------
    (raizcuadrada(sumatoria((x_i - x_md)^2)raizcuadrada(sumatoria(y_i - y_md)^2)))
"""

import pandas as pd
import math as mt

def coef_pearson(values_1, values_2):
    mx = sum(values_1)/len(values_1)
    my = sum(values_2)/len(values_2)
    num = sum([(x - mx)*(y - my) for x,y in zip(values_1, values_2)])
    den_1 = mt.sqrt(sum([(x - mx)**2 for x in values_1]))
    den_2 = mt.sqrt(sum([(y - my)**2 for y in values_2]))
    den = den_1 * den_2
    r = num/den
    return r

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Compute the correlation between two variables
#v_1 = 'height'
#v_2 = 'weight'
#values_1 = df[v_1].tolist()
#values_2 = df[v_2].tolist()
#r = coef_pearson(values_1, values_2)
#print(f'Coeficiente de Pearson para "{v_1}" y "{v_2}" = {r:.3f}')
#df.plot(x=v_1, y=v_2, kind='scatter')

#Compute correlation between every two pair of variables
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']

for v_1 in l_v:
    for v_2 in l_v:
        df.plot(x=v_1, y=v_2, kind='scatter')
        values_1 = df[v_1].tolist()
        values_2 = df[v_2].tolist()
        r = coef_pearson(values_1, values_2)
        #print(f'Coeficiente de Pearson para "{v_1}" y "{v_2}" = {r:.3f}')

# With pandas
print(df.corr()) #coeficiente pearson








