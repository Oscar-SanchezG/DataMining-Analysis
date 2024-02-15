# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 00:56:48 2021

@author: EDUARDO

@Description: Leer el archivo con los datos de los estudiantes y para las 
variables de intervalo/razon: edad, altura, peso, semestre, num_cursos

discretizar los valores en n grupos (p. ejem. n = 3)

Generar la tabla de contingencia para cada par de variables utilizando sus grupos.

[edad, altura]
[edad, peso]
[edad, semestre]
...

lista_1 = [1.75, 1.63, 1.89, 1.66, 1.72, 1.65, 1.80, 1.77, 1.71]
grouplist_1 = [2, 1, 1, 2, 3, 1, 2, 1, 2, 2]

lista_2 = [1.75, 1.63, 1.89, 1.66, 1.72, 1.65, 1.80, 1.77, 1.71]
grouplist_1 = [3, 1, 1, 2, 2, 1, 2, 1, 2, 2]

                altura
        peso / 1 / 2 / 3 /
        --------------
        1   / 1 / 0 / 1 /
        2   / 1 / 2 / 1 /
        3   / 1 / 1 / 1 /

"""

import pandas as pd

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def grouping(values, n):
    mn = min(values)
    rang = max(values) - mn
    inter = rang / n
    ul = mn + inter
    d = {}
    for i in range(n):
        d[ul] = i
        ul += inter
        
    l = []
    for v in values:
        for t in d:
            if v <= t:
                l.append(d[t])
                break
    return l, d

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Lista de variables intervalo/razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['age', 'height']

for i in range(len(l_v)-1):
    for j in range(i+1, len(l_v)):
        values_1 = df[l_v[i]].tolist()
        values_2 = df[l_v[j]].tolist()
        values_1, r_1 = grouping(values_1, 3)
        values_2, r_2 = grouping(values_2, 3)
        c_t = contingency_table(values_1, values_2)
        print(r_1)
        print(r_2)
        print(f'[{l_v[i]}, {l_v[j]}]', c_t)











