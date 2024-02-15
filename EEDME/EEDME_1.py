# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:10:19 2022

@author: EDUARDO

1. Escribe un programa en Python que lea un archivo que contenga una lista de países y de 
ciudades que están en esos países. Después, que pida una ciudad al usuario y devuelva en 
qué país se encuentra esa ciudad, en caso de que la ciudad no se encuentre, que devuelva 
‘No sé’. En el archivo, una línea representa un país y sus ciudades, la primera palabra de la 
línea es el país y el resto de las palabras son las ciudades, todas separadas por espacios. 
Crear el archivo para probar en formato .txt. Transformar los nombres a minúsculas para 
comparar.

Ejemplo:
Archivo: US Boston Pittsburgh Washington Seattle 
        UK London Edinburgh Cardiff Belfast
        México Guanajuato Querétaro CDMX Toluca Torreón
        Brasil Río Brasilia SaoPaulo Recife PortoAlegre
Dado: ciudad = ‘Guanajuato’
Salida: Mexico

Explicación: Hay cuatro países: US, UK, Mexico y Brasil, cada uno con una lista de ciudades 
que se encuentran en él. Guanajuato es una ciudad que se encuentra en Mexico.

"""

import pandas as pd


w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
f_i = w_d +'paises.txt'

l_pub = []
with open(f_i, 'r', encoding=('utf-8') ) as f_r:
    for line in f_r:
        l_pub.append(line.strip()) 
l_pub = [pub.lower() for pub in l_pub]
l_pub = [pub.split() for pub in l_pub]

n = str(input("Enter the city: "))
n = n.lower()
l_pub1 = []

for pub in l_pub:
    for token in pub:
        if token == n:
            l_pub1.append(pub)

if l_pub1 == []:
    print('No sé')
else:
    print(l_pub1[0][0])