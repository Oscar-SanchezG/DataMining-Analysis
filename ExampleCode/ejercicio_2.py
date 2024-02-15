# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:32:02 2021

@author: EDUARDO

@Description:
2. Con el mismo archivo del punto anterior escribe un programa en Python que: 
a. Transforme la variable salary a una variable binaria, considerando sueldos altos o 
bajos. Un salario bajo es aquel menor o igual 10000, el alto es mayor a 10000. 
b. Transforme la variable hours_worked en una variable binaria, considerando tiempo 
completo o tiempo parcial, el tiempo parcial es menor o igual a 6 horas, el tiempo 
completo es mayor a 6 horas 
c. Genere una tabla de contingencia con estas dos variables como se muestra a 
continuación (los números son ficticios)
d. Calcule el coeficiente Q de Yule, definido como

"""

import pandas as pd

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def q_yule(c_t):
     ad = (c_t[1][1]*c_t[0][0]) - (c_t[1][0]*c_t[0][1])
     bc = (c_t[1][1]*c_t[0][0]) + (c_t[1][0]*c_t[0][1])
     print(ad)
     print(bc)
     qy = (ad - bc)/(ad + bc)
     return qy

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'salaries.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

sal = df['salary'].tolist()
sal = [0 if m <= 10000 else m for m in sal] # 0 para bajo
sal = [1 if m > 10000 else m for m in sal] # 1 para alto

hw = df['hours_worked'].tolist()
hw = [0 if m <= 6 else m for m in hw] # 0 tiempo parcial
hw = [1 if m > 6 else m for m in hw] # 1 tiempo completo


c_t = contingency_table(hw, sal)
qy = q_yule(c_t)
print(f'Coeficiente Q = {qy:.3f}')

