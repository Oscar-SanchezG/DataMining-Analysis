# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:52:00 2021

@author: EDUARDO

@Description:1. Compute the five-number summary, the mean, and the standard deviation for the 
annual salary per gender (the data considers three genders, you must compute the 
statistics for each one) and draw the boxplot.
Perform the computations with the original data and with the trimmed data at 10% for 
the salary (you must cut the 10% lowest salaries and 10% highest salaries). Make 
comparisons between the results with the original data and the ones with the trimmed 
data.
Besides, try to give and explanation for the following questions by using the trimmed 
data at 10% for the salary and by computing all the additional and necessary statistics 
and drawing the necessary graphs/plots.
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
    #print(f'Outliers = {outs}')
    print(f'Total outliers = {len(outs)}')
    
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'survey_results.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Lista de intervalo y razon
l_v_g = ['Man', 'Woman', 'Non-binary, genderqueer, or gender non-conforming']
filter_Gen = (df['Gender'] == 'Man')
l_v = ['ConvertedComp']
# Iterar sobre la lista de variables
for v in l_v:
  
    print(f'******************* {v}, ConvertedComp *********************')
    print('--------------------- Valores Completos ---------------------')
    values = df[filter_Gen]['ConvertedComp'].tolist()
    print("The total number of elements in the list: ", len(values))
    summary(values, v)  
    print('-------------------------------------------------------------')
    
    print('****************** Valores recortados ***********************')  
    values = trim_data(values, 10)
    summary(values, v)
    print("The total number of elements in the list: ", len(values))
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('*************************************************************')


#a. Which gender has more answers? 
#b. Which gender tends to have higher salaries, and which one tends to have lower 
#salaries? 
#c. What are the most popular and less popular programming language per gender? 
#d. What are the most popular and less popular developer type per gender? 
#e. Is there a relation between gender and salary? (Consider only the genders 
#man/woman) 
#f. Is there a relation between gender and age? (Consider only the genders 
#man/woman) 

