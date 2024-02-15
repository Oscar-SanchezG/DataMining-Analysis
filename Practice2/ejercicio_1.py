# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:15:34 2021

@author: ivand
"""

import matplotlib.pyplot as plt
import pandas as pd
import math as mt

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n - 1)
    std = mt.sqrt(var)
    return var, std

def percentil(values, p):
    pos = (len(values) - 1) * p
    pl = mt.floor(pos)
    pu = mt.floor(pos)
    return values[pl] + (values[pu] - values[pl]) * p

def summary(values, var): 
    
    #Resumen de los cinco numeros
    mi = values[0]
    mx = values[-1]
    fq = percentil(values, 0.25)
    med = percentil(values, 0.50)
    tq = percentil(values, 0.75)
    print(f'Mínimo = {mi:.2f}')
    print(f'Máximo = {mx:.2f}')
    print(f'1er cuartil = {fq:.2f}')
    print(f'Mediana = {med:.2f}')
    print(f'3er cuartil = {tq:.2f}')
    
    #Mean
    md = sum(values)/len(values)
    print(f'Media/promedio = {md:.2f}')
    
    #Varianze and standard deviation
    vari, std = var_std(values)
    print(f'Varianza = {vari:.2f}')
    print(f'Desviación estándar {std:.2f}')
    
    #Boxplot
    plt.figure()
    plt.boxplot(values)
    plt.title(f'{var}')
    
def coef_pearson(values_1, values_2):
    mx = sum(values_1)/len(values_1)
    my = sum(values_2)/len(values_2)
    num = sum([(x - mx)*(y - my) for x,y in zip(values_1, values_2)])
    den_1 = mt.sqrt(sum([(x - mx)**2 for x in values_1]))
    den_2 = mt.sqrt(sum([(y - my)**2 for y in values_2]))
    den = den_1 * den_2
    r = num/den
    return r
    
w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

f_gto = df['state'] == 'Guanajuato'

salary_gto = df[f_gto]['salary'].tolist()
hours_gto = df[f_gto]['hours_worked'].tolist()
days_gto = df[f_gto]['days_worked'].tolist()

total_hours = [h*d for h, d in zip(hours_gto, days_gto)]
salary_gto = [s for s, h in zip(salary_gto, total_hours) if h >= 20 and h <= 40]

print('-------------------------- Inciso a ----------------------------------')
print('--------------------- Estadisticas para Guanajuato -------------------')
summary(salary_gto, 'Guanajuato')

f_qro = df['state'] == 'Querétaro'

salary_qro = df[f_qro]['salary'].tolist()
hours_qro = df[f_qro]['hours_worked'].tolist()
days_qro = df[f_qro]['days_worked'].tolist()

total_hours = [h*d for h, d in zip(hours_qro, days_qro)]
salary_qro = [s for s, h in zip(salary_qro, total_hours) if h >= 20 and h <= 40]

print('--------------------------- Inciso b --------------------------------')
print('--------------------- Estadisticas para Querétaro --------------------')
summary(salary_qro, 'Querétaro')

print('---------------------------- Inciso c --------------------------------')
states = df['state'].tolist()
states = list(set(states))
states.sort()

for s in states:
    s_filter = df['state'] == s
    salary = df[s_filter]['salary']
    days = df[s_filter]['days_worked']
    corr = coef_pearson(salary, days)
    print(f'Correlacion de Pearson para {s}: {corr:.3f}')