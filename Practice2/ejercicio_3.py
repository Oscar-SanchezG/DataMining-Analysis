# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:24:51 2021

@author: ivand
"""

import pandas as pd
import math as mt
def d_euclidiana(p, q):
    d = [(pi - qi)**2 for pi, qi in zip(p, q)]
    d = sum(d)
    d = mt.sqrt(d)
    return d

w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

f_salary = df['salary'] > 20000

salary_data = df[f_salary]['salary'].tolist()
hours_data = df[f_salary]['hours_worked'].tolist()
days_data = df[f_salary]['days_worked'].tolist()

vector = [(x, y, z) for x, y, z in zip(salary_data, hours_data, days_data)]

n = len(vector)

m_d = []
for i in range(n):
    t = [0 for j in range(n)]
    m_d.append(t)
    
for i in range(n-1):
    for j in range(i+1, n):
        d = d_euclidiana(vector[i], vector[j])
        m_d[i][j] = d
        m_d[j][i] = d
        
print(m_d)