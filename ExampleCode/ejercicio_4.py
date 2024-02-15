# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:32:06 2021

@author: EDUARDO

@Description:


"""
import pandas as pd

#l=[1, 2, 3, 4, 5, -1, -1, -5, -2, 1, 2, 1, 2, 3, 3, -1]

def moda(l):
    modal = []
    con = 0
    for e in l:
        if l.count(e) > con :
            modal = []
            modal.append(e)
            con = l.count(e)
        elif l.count(e) == con:
            if not e in modal:
                modal.append(e)
                con = l.count(e)
    if con * len(modal) == len(l):
        modal = [-1]
    return modal

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'salaries1.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#lista variables intervalo/razon
l_v = ['salary', 'hours_worked', 'days_worked']
#l_v = ['salary']

for v in l_v:
    values =df[v].tolist()
    mo = moda(values)
    print(f' La moda para {v} es :  {mo}')
    











