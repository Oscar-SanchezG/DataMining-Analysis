# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 02:37:23 2021

@author: oscar

@Description: objects identidiers and strings (as lists)
"""
#Identification of objects 
a = 5
print(id(a))        #id of object
b = 6
print(id(b))
b = 5               #Reference to an object that already exists
print(id(b))
a = [1, 2, 3]       #New collection of objects
print(id(a))
b = a               #Reference to an existing object
print(id(b))        #id of the referenced object
b.append(4)         #Modified the referenced object
print(a)
print(b)
b = []              #Create a new object
b.extend(a)
b.append(5)
print(id(b))

#Strings are inmutable list
#The objects (characters) in a specific index CANNOT be modified
s = 'Hello world!'
print(s)
print(s[3])     #Character at index 3
print(s[:5])    #Slicing: characters from index 0 to 5-1
print(s[5:])    #Slicing: characters from index 5 to end
print(s[:5:2])  #Slicing: characters from beginig, end , step 2
s[5] = 'd'      #Not possible because sthings are inmutable

s = 'Hello'
t = 'world!'
u = s+' '+t     #Concatenation
print(s*3)      #Repetition
print(len(u))   #length of string

#Comparing strings
a = 'Hello world!'
if a==s:
    print('yes')
else:
    print('no')

s = 'Hello'
a = 'hello'
if a > s:       #Comparison is done lexicographically i.e using ASCCI value of the character
    print('yes')
elif a < s:
    print('no')
else:
    print('Son iguales')

#Iterates over string
for i in s:     #i iterates over the characters of the string. A string is an iterable object
    print(i)    #i takes the characters in order(a string is a list, then it is  an ordered collection)

for i in s[2:3]:
    print(i)
    
for i in s[::-1]: #i iterates over the string from end to beginig
    print(i)

#Some usefull string methods
#Strings are inmutable, so the methods always return another string. They do
#not mnodify the current string.
s1 = 'Hello World from pyton world \t\n'
s2 = 'Alphabetic'
print('\n',s1.lower())  #Return the lowercase version of the string
print('\n',s1.upper())  #Return the uppercase version of the string
print('\n',s1.strip())  #Return the string with whitespace removed from the start and end
print('\n',s1.lstrip())  #Return the string with whitestapce removed from the strart
print('\n',s1.rstrip())  #Return the string with whitespace removed from the end
print('\n',s1.isalpha())  #test if all the chars in the string ara alphabetic chars
print('\n',s1.isdigit())  #test if all the chars in the string are digits
print('\n',s1.isspace())  #test if all the chars in the string are spaces
print('\n',s1.startswith('Hello'))  #test if the string starts with the given other string
print('\n',s1.endswith('Hello'))  #tests if the string  ends with the given other string
print('\n',s1.find('World'))  #Search for the given other string within s1, and returns the first index where it begins or -1 if not fount
print('\n',s1.replace('World', 'Everyone'))  #Replace all the occurences of the first string with the second string
