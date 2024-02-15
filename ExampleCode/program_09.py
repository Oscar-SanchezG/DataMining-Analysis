# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 03:57:31 2021

@author: oscar

@Description: Dictionaries
"""

# Python dictionaries
#A dictionari is an ordered collection of pairs key:value. they are optimized to retrieve information.
#Key must be of an immutable type (not a list, set or dictionary)
#Keys are unique, there could not be two keys with different values.
#Values could be of any type
#A dictionary is similar to an array (or a list), but instead of an index to access an object, we be use key.
d = {} #Empty dictionary
d = {'uno':'value','number':2, 3:'test'} #Dictionary with three pairs
print(d['uno'])                          #The value is accsed by its key
print(d['number'])                       #The object between [] is the key not an index, sice dictionaries  are unordered (do not keep the insertion order)
print(d.get('uno'))                     #Similar to d[key]
d['uno'] = 1378                         #Change the value associated with a key
d['uno'] = 'Hello World!'               #Value associated with an existing key is overwritten
d['five'] = 5                           #Add an element to a dictionary, simply put the key between [] and the value to the right of =
d.update({6:'six','eight':'hello',9:1890}) #Add several elements to a dictionary
d.pop(9)                                #Removes the pair with the specified key. It returns the value and delete the pair
print(len(d))                           #Number of pairs in a dictionary
del d['eight']
d.clear()                               #Delete all the pairs in a dictionary
l = ['key1', 'key2', 'key3']            #A list of keys
d = dict.fromkeys(1, 0)                 #Creates a dictionary using the list of keys an a value of 0 for all the keys
#dict is a reserved word for dictionaries
d = dict(brand='ford', model='Mustang', year=1964) #Creating a dictionary with dict
#Note that keys are not string literals
#note the use of equals rather than colon for the assignment

if 'brand' in d:     #Check if a key exists in a dictionary
    print('Yes!')
    
Keys = list(d.keys()) #Return a list with all the keys
values = list(d.values()) #Return a list with all the values
items = list(d.items()) #Return a list fill with tuples of key, value

#Accesing pairs in a dictionary
for k in d:     #A dictionary is an iterable, we first access the key
    print(k,d[k])   #Accessig the value associated with the key
    
for k,v in d.items():   #Accessing key and value at the same time
    print(k,v)
    
#Importan, since dictionaries are unordered, do not assume the are returned in insertion order
d_n = {1:'Geeks', 2:'for', 3:{'A':'Welcome', 'B':'to', 'C':'Geeks'}} #Nested dictionaries 
d_l = {1:['one', 'two', 'three'], 2:['four', 'five', 'six'], 3:['seven', 'eight', 'nine']} #A dictionary of list

#1. Dada una lista con strings, escribe un programa usando una comprensión de listas 
#para generar una lista que contenga las longitudes de cada string de la lista original.
l = ['hola', 'que', 'tal', 'mundo']
l_new = [len(i) for i in l]

#2. Dada una lista con strings, escribe un programa usando una comprensión de listas 
#para generar una lista que contenga aquellos strings que contengan un punto.
l = ['hola', 'que', 'tal.', 'mun.do']
l_new = [word for word in l if '.' in word]

#3. Dado un string, escribe un programa para separarlo por espacios y usando una 
#comprensión de listas seleccione solo aquellos substrings cuya longitud sea menor a 20.
s ='supercalifragilisticoespialidoso aunque suene extravagante si lo dice con soltura'
l_s = s.split() 
l = [word for word in l_s if len(word) < 20]

#4. Dada una lista llena con enteros, escribe un programa usando una comprensión 
#de lista para generar una lista llena con True o False si cada entero es mayor 
#que un número dado (definelo tú).
n = 20
l = [14, 167, 98, 34, 20, 74]
l_new = [True if num > n else False for num in l]

#5. Escribe un programa que tome un diccionario con llaves string y valores 
#strings y números (definido por ti) y que devuelva la suma y promedio de todos los 
#valores que son numéricos.
somme = 0
count = 0
d = {'uno':3, 'dos':4, 'tres':10, 'cinco':'cuatro', 'seis':'siete'}
for k, v in d.items():
    if type(v) == int:
        somme += v
        count += 1

print("The sum is: ", somme)
print("The mean is: ", somme/ count)

#6. Dadas dos listas llenas con strings y números, escribe un programa que genere 
#un diccionario donde las llaves son los objetos de la primera lista y los valores los 
#objetos de la segunda.
l_one = ['hola', 'que', 'Python', 4, 10]
l_two = [12, 90, 'tal', 13, 67]
d = {}
for k, v in zip(l_one, l_two):
    d[k] = v

#7. Dados dos diccionarios (definidos por ti), escribe un programa que devuelva una 
#lista con las llaves que ambos comparten.
l_new = []
d_one = {'hola':10, 'mundo':43, 'que':38, 3:9, 1:'tal'}
d_two = {'hola':10, 'sabe':43, 'que':38, 56:9, 1:'tal'}
for k_one, k_two in zip(d_one.keys(), d_two.keys()):
    if k_one == k_two:
        l_new.append(k_one)

#8. Dado un string, escribe un programa que lo separe en palabras (una palabra es 
#todo lo que está entre espacios) y devuelva un nuevo string con las palabras únicas del 
#primer string.
d = {}
s ='hola que tal como esta? hola que tal'
s = s.split()
for word in s:
    d[word] = d.get(word, 0) + 1
    
s_new = ' '.join(d.keys())