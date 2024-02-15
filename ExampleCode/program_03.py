# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:42:37 2021

@author: oscar

@Description: Basic while
"""

n=10
suma=0 #acumulador
i=0 #counter
while i<n:
	i=i+1  #Count
	suma += i  #Accumulate
print('The sum is', suma)

#Use break
n=10
suma=0  #Accumulator
i=0     #Counter
while i<n:
	i += i+1
	if i == 5:
		break
	suma += i
print('The sum is', suma)

#Use of continue
n=10
suma=0
i=0
while i<n:
	i=i+1
	if i==3 or i==5:
		continue
	suma += i
print('The sum is', suma)

#use of else
n=10
suma=0
i=0
while i<n:
	i=i+1
	if i == 11:
		break
	suma += i
	print(suma)
else:
	print('The sum is', suma)