# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 00:33:38 2021

@author: oscar
@Description: This is my first program in python. Initialize some variables
and print some results.
"""
a = 5
b = 6
c = 8
d = e = f = 19
h = 9*a
print(d)
print(a*b)
print(h)
print(a, e, f)

#Operadores aritmeticos basicos
a = b + c   #Suma
a = b * c   #Multiplicacion
a = b - c   #Resta
a = b / c   #Division
a = b // c  #Division entera
a = b ** c  #Exponente
a = b % c   #Modulo

#Operadores in-site
a += c      # a = a + c
a += c      # a = a * c
a -= c      # a = a - c
a /= c      # a = a / c
a //= c     # a = a // c
a **= c     # a = a ** c
a %= c      # a = a % c

#Operadores de comparacion  --> Devuelve un valor logico
a == b      #Igual que
a > b       #Mayor que
a < b       #Menor que
a != b      #No igual que
a >= b      #Mayor o igual que
a <= b      #Menor o igual que

#Operadores logicos --> Devuelve un valor logico de verdad
a = True    #Valor logico de verdad
a = False   #Valor logico de Falso
a and b     #Conjuncion and
a or b      #Disyuncion or
not a       #Negacion Not
(a == b) and (e < h)

#Strings basicos
s = 'Hola mundo!'
s = "Hola mundo!"
s = 'Hola "mundo"'
s = "Hola 'Mundo'"
s = 'Hola \'mundo\''

a = float(input('Ingrese el coeficiente de la variable cuadrática\n'))
b = float(input('Ingrese el coeficiente de la variable cuadrática\n'))
C = float(input('Ingrese el coeficiente de la variable cuadrática\n'))