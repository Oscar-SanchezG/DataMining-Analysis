# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 12:18:05 2021

@author: EDUARDO

@Description:Leer el archivo con los datos de los estudiantes y para la varible
sexo y cuidad de origen, encontrar las frecuencias de cada valor y porcentaje. 
Imprimir los valores en orden decendente por porcentaje y sacar graficas de pie
y barras.
En ambos casos, convierte los valores a minúsculas para evitar irregularidades.
p. ej. Salamanca --> salamanca

Sexo
h:50:65%
m:30:35%

Cuidad
Salamanca:15:30%
Irapuato:10:25%
Celaya:8:20%
...
"""
import matplotlib.pyplot as plt
import pandas as pd

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

# Sex variable
sexs = df['sex'].tolist() #creo una lista
d = {}  #Diccionario vacio
n = 0
for v in sexs:              #Lleno el diccionario
    v = v.lower().strip()
    d[v] = d.get(v, 0) + 1
    n += 1
    
freqs = []
for v,f in d.items():
    freqs.append((f, f/n*100, v))
    
freqs.sort(reverse=True)
lab =[]
val =[]
print('Sexo:')
for f,p,v in freqs:
    print(f'{v}:{f}:{p:.2f}%')
    lab.append(v)
    val.append(f)

plt.pie(val, labels=lab) #Grafica de pay
plt.figure() #nueva figura sino ensima la graficas
plt.bar(lab, val)



# City of origin varibale
print('\n')

c_o = df['city_origin'].tolist() #creo una lista
d = {}  #Diccionario vacio
n = 0
for v in c_o:              #Lleno el diccionario
    v = v.lower().strip()
    d[v] = d.get(v, 0) + 1
    n += 1
    
freqs = []
for v,f in d.items():
    freqs.append((f, f/n*100, v))
    
freqs.sort(reverse=True)
lab =[]
val =[]
print('Ciudad de origen:')
for f,p,v in freqs:
    print(f'{v}:{f}:{p:.2f}%')
    lab.append(v)
    val.append(f)
plt.figure() #nueva figura sino ensima la graficas
plt.pie(val, labels=lab) #Grafica de pay
plt.figure() #nueva figura sino ensima la graficas
plt.bar(lab, val)
#Create a pie and a bar plot for both variables
#Create a function with the previous



