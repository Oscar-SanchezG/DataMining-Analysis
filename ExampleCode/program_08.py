# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 03:37:42 2021

@author: oscar

@Description: Tuples and sets
"""

#Python tuples
t = ('tuples', 'are', 'list', 'but', 'immutable', 4, [1,2])
#Tuple definition
print(t[0]) #Indexing
print(t[:3]) #Slicing
t[0] = 'assignments to elements in a tuple are not possible'
#Tuples are inmmutable
t = t +(9,)  #Merge of tupls. the ',' is necesary to indicate to python that
#it is  a tuple of only one object and not a number (9)
print('\nAdd sereral elements to tuple')
t = t + (10,11,'hello',10) #Marge of tuple. The ',' is no longer necessary
print(t.index(10)) #Return the index of the first occurence of object
print(t.count(10)) #Return the index the number of defined object
t_2 = t*2  #Repetition of tuples
t_3 = ('a', 'b')
x, y = t_3 #Tuple unpacking. Each object in the left takes an object from de tuple.
#we nedd to put as many objects in the left as object in the tuple

a = [(1,2), (3,4), (5,6)] #A list of tuples
b = ([1,2], [3,4], [5,6]) #A tuple of lists
c = tuple(a) #List to tuple
d = list(b) #tuple to list

for i in t: #Tuples are interables
    print(i)
    
for i in range(len(t)): #But can also be accesed by index
    print(t[i])
    
    
#Tuples ar faster than list. They are useful when a collection of objets are 
#not going to change durig the program execution

#####################
# Python sets
####################

a = set() #Empty set
a = {1, 2, 3, 4, 5.5, 1, 2, 3} #Set definition
a = {5, 1, 2, 3, 4, 5, 5, 3, 2, 1} #collection of unique objects,
#repeated objects are eliminated
print(a[0]) #Collection of unordered objects, so we cannot access objects by index
b={3, 4, 5, 6, 7, 8}
print(a.union(b)) #Return a set that is the union of two sets
print(a.intersection(b)) #Return a set that is the instersection of two sets
print(a.difference(b)) # Returne a ser that is the difference of two sets
print(b.difference(a))
b = {1,2}
print(b.issubset(a)) #Return True if b is b subset of a
print(a.issuperset(b)) #Retrun True if b is a superset of a
a.add('hola') #Add object to a set
a.update(['one','two','three']) #Add a list of objects to a set
a.remove(3) #Remove an object from a set(objects are unique)
a.pop() #Extract the last object from the set, Since sets are unordered,
#we dont know which object will be extracted

for i in a:    #Sets are interable
    print(i)   #But cannot be accessed by index
    
#Sets are faster than lists and tuples, they are useful when a collection 
#of objects contains only unique objects


#9. Dado un string (defínelo tú), escribe un programa que genere otro string compuesto por las dos primeras y las dos últimas letras del string original. Si la longitud del string original es menor que 2, que devuelva la leyenda "Empty string".

#10. Dado un string (defínelo tú), escribe un programa que remueva el enésimo caracter de ese string (definir n tú mismo). Comprobar que el string tiene más de n caracteres.

#11. Dada una lista llena con strings (crea una lista por tu cuenta), escribe un programa que devuelva cuál es el string más largo de la lista.

#12. Escribe un programa que cuente cuantas veces aparece el string 'bob' en un string dado (defínelo tú).
#13. Dado un string (defínelo tú), escribe un programa que genere otro string en donde todas las repeticiones del primer caracter son reemplazadas por el caracter $, excepto el primer caracter.
#14. Dada una lista llena con enteros y strings mezclados (crea una lista por tu cuenta), escribe un programa que separe en dos listas los strings de los enteros.
#15. Dada una lista con strings, escribe un programa usando una comprensión de listas para generar una lista que contenga las longitudes de cada string de la lista original.
#16. Dada una lista con strings, escribe un programa usando una comprensión de listas para generar una lista que contenga aquellos strings que contengan un punto.
#17. El ejercicio anterior, pero seleccionando solo aquellos strings que contengan 'jpg' o 'png' después del punto (solo esos tres caracteres).
#18. Dada una lista de tuplas, escribe un programa que ordene cada tupla dentro de la lista en orden descendente.
#19. Dadas tres listas llenas con números enteros, escribe un programa que encuentre todos los elementos que comparten las tres listas.

#20. Escribe un programa para encontrar los elementos repetidos dentro de una tupla y que genere una lista con ellos.
#Dado un número entero, escribe un programa que lo escriba con letras. 123 --> uno dos tres

#21. Escribe un programa que solicite un string de solo letras al usuario y que determine si el string es un heterograma, es decir un string en el que cada letra solo ocurre una vez.
