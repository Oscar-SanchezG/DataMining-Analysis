# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:02:22 2021

@author: ivand
"""

import pandas as pd

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

salary = df['salary'].tolist()
hours = df['hours_worked'].tolist()

#------------------------- Inciso a --------------------------
b_salary = ['Bajo' if s <= 10000 else 'Alto' for s in salary]
salary_v = list(set(b_salary))

#------------------------- Inciso b --------------------------
b_hours = ['Parcial' if h <= 6 else 'Completo' for h in hours]
hours_v = list(set(b_hours))

#------------------------- Inciso c --------------------------
d_c = {}
for s, h in zip(b_salary, b_hours):
    t = (s, h)
    d_c[t] = d_c.get(t, 0) + 1

print('=========== Tabla de contingencia ===============')
print('\t'+' | '.join(hours_v))
print('   --------------------')
for s in salary_v:    
    print(f'{s}: '+' | '.join(f'{d_c[(s, h)]}' for h in hours_v))

#------------------------ Inciso d --------------------------
yule_coef = ((31980)*(71)-(1097)*(3646))/((31980)*(71)+(1097)*(3646))
print(f'El coeficiente Q de Yule es: {yule_coef:.3f}')