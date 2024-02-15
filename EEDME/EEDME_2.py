# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:10:21 2022

@author: EDUARDO

2. Escribe un programa en Python que lea un archivo de texto, lo separe en palabras, 
encuentre aquellas que terminen en ‘ando’ o ‘iendo’ y elimine esos segmentos de las 
palabras, pero solo cuando la primera letra de la palabra esté en mayúscula. La salida se 
debe guardar en otro archivo, guardando tanto las palabras no modificas como las sí 
modificadas. Utiliza la expresión regular \w+ para capturar las palabras. Solo se deben 
modificar las palabras que contengan exclusivamente letras (no números o caracteres 
especiales).

Ejemplo:
Archivo entrada: hola estoy corriendo Saltando y Cantando Corr1iendo
Archivo salida: hola estoy corriendo Salt y Cantando corr1iendo

Explicación: Hay cuatro palabras que terminan en ‘ando’ o ‘iendo’ (corriendo, Saltando, 
Cantando, Corr1iendo), de éstas solo 3 empiezan con mayúsculas (Saltando, Cantando, 
Corr1iendo), finalmente, solo 2 están compuestas por solo letras (Saltando, Cantando) que 
son las que se modifican
"""
import pandas as pd
import re

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
f_i = w_d +'palabras.txt'

l_pub = []
with open(f_i, 'r', encoding=('utf-8') ) as f_r:
    for line in f_r:
        l_pub.append(line.strip()) 
l_pub = [pub.split() for pub in l_pub]

l_pub1 = []
for pub in l_pub:
    for token in pub:
        l = re.findall('[a-z].ando', token)
        if token == l:
            l_pub1.append(token)

#s = '*/!'.join(l_pub) 
      

