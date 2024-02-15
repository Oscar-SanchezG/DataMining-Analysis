# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 03:16:33 2021

@author: oscar

@Description: String to list. List comprehensions
"""

s1 = 'Hello World! How ! are you?'
words = s1.split() #Return a list of substrings separated by the given delimiter.
#The delimiter is another string, with no arguments it splits on all whitespase chars
#---->String to list

words2 = ['Hola', 'mundo']
s2 = '*/!'.join(words2) #Return a string formed by the concatenation of all the strings
#in a list separated by a demiliter '*'----> Lists to string

#Create a new list with elements from an iterable
l_letters = []
for char in 'human':
    l_letters.append(char)
print(l_letters)

#Using list comprehesions
l_letters = [char for char in 'human']

#Using conditionals in a list comprehension
l_pairs = []
for x in range(20):
    if x % 2 == 0:
        l_pairs.append(x)
        
l_pairs = [x for x in range(20) if x % 2 == 0] #Select only those numbers from
#iterable that are pairs

#Nested conditionals
l_numbers = [y for y in range(100) if y % 2 == 0 if y % 5 == 0] #Selected only those
#numbers that are pairs and divisible by 5

l_numbers = []
for y in range(100):
    if y % 2 == 0:
        if y % 5 ==0:
            l_numbers.append(y)
        
#Alternatively, use logical operators
#Does the same as above
l_numbers = [y for y in range(100) if y % 2 == 0 and y % 5 ==0] 

l_numbers = []
for y in range(100):
    if y % 2 == 0 and y % 5 == 0:
        l_numbers.append(y)
        
#if ... else
# Create a list full of strings 'Even' or 'Odd' if the numbers are pairs or not
l_numbers = ['Even' if i % 2 == 0 else 'Odd' for i in range(10)] #Create a list full of
#strings 'Even' or 'Odd' if the numbers are pairs or not

#General sintax
#'['[object] | [[object] 'if' [expresion] else [object]] 'for' [object] 'in' [iterable]'<'if' [expresion]>]'
#Important
#1. List comprehension is an elegant way to define and create lists based on existing iterables.
#2. List comprehension is generally more comprac and faster than normal functions and loops for creating list.
#3. However, we should avoid writing very long list comprehesions in one line to ensure that code is user-friendly.
#4. Every list comprehesion can be rewritten in a for loop, but not every for loop can be
#rewritten in the form of list comprehesion 