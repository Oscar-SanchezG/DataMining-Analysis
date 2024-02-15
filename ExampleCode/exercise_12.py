# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 01:08:30 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para las
variables nominales: genero, mascota y consola

Generar una tabla de contingencia entre cada par de variables:

[genero, consola]
[genero, mascota]
[consola, mascota]

en el caso de la mascota, transforma a valor binario (y/n). Todas
deben ser tablas de contingencia de 2x2

Calcular el Odds ratio entre cada par de variables

                var1
        var2 / 1 / 0 /
        --------------
        1   / n11 / n10 /
        0   / n01 / n00 /

OR = (n_11n_00)/(n_10n01)
"""

import pandas as pd

def contingency_table(values_1, values_2):
    d_s = {}
    for i, j in zip(values_1, values_2):
        if i not in d_s:
            d_s[i] = {}
        d_s[i][j] = d_s[i].get(j, 0) + 1
    return d_s

def odds_ratio(c_t, lab_1, lab_2):
    #agregar la condicion para el valor 0
    n11 = c_t[lab_1[0]][lab_2[0]]
    n10 = c_t[lab_1[0]][lab_2[1]]
    n01 = c_t[lab_1[1]][lab_2[0]]
    n00 = c_t[lab_1[1]][lab_2[1]]
    odds = (n11*n00)/(n10*n01)
    return odds

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# [sex, videogame_console]
sex = df['sex'].tolist()
con = df['videogame_console'].tolist()
c_t = contingency_table(sex, con)
print('[sex, videogame_console]:', c_t)
odds = odds_ratio(c_t, ['h', 'm'], ['y', 'n'])
print(f'Odds ratio [sex, videogame_console]: {odds:.3f}')

# [sex, pet]
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
c_t = contingency_table(sex, pet)
print('[sex, pet]:', c_t)
odds = odds_ratio(c_t, ['h', 'm'], ['y', 'n'])
print(f'Odds ratio [sex, pet]: {odds:.3f}')

# [videogame_console, pet]
c_t = contingency_table(con, pet)
print('[videogame_console, pet]:', c_t)
odds = odds_ratio(c_t, ['y', 'n'], ['y', 'n'])
print(f'Odds ratio [videogame_console, pet]: {odds:.3f}')

