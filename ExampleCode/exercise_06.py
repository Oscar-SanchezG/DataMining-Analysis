# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:22:52 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y hacer una 
funcion para obtener el resumen de los cinco numeros (minimo, maximo, 1er
cuartil, mediana, 3er cuartil) para cada variable de tipo intervalo/razon.
Calcular la media.
Graficar el Boxplot.

Además, la funcion debe de encontrar los outliers haciendo lo siguiente:
a. Calcular el rango intercuartil (IQR)
b. Calcular las vallas (Upper inner fence, lower inner fence)
c. Encontrar los whiskers (Upper whisker, lower whisker)
d. Encontrar los outliers

Recortar los datos a un a% y volver a calcular todo lo anterior.

Ejemplo para recortar los datos
L = [33750, 33750, 33750, 33750, 44000, 44000, 44000, 44000, 45566, 65000
  95000, 103500, 112495, 138188, 141666, 181500, 190000, 194375, 195000]

a = 10 
k = 10/100*n = 10/100*20 = 2

L = [33750, 33750, 44000, 44000, 44000, 44000, 45566, 65000
  95000, 103500, 112495, 138188, 141666, 181500, 190000]

Agregar a la funcion summary el calculo de la varianza y la desviación estándar

var = sum((xi-mean(x))^2)/(n-1)
sd = sqrt(var)
"""

import matplotlib.pyplot as plt
import pandas as pd
import math as mt

def trim_data(values, a):
    n = len(values)
    k = int(a/100*n)
    print(f'Valores a recortar : {k}')
    return values[k:n-k]

def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return var, std

def outliers(values, fq, tq):
    iqr = tq - fq
    uif = tq + 1.5 * iqr
    lif = fq - 1.5 * iqr
    for i in values:
        if i >= lif:
            lw = i
            break
    for i in values[::-1]:
        if i <= uif:
            uw = i
            break
    outs = []
    for i in values:
        if i < lw or i > uw:
            outs.append(i)
    return iqr, lif, uif, lw, uw, outs

def percentil(values, p):
    pos = (len(values) -1) * p
    pl = mt.floor(pos)
    pu = mt.ceil(pos)
    return values[pl]+(values[pu]-values[pl])*p

def summary(values, var):
    n = len(values)
    index = list(range(n))
    #Dispersion natural
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    #Dispersion ordenada
    values.sort()
    plt.figure()
    plt.scatter(index, values)
    plt.title(f'{var}')
    
    # Resumen de los cinco numeros
    mi = values[0]
    mx = values[-1]
    fq = percentil(values, 0.25)
    med = percentil(values, 0.50)
    tq = percentil(values, 0.75)
    print(f'Mínimo = {mi:.2f}')
    print(f'Máximo = {mx:.2f}')
    print(f'1er cuártil = {fq:.2f}')
    print(f'Mediana = {med:.2f}')
    print(f'3er cuártil = {tq:.2f}')
    # Mean
    md = sum(values)/len(values)
    print(f'Media/promedio = {md:.2f}')
    
    #Varianze and standar devitation
    vari, std = var_std(values)
    print(f'Varianza = {vari:.2f}')
    print(f'Desviación estándar = {std:.2f}')
    
    # Boxplot
    plt.figure()
    plt.boxplot(values)
    plt.title(f'{var}')
    
    # Find outliers
    iqr, lif, uif, lw, uw, outs = outliers(values, fq, tq)
    print(f'IQR = {iqr:.2f}')
    print(f'LIF = {lif:.2f}')
    print(f'UIF = {uif:.2f}')
    print(f'LW = {lw:.2f}')
    print(f'UW = {uw:.2f}')
    print(f'Outliers = {outs}')
    print(f'Total outliers = {len(outs)}')
    
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Lista de intervalo y razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['semester']
# Iterar sobre la lista de variables
for v in l_v:
    print(f'*************************** {v} ****************************')
    print('--------------------- Valores Completos ---------------------')
    values = df[v].tolist()
    summary(values, v)
    print('-------------------------------------------------------------')
    
    print('****************** Valores recortados ***********************')  
    values = trim_data(values, 10)
    summary(values, v)
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('*************************************************************')
    
    
    
    
    
    