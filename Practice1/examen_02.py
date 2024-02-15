# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:38:41 2021

@author: ivand

@2. Con el mismo archivo del punto anterior escribe un programa en Python que:
    a.  Transforme la variable salary a una variable binaria, considerando
        sueldos altos o bajos. Un salario bajo es aquel menor o igual 10000,
        el alto es mayor a 10000.
    b. Transforme la variable hours_worked en una variable binaria, 
        considerando tiempo completoo tiempo parcial, el tiempo parcial es menor
        o igual a 6 horas, el tiempo completo es mayor a 6 horas.
    c. Genere una tabla de contingencia con estas dos variables como se muestra
        a continuacion (los numeros son ficticios).
    d. Calcular el valor esperado para cada combinacion de renglon y columna
        (Cuantas ofertas de un tipo de salario son para trabajar tiempo 
        completo o parcial?). El valor esperado se calcula como
    E_(c, r) = ((suma de renglon r)(suma de columna c))/(total de observaciones)
        
"""

import pandas as pd

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

salary = df['salary'].tolist()
hours = df['hours_worked'].tolist()

sal_bin = ['bajo' if s <= 10000 else 'alto' for s in salary]
hou_bin = ['parcial' if h <= 6 else 'completo' for h in hours]
sal_vals = list(set(sal_bin))
hou_vals = list(set(hou_bin))

d_c = {}
for s, h in zip(sal_bin, hou_bin):
    t = (s, h)
    d_c[t] = d_c.get(t, 0) + 1

print('=========== Tabla de contingencia ===============')
print('\t'+' / '.join(hou_vals))
print('      --------------------')
for s in sal_vals:    
    print(f'{s}: '+' / '.join(f'{d_c[(s, h)]}' for h in hou_vals))

total = sum([v for k, v in d_c.items()])
for s in sal_vals:
    s_r = sum([v for k, v in d_c.items() if k[0] == s])
    for h in hou_vals:
        s_c = sum([v for k, v in d_c.items() if k[1] == h])
        ev = s_r*s_c/total
        print(f'Valor esperado para el renglos {s} y la columna {h}: {ev:.3f}')
