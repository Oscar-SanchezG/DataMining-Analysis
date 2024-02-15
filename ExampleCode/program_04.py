# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:50:29 2021

@author: oscar

@Description: Lists
"""

#Lists are ordered collections of objects --> Insertion order matter -->
#Objects are indexed
#We can access objects by index
#Objects in a list do not have to be of the same type
#List are mutable objects. We cab change the objects in specific indexes
a = [1,2,3,4,5,6,7,8,9]     #A list of int objects int
b = [1, 2.2, 'Python', [1,2,3]]     #A list of different objects
c = []      #A empty list
print(a)
print(b)
print(a[0])         #Access the object at index 0
print(a[:5])        #Slicing: access the objects from index 0 to 5-1
print(a[2:6])       #Slicing: access the objects from index 2 to index 6-1
print(a[5:])        #Slicing: access the objects from index 5 to end
print(a[2:8:2])     #Slicing: access the objects from index 2 to 8-1 in steps of 2
print(a[-1])        #Access the last element
print(a[-2])        #Access the second-to-last element
print(a[-5])
print(b[3][2])      #Access the first element fo the list inside the first list
# Mutate the list
b[1] = 'hundred'    #Change the value of an element in a given index
b[-1] = 4.5         #Change the value of the last element
                    #(List are mutable)
                    
# Add elements to lists
b.append('two hundred')     #Add an object to the list at the end
c.append('hello')           #Add an object to the empty list
b.extend(['a','b','c','d']) #Extend a list with another list
d = b + ['e','f','g','h']   #Extend a list with another list, concatenation
                            #(Not recomended)
b.append(['i','j','k'])
print(len(b))               #Length of a list(number of objects in the list)
last = b.pop()              #Extract the last object fron the list
fifth = b.pop(4)            #Extract the object at a given index
print(b)
b.append('a')
print(b)
b.reomove('a')              #Remove the first occurence of 'a'
print(b)
print(b.index('b'))     #Get the index of the first occurrence of an object
print(b.index('b',2,5)) #Get the index of the first occurrence of an object
                        #between two indices
b.insert(3,2000)        #Insert an object in specific index
print('a' in b)         #Menbership operator(test if an object is inside a collection)
print('a' not in b)     #Menbership operator(test if an object is not inside)
e = a + b               #Concatenation
e = a*3                 #Repetition: the list is repeted 3 times
lista = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 1, 'a', 'b', [4,5,'h']]
print(lista.sort())     #Sort the objects in the list in place(it modifies the list)
                        #Objects have to be of the same type
print(lista.reverce)    #Reverce the order of the objects in the list in place(it modifies the list)
lista.clear()           #Remove all items from the list

# Useful functions/methods
print(len(a), len(b), len(c)) #Lengt of a list
last = b.pop() #Extract the last element from a list
fifth = b.pop(4) #Extract the element at index 4
b.append('a')

b.remove('a')       #Remove the first occurence of 'a'
b.index('c')        #Get the index of the first occurrence of 'c'
b.index('c', 2, 6)  #Get the index of the first occurrence of 'c' between two indexes
b.insert(3, 2000)   #Insert an element in a specific index

# Menbership operators (boolean): True/False
print('a' in b)     #Test if an elements is inside a collection
print('a' not in b) #Test if an element is not inside a collection

#Concatenation
e = a + c
#Repetition
f = a * 3   #The list a is repeated 3 times
print(f.count(1))   #Count the number of times an element appers in a list
f.sort()            #Sort the elements in a list in place(it modifies the list)
f.sort(reverse=True)#Sort the elements in a list in reverse order
                    #in place (it modifies the list)
                    #To apply the sort funtions, all elements inside the
                    #list MUST BE od the same type
                    
        
#Iterate over lists
for i in lista:         #i iterates over the objects of the list. A list is an iterable object
    print(i)

for i in lista[8:]:     #i iterates over a slice of the list.
    print(i)
    
for i in lista[::-1]:   #i iterates over the list From end to beginig
    print(i)    
    
for i in lista:         #i iterates over the objects of the list. A list is an iterable object
    print(i)
    
a = lista[8:]
a.reverse()
for i in a:
    print(i)

#List of lists
lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for i in lista:         #i iterates over the objects of lista
    print(i)            #i takes each objects from lista(i is a list)
    
for i in lista:         #i iterates over the objects of lista
    for j in i:         #j iterates over the objects of i
        print(j)        #j takes each objects from i(j is an int)
        

#6. Dada una lista de tres números enteros (crea una lista por tu cuenta), 
#  escribe un programa que determine si la lista está ordenada en orden ascendente 
#  o descendente.

#7. Dada una lista llena con números flotantes (crea una lista por tu cuenta), 
#   escribe un programa que calcule la suma y el promedio de todos los elementos.

#8. Dada una lista llena con números enteros (crea una lista por tu cuenta), 
#   escribe un programa que devuelva la lista original sin elementos duplicados.
