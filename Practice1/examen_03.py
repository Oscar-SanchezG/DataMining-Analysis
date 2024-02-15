# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:28:49 2021

@author: ivand

@3. Utilizando el mismo archivo de salarios, hacer un programa en Python que
    para cada puesto de trabajo tome el subconjunto de variables con salary, 
    hours_worked y days_worked, de tal forma que cada puesto de trabajo pueda
    representar un punto en un espacio 3D. Despues, debe calcular la distancia 
    euclideana entre cada par posible de puntos. La salida debe ser una lista 
    de listas de nxn con las distancias (n = numero de puestos de trabajo en
    la lista).
"""

import pandas as pd
import math as mt
def euc_dist(p, q):
    d = [(pi - qi)**2 for pi, qi in zip(p, q)]
    d = sum(d)
    d = mt.sqrt(d)
    return d

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

sal_filter = df['salary'] > 20000

sal_coord = df[sal_filter]['salary'].tolist()
hor_coord = df[sal_filter]['hours_worked'].tolist()
day_coord = df[sal_filter]['days_worked'].tolist()

data_points = [(x, y, z) for x, y, z in zip(sal_coord, hor_coord, day_coord)]

n = len(data_points)

m_d = []
for i in range(n):
    t = [0 for j in range(n)]
    m_d.append(t)
    
for i in range(n-1):
    for j in range(i+1, n):
        d = euc_dist(data_points[i], data_points[j])
        m_d[i][j] = d
        m_d[j][i] = d
        
print(m_d)
