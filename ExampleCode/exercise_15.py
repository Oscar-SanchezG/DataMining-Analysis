# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 02:47:31 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para las
variables nominales: genero, mascota y consola y de intervalo/razon
calcular la correlacion de punto biseral entre cada par de variables: una
nominal y una intervalo/razon

[genero, altura]
[genero, peso]
[genero, semestre]
[genero, materias_cursadas]
[consola, altura]
[consola, peso]
[consola, semestre]
[consola, materias_cursadas]
[mascota, altura]
[mascota, peso]
[mascota, semestre]
[mascota, materias cursadas]

en caso de la mascota, transforma a valor binario (y/n)

r_pb = ((M_0-M_1)/s_y) sqrt(n_0/n n_1/n)
"""

import pandas as pd
import math as mt

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return std

def point_biseral(values_1, values_2, lab):
    n = len(values_1)
    n0 = n1 = m0 = m1 = 0
    for l, v in zip(values_1, values_2):
        if l == lab[0]:
            n0 += 1
            m0 += v
        else:
            n1 += 1
            m1 += v
    sy = var_std(values_2)
    m0 /= n0
    m1 /= n1
    t1 = (m0 - m1)/sy
    t2 = mt.sqrt((n0/n)*(n1/n))
    rpd = t1*t2
    return rpd

   
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#lista variables intervalo/razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['age']

#lista variables nominales
sex = df['sex'].tolist()
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
con = df['videogame_console'].tolist()

# Para la variable genero
for v in l_v:
    values =df[v].tolist()
    rpd = point_biseral(sex, values, ['h', 'm'])
    print(f'Point biseral correlation [sex, {v} = {rpd:.3f}')
    
# Para la variable consola
for v in l_v:
    values =df[v].tolist()
    rpd = point_biseral(con, values, ['y', 'n'])
    print(f'Point biseral correlation [Video game console, {v} = {rpd:.3f}')

# Para la variable mascota
for v in l_v:
    values =df[v].tolist()
    rpd = point_biseral(pet, values, ['y', 'n'])
    print(f'Point biseral correlation [pet, {v} = {rpd:.3f}')














