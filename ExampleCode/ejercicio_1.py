# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:32:01 2021

@author: EDUARDO

@Description:
1. El archivo adjunto salaries.csv contiene datos de 5 variables de interés para puestos de 
trabajo en México. Las variables son (entre paréntesis está el nombre de la variable en el 
archivo), puesto (offer), salario (salary), horas diarias de trabajo (hours_worked), días 
semanales de trabajo (days_worked), y estado de la república (state). Escribe un programa 
en Python que lea el archivo con Pandas y calcule lo siguiente: 
    a. El resumen de los cinco números, la media, la desviación estándar y dibuje el 
diagrama de caja para la variable salary para las respuestas del estado de Queretaro 
y solo para las personas que trabajan entre 20 y 40 horas a la semana (nota que la 
variable de horas de trabajo es por día). 
    b. El resumen de los cinco números, la media, la desviación estándar y dibuje el 
diagrama de caja para la variable salary para las respuestas del estado de 
Guanajuato y solo para las personas que trabajan entre 20 y 40 horas a la semana 
(nota que la variable de horas de trabajo es por día).
    c. La correlación entre las variables salary y days_worked de forma independiente 
para cada estado que aparece en la variable state. Debes separar los datos de salary 
y days_worked por estado, y para cada estado calcular la correlación entre esas dos 
variables.
"""
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


def var_std(values):
    n = len(values)
    md = sum(values)/n
    num = [(x - md)**2 for x in values]
    num = sum(num)
    var = num/(n-1)
    std = mt.sqrt(var)
    return var, std



def percentil(values, p):
    pos = (len(values) -1) * p
    pl = mt.floor(pos)
    pu = mt.ceil(pos)
    return values[pl]+(values[pu]-values[pl])*p

def summary(values):
    n = len(values)
    index = list(range(n))
    #Dispersion natural
    plt.figure()
    plt.scatter(index, values)
    plt.title('salary')
    
   
    
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
    plt.title('salary')
    
    
    
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'salaries.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file
values = df['hours_worked'].tolist()
values2 = df['days_worked'].tolist()

hw = [a*b for a,b in zip(values, values2)]
ste_filter = (df['state'] == 'Guanajuato')
summary(hw)
#lista variables intervalo/razon
#l_v = ['salary', 'hours_worked', 'days_worked']




