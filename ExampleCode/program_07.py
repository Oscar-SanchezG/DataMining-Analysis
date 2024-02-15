# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 03:29:39 2021

@author: oscar

@Description: Built-in functions
"""

#Some useful built-in functions
x=-16
print(abs(x))       #Absolute value
print(bin(x))       #Convertion to binary (as string)
print(format(x, 'b')) #Convertion to binary (as string) without prefix 0b
print(bool(x))      #Check if the value exist
print(bool(0))
print(chr(100))     #Unicode char for integer i
print(dir())        #List of names in the current local scope
print(dir(x))       #List of valid attibutes for the object
print(divmod(10,3)) #Return qoutient and remainder of the division of two numbers

# Enumerate objects from a collection
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, v in enumerate(seasons, start=10):
    print(i, v)
print(list(enumerate(seasons)))
#Return an enumerate object, produce tuples of count and values
print(list(enumerate(seasons, start=10)))
#Return an enumerate object produce tuples of count and values, starting at a certian value 
print(format(x,'o')) #Convert the value to a formatted representation
print(hasattr(x, 'imag')) #Check if the object has a specific attribute

a = [1,6070,34,14,183,3224,383]
b = ['a','b','c','d','e','zapato']
c = [1.4, 2.5, 3.6]

print(max(a)) #Return largest item in a collection(list, set, tuple, dict),
#objects in the collection must be of the same type
print(max(b))
print(min(a)) #Return smallest item in a collection
print(min(b))
print(ord('a')) #Integer for an Unicode char
print(pow(2,4)) #Return x to the power y
print(list(reversed(a))) #Reverse an ordered iterable
print(round(10.5698,2)) #Round a number to a precision
print(sorted(a)) #Return a sorted list from an iterable
print(sum(a)) #Sum the elements of an iterable 
print(sum(a, 1000)) #sum the elements fo an iterable and start
for i, j in zip(b, a):
    print(i,j)
print(list(zip(a, b, c)))

print(list(zip(a,b))) #Aggregates elements from each of the iterables stops
#at the shortest iterable 
del a,b  #Delete variables from the evironment