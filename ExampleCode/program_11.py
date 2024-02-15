# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 04:30:12 2021

@author: oscar

@Description: Functions and files
"""
def greet(name):
    """ this funtion sends a geet to the person
    that is passed as argument"""
    print('Hello, ' +name + '. Good mornig')
    
greet('Juan')   #Llamada a la funcion

def absolute_value(num, name):
    """ this funtion returns the absolute value of 
    a number"""
    print('Hello, ' +name + '. Good mornig')
    if num >= 0:
        return num, name
    else:
        return -num, name
    
print(absolute_value(-89))
n= absolute_value(-89, 'maria')
print(n)

#Default arguments
def geet(name, msg = 'Good morning!', number = 3):
    """This function geets a person with the derired message.
    if the message ir not passed, the default "Good morning" is used.
    """
    print('Hello ' + name + ', ' + msg + str (number))
    
greet('Maria')
greet('Maria', 'How do you do?')
greet('Maria', 'How do you do?', 10)

#Keyswords arguments
greet(name = 'Maria', msg = 'How do you do?')
greet(msg = 'How doyou do?', name = 'Maria', number = 10)
greet('Maria', number = 9, msg = 'How do you do?')

try:
    greet(msg='How do you do?')
except:
    print('Error')

#undefined number of arguments
def greet(*names):
    """This function greets all the persons
    inside a tuple."""
    # names is a tuple with all the arguments
    print(names)
    
greet('Maria', 'Luis', 'Pedro', 'Susana', ['Juan', 'Ana'])
greet('Maria', 'Luis')

"""
22. Escribe un programa que tome un diccionario con llaves string y valores strings y números (definido por ti) y que devuelva la suma y promedio de todos los valores que son numéricos.

23. Dados dos diccionarios (definidos por ti), escribe un programa que devuelva una lista con las llaves que ambos comparten.

24. Escribe un programa que genere una lista llena con números enteros aleatorios

25. Dado un string (definido por ti), escribe un programa que genere un diccionario en donde la llave es la posición de cada caracter del string y el valor el propio caracter.

26. Escribe un programa que dada una lista de números enteros (definida por ti), genere un diccionario donde la llave es el número entero y el valor es una lista con todos los divisores exactos de ese número.

27. Escribe una función que reciba un número entero n y devuelva un string de n caracteres, donde los caracteres son letras del alfabeto en minúsculas seleccionadas al azár.

28. Los mismo que el anterior, pero el string puede contener letra en mayúsculas o minúsculas.

29. Escribe un programa que permita jugar piedra, papel o tijera con la computadora (selección de forma aleatoria).

"""



