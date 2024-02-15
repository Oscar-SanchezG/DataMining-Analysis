# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 04:15:12 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para las
variables nominales: genero, mascota y consola

Generar una tabla de contingencia entre cada par de variables:

[genero, consola]
[genero, mascota]
[consola, mascota]

en el caso de la mascota, transforma a valor binario (y/n). Todas
deben ser tablas de contingencia de 2x2

Calcular la probabilidad condicional entre cada valor de cada par de variables:
    
genero(h/m), consola(y/n)
genero(h/m), mascota(y/n)
consola(h/m), consola(y/n)

"""

import pandas as pd


def cond_prod(values_1, values_2, l_1, l_2):
    n = len(values_1)
    num = den =0
    for v_1, v_2 in zip(values_1, values_2):
        if v_1 == l_1 and v_2 == l_2:
            num += 1
        if v_2 == l_2:
            den += 1
            
    num /= n
    den /= n
    cp = num/den
    return cp

def cond_prod_iter(values_1, values_2, lab_1, lab_2):
    for l_1 in lab_1:
        for l_2 in lab_2:
            p_c = cond_prod(values_1, values_2, l_1, l_2)
            print(f'Confitional probability of [{l_1}|{l_2}]= {p_c:.3f}')
    pass

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#lista variables nominales
sex = df['sex'].tolist()
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]
con = df['videogame_console'].tolist()
sex_1 = set(sex)
con_1 = set(con)
pet_1 = set(pet)

print('Conditional probability between sex and video games console')
cond_prod_iter(sex, con, sex_1, con_1)
print('-----------------------------------------------------------')
print('Conditional probability between sex and video pet')
cond_prod_iter(sex, pet, sex_1, pet_1)
print('-----------------------------------------------------------')
print('Conditional probability between video game console and pet')
cond_prod_iter(con, pet, con_1, pet_1)










