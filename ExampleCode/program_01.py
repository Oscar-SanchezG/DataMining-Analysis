# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:01:11 2021

@author: oscar

@Description: Basic conditionals
"""

num = 10
if num >= 0:
    print("Positive or Zero")
    print('End!')
else:
    print("Negative number")
    print(num*10)
    
n = float(input("Enter a number")) # Always gets a string
if n >= 0:
    if n == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    print('Hola')
    
n = float(input('Enter a number')) #Always gets a string
if n > 0:
    print('Positive number')
elif n == 0:
    print('Zero')
else:
    print('Negative number')
    
