# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 02:32:14 2022

@author: EDUARDO
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
    
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'titanic.csv'

df = pd.read_csv(i_f)
#Filtro para male
age_filter = (df['Age'] >= 1)
sex_filter = (df['Sex'] == 'male')
sex_age_filter_m = df[age_filter][sex_filter]
l_v = sex_age_filter_m['Age'].tolist()
print('-------------------------- Inciso a ----------------------------------')
print('--------------------- Estadisticas para Age_male -------------------')
summary(l_v, 'Guanajuato')

#Filtro para female
age_filter = (df['Age'] >= 1)
sex_filter = (df['Sex'] == 'female')
sex_age_filter_f = df[age_filter][sex_filter]
l_v = sex_age_filter_f['Age'].tolist()

print('--------------------- Estadisticas para A_female -------------------')
summary(l_v, 'Guanajuato')

