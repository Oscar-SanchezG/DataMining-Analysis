# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 02:04:21 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para las
variables nominales: genero, mascota y consola

Generar una tabla de contingencia entre cada par de variables:

[genero, consola]
[genero, mascota]
[consola, mascota]

en el caso de la mascota, transforma a valor binario (y/n). Todas
deben ser tablas de contingencia de 2x2

Calcular el coeficiente phi de Pearson entre cada par de variables

                var1
        var2 / 1 / 0 /
        --------------
        1   / n11 / n10 / n1*
        0   / n01 / n00 / n0*
              n*1   n*0

phi = (n_11n_00-n10n01)/sqr(n_(1*)n_(0*)n_(*1)n_(*0))
"""
import pandas as pd
import math as mt

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def phi_coefficient(c_t, lab_1, lab_2):
    #agregar la condicion para el valor 0
    n11 = c_t[lab_1[0]][lab_2[0]]
    n10 = c_t[lab_1[0]][lab_2[1]]
    n01 = c_t[lab_1[1]][lab_2[0]]
    n00 = c_t[lab_1[1]][lab_2[1]]
    
    n1a = n11 + n10
    n0a = n01 + n00
    na1 = n11 + n01
    na0 = n10 + n00
    
    num = (n11*n00) - (n10*n01)
    dem = n1a * n0a * na1 * na0
    dem = mt.sqrt(dem)
    phi =num / dem
    
    return phi

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
phi = phi_coefficient(c_t, ['h', 'm'], ['y', 'n'])
print(f'Phi coefficient [sex, videogame_console]: {phi:.3f}')

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
phi = phi_coefficient(c_t, ['h', 'm'], ['y', 'n'])
print(f'Phi coefficient [sex, pet]: {phi:.3f}')

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[videogame_console, pet]:', c_t)
phi = phi_coefficient(c_t, ['y', 'n'], ['y', 'n'])
print(f'Phi coefficient [videogame_console, pet]: {phi:.3f}')

















