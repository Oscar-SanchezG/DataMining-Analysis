# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:37:46 2021

@author: ivand

@4. Utilizando el mismo archivo previo, escribe un programa en Python que
    encuentre la(s) moda(s) para las variables salary, hours_worked y days_worked.
    La moda es el valor de la lista que mas se repite (si varios numeros se repiten
    el mismo numero maximo de veces, todos son modas).
"""

import pandas as pd

def modes(values):
    d = {}
    for v in values:
        d[v] = d.get(v, 0) + 1
    
    l_f = [(v, k) for k, v in d.items()]
    l_f.sort(reverse=True)
    mx = l_f[0][0]
    mod = []
    for v, k in l_f:
        if v == mx:
            mod.append(k)
        else:
            break
    return mod 

def modes_var(var):
    values = df[var].tolist()
    mods = modes(values)
    print(f'Modas para {var}: {mods}')

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

modes_var('salary')
modes_var('hours_worked')
modes_var('days_worked')
