# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 02:30:54 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para las
variables nominales: genero, mascota y consola

Generar una tabla de contingencia entre cada par de variables:

[genero, consola]
[genero, mascota]
[consola, mascota]

en el caso de la mascota, transforma a valor binario (y/n). Todas
deben ser tablas de contingencia de 2x2

Calcular el test de chi cuadrada entre cada par de variables.

                var1
        var2 / 1 / 0 /
        ---------------------
        1   / x_1 / x_2 / x1*
        0   / x_3 / x_4 / x0*
        ---------------------
              x*1   x*0   n

x^2 = sumatoria(i=1)^k(x_i-m_i)^2/m_i
"""

import pandas as pd
import math as mt
from scipy.stats import chi2

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def chi_square(c_t, lab_1, lab_2):
    total = sum([sum([v1 for k1, v1 in v.items()]) for k, v in c_t.items()])
    chi = 0
    for r in lab_1:
        s_r = sum([sum([v1 for k1, v1 in v.items()]) 
                  for k, v in c_t.items() if k == r])               
        for c in lab_2:
            s_c = sum([sum([v1 for k1, v1 in v.items() if k1 == c])
                  for k, v in c_t.items()])
            ev = s_r*s_c/total
            ov = c_t[r][c]
            chi += ((ov -ev)**2)/ev
        
    return chi

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
chi = chi_square(c_t, ['h', 'm'], ['y', 'n'])
print(f'chi_square [sex, videogame_console]: {chi:.3f}')

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
chi = chi_square(c_t, ['h', 'm'], ['y', 'n'])
print(f'chi_square [sex, pet]: {chi:.3f}')

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[videogame_console, pet]:', c_t)
chi = chi_square(c_t, ['y', 'n'], ['y', 'n'])
print(f'chi_square [videogame_console, pet]: {chi:.3f}')

# nivel de confianza, comunmente 0.5  0.01. Entre mas pequeño,
# mayor confianza de rechazar la hipotesis nula
p = 0.05
n_r = len(c_t)
n_c = len(c_t['y'])
df = (n_r-1)*(n_c-1) #numero de renglones -1 y numero de comunas -1
#calcula el valor de la distribucion chi^2 en tablas (o con la ecuacion) 
chi_dist = chi2.isf(p, df)
print('======================================================================')
print(f'Valor de la distribucion chi^2 con {df} grados de libertad y {p} nivel confianza = {chi_dist}') 











