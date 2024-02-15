# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 08:41:33 2022

@author: EDUARDO
1. Write a regular expression to capture all numbers in the string.
s = 'abc123xyz, define "123", var g = 123;'


2. Write a regular expression that captures the first three strings
but not the Last.
ls = ['cat.', '896.', '?=+.', 'abc1']

3. Write a regular expression to capture the first three words but not
the Last three in the string.
s = 'can man fan dan ran pan"

4. Using the (exclusion) operator, write a regular expression to capture
the first two words but not the Last one in the string:

s = "dog hog fog"

5. Write a regular expression to capture the first three words but not
the Last three in the string:
s = Ana Bob Cpc aax bby ccz

6. Write a regular expression to capture the first two words but not
the Last one in the string.
s = 'wazzzzzup wazzzup wazup'
"""

import re
#1
s = 'abc123xyz, define "123", var g = 123;'
l = re.findall('\d', s)
l = re.findall('\d+', s)

#2
ls = ['cat.', '896.', '?=+.', 'abc1']
for s in ls:
    l = re.findall('...\.', s)
    print(l)
    
#3
s = 'can man fan dan ran pan'
l = re.findall('[cmf]an', s)

#4
s = "dog hog fog"
l = re.findall('[^f]og', s)

#5
s = 'Ana Bob Cpc aax bby ccz'
l = re.findall('[ABC][a-z]{2}', s)

#6
s = 'wazzzzzup wazzzup wazup'
l = re.findall('waz{3,5}up', s)

s = 'hola estoy corriendo Saltando y Cantando Corr1iendo'
l = re.findall('ando|iendo', s) # 
