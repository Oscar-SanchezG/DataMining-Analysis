# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:10:22 2022

@author: EDUARDO

3. Escribe un programa en Python que dado un número entero n>3, cree una lista de listas de 
nxn, llena con números enteros al azar entre 1 y 100, y que después imprima todos los 
bloques continuos de 3x3 junto con el promedio de cada bloque.
Ejemplo:
Dado: n = 4
Se genera al azar la siguiente lista de listas (como si fuera un arreglo de 4x4):
    
m =  [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

Salida: [[1,2,3],[5,6,7],[9,10,11]], 6 
        [[2,3,4],[6,7,8],[10,11,12]], 7
        [[5,6,7],[9,10,11],[13,14,15]], 10
        [[6,7,8],[10,11,12],[14,15,16]], 11
        
Explicación: A continuación, se muestran los bloques de 3x3 que se generan:
[[1, 2, 3, 4],      [[1, 2, 3, 4],      [[1, 2, 3, 4],      [[1, 2, 3, 4],
[5, 6, 7, 8],       [5, 6, 7, 8],       [5, 6, 7, 8],       [5, 6, 7, 8],
[9, 10, 11, 12],    [9, 10, 11, 12],    [9, 10, 11, 12],    [9, 10, 11, 12],
[13, 14, 15, 16]]   [13, 14, 15, 16]]   [13, 14, 15, 16]]   [13, 14, 15, 16]
"""

import random as rn

n = int(input("Numero de N: "))
l=[]
for i in range(n):
    aux=[]
    for j in range(n):
        nr=rn.randint(1, 100)
        aux.append(nr)
    l.append(aux)


        
