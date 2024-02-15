# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 08:52:02 2022

@author: EDUARDO

@Descrition: Leer archivo de publicaciones de amigos csv y para cada
publicacion:
    1.- ConvertirLa a minusculas
    2.- Separarla en tokens usando espacios o una expresion regular \w+
    3. - Quitar Los tokens de cada publicacion que sean solo numeros
    
amigo,sexo,publicacion
am_1,f,Hola Mundo 1234
am_1,f,Que tal 568 Estoy bien

--->['Hola Mundo 1234', 'Que tal 568 Estoy Bien']
1. ['hola mundo 1234', 'que tal 568 estoy bien']
2. p1 = ['hola', 'mundo', '1234']
   p2 = ['que', 'tal', '568', 'estoy', 'bien']
3. p1 = ['hola', 'mundo']
   p2 = ['que', 'tal', 'estoy', 'bien']

"""

import pandas as pd
import re

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'fb_posts.csv'

df = pd.read_csv(i_f)

l_pub = df['publicacion'].tolist()

# Punto 1
l_pub = [pub.lower() for pub in l_pub]

#Punto 2
# exprecion regular
l_pub = [re.findall('\w+', pub) for pub in l_pub]

#con split
l_pub = [pub.split() for pub in l_pub]


#Punto 3
l_pub = [[token for token in pub if not token.isdigit()] for pub in l_pub]