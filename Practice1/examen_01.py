# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 11:07:36 2021

@author: ivand

@1. El archivo adjunto salaries.csv contiene datos de 5 variables de interes
para puestos de trabajo en mexico. Las variables son (entre parentesis esta el
nombre de la variable en el archivo), puesto (offer), salario (salary), horas
diarias de trabajo (hours_worked), dias semanales de trabajo (days_worked),
y estado (state). Escribe un programa en Python que lea el archivo con Pandas
y calcule lo siguiente:
a. El resumen de los cinco numeros, la media, la desviacion estandar y dibuje
    el diagrama de caja para la variable salary de forma independiente para los
    estados de Guanajuato y Queretaro, pero solo para las personas que trabajan
    entre 20 y 40 horas a la semana (todos los calculos deben ser independiente
    para cada estado).
b. La correlacion entre las variables salary y days_worked en general de forma
    independiente para estado posible (cada uno de los que aparecen en el conjunto
    de datos).
"""

import matplotlib.pyplot as plt
import pandas as pd
import math as mt

def coef_pearson(values_1, values_2):
    mx = sum(values_1)/len(values_1)
    my = sum(values_2)/len(values_2)
    num = sum([(x - mx)*(y - my) for x,y in zip(values_1, values_2)])
    den_1 = mt.sqrt(sum([(x - mx)**2 for x in values_1]))
    den_2 = mt.sqrt(sum([(y - my)**2 for y in values_2]))
    den = den_1 * den_2
    r = num/den
    return r

def percentil(values, p):
    pos = (len(values) - 1) * p
    pl = mt.floor(pos)
    pu = mt.floor(pos)
    return values[pl] + (values[pu] - values[pl]) * p

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n - 1)
    std = mt.sqrt(var)
    return var, std

def summary(values, var): 
    n = len(values)
    index = list(range(n))
    
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
    
def stats_per_state(state):
    st_filter = df['state'] == state
    
    salary = df[st_filter]['salary'].tolist()
    hours = df[st_filter]['hours_worked'].tolist()
    days = df[st_filter]['days_worked'].tolist()
    
    total_hours = [h*d for h, d in zip(hours, days)]
    salary = [s for s, h in zip(salary, total_hours) if h >= 20 and h <= 40]
    
    print(f'=================== Estadisticas para {state} ================')
    summary(salary)
    
w_d = 'C:/Users/ivand/Desktop/Universidad/Ago-Dic2021/MineriaDatos/Examen/'
i_f = w_d + 'salaries.csv'

df = pd.read_csv(i_f)

#Guanajuato
stats_per_state('Guanajuato')

#Queretaro
stats_per_state('Querétaro')

#Correlacion por estado
states = df['state'].tolist()
states = list(set(states))
states.sort()

print('============== Correlacion de Pearson ===============')
for state in states:
    st_filter = df['state'] == state
    salary = df[st_filter]['salary']
    days = df[st_filter]['days_worked']
    corr = coef_pearson(salary, days)
    print(f'Correlacion de Pearson entre salary y days worked para {state}: {corr:.3f}')