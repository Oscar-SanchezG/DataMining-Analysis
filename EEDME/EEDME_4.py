# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:10:24 2022

@author: EDUARDO

4. El archivo adjunto titanic.csv contine las siguientes variables de interés (PassengerId,
Survived, Pclass, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked). Escribe un programa
en Python que lea el archivo con Pandas y calcule lo siguiente:
    
a.  El resumen de los cinco números, la media, la desviación estándar y dibuje el 
    diagrama de caja para la variable Age (edad) de forma independiente para cada 
    valor de la variable Sex (sexo: female, male). Ignorar los valores que sean 0 en la 
    variable Age.
b.  La correlación entre las variables Age (edad) y Fare (tarifa) de forma 
    independiente para cada sexo. Debes separar los datos de Age y Fare por sexo y 
    para cada sexo calcular la correlación entre esas dos variables. 
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
    return std

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
    std = var_std(values)
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
print('-------------------------- Inciso a --------------------------------')
print('--------------------- Estadisticas para Age_male -------------------')
summary(l_v, 'Age_male')

#Filtro para female
age_filter = (df['Age'] >= 1)
sex_filter = (df['Sex'] == 'female')
sex_age_filter_f = df[age_filter][sex_filter]
l_v = sex_age_filter_f['Age'].tolist()

print('--------------------- Estadisticas para A_female -------------------')
summary(l_v, 'A_female')
print('------------------------------------------------ -------------------')

print('-------------------------- Inciso b --------------------------------')
print('------------ Correlacion para Age/fare para male -------------------')

vc_1 = 'Age'
vc_2 = 'Fare'
valuesc_1 = sex_age_filter_m[vc_1].tolist()
valuesc_2 = sex_age_filter_m[vc_2].tolist()
r = coef_pearson(valuesc_1, valuesc_2)
print(f'Coeficiente de Pearson para "{vc_1}" y "{vc_2}" = {r:.3f}')
sex_age_filter_m.plot(x=vc_1, y=vc_2, kind='scatter', title = 'male')

print('-------------------------- -----------------------------------------')
print('------------ Correlacion para Age/fare para female -------------------')

valuesc_1 = sex_age_filter_f[vc_1].tolist()
valuesc_2 = sex_age_filter_f[vc_2].tolist()
r = coef_pearson(valuesc_1, valuesc_2)
print(f'Coeficiente de Pearson para "{vc_1}" y "{vc_2}" = {r:.3f}')
print('------------------------------------------------ -------------------')
sex_age_filter_f.plot(x=vc_1, y=vc_2, kind='scatter', title = 'female')

