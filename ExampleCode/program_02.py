# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:14:30 2021

@author: oscar

@Description: Basic for
"""

for i in range(11):
    print(i)
    
for i in range(1, 11):
    print(i)
    
for i in range(1, 11, 2):
    print(i)
    
#Use of break
for i in range(10):
    if i == 3:
        break
    print(i)
print('End')

#Use of continue
for i in range(10):
    if i == 3 or i == 5:
        continue
    print(i)
print('End')

#Use of else in for
for i in range(11):
    if i == 3:
        break
    print(i)
else:
    print('No numbers left.')

#Nested fors
for i in range(1, 11):
    for j in range(1, 11):
        k = i * j
        print(i, '*', j, '=',k)
        
#1. Solicitar n calificaciones flotantes, encontrar las calificaciones menor y mayor
n = int(input("Numero de claificaciones a ingresar:  "))
cal_men = 0.0
cal_may = 0.0
for i in range(1, n+1):
    if (n == 0):
        print('No se ingresaran calificaciones')
        break
    if (n == 1):
        aux = float(input("Ingrese la calificacion: "))
        cal_may = aux
        cal_men = aux
    else:
        aux = float(input("Ingrese la calificacion: "))
        if (aux <= cal_men):
            cal_men = aux
        if (aux >= cal_may):
            cal_may = aux
print('La calificacion mayor es:',cal_may)
print('La calificacion menor es:',cal_men)
        
#2. Una persona adquirió un producto para pagar en 20 meses. 
#   El primer mes pagó $10, el segundo $20, el tercero $40 y así sucesivamente. 
#   Calcular cada pago mensual y el total de lo que pagó después de los 20 meses.
pago = 10
pago_total = 0
for i in range (20):
    print('Total de pago mes',i, '=', pago)
    pago = pago*2
    pago_total += pago
print('Total a pagar es: ', pago_total)

#3. Una persona empieza a ahorrar 2 centavos el 1 de enero, 4 centavos el 2 de enero, 
#   8 centavos el 3, 16 el 4 y así sucesivamente hasta el 31 de diciembre. 
#   Calcular cuánto habrá ahorrado en PESOS al final del año (año no bisiesto).
total = 0
ahorro = 1
for i in range (365):
    ahorro *=2
    total += ahorro
print('Total ahorrado es $ ', total/100)

#4. Solicitar n números enteros y decir cuántos son pares, cuántos impares, 
#   cuántos negativos, cuantos positivos y cuántos ceros
par = 0
inpar = 0
neg = 0
pos = 0
cer = 0
n = int(input('Numero de numeros a evaluar: '))
for i in range(n):
    numbers = int(input('Ingresa el Valor: '))
    if (numbers % 2 == 0):
        par += 1
    else:
        inpar += 1
    if (numbers < 0):
        neg += 1
    elif (numbers > 0):
        pos += 1
    else:
        cer += 1
print('Total de numeros inpares es: ', inpar)
print('Total de numeros pares es: ', par)
print('Total de numeros negativos es: ', neg)
print('Total de numeros positivos es: ', pos)
print('Total de numeros Zeros es: ', cer)

        
#5. Escribir un programa que imprima los números pares entre 1 
#   y un número entero dado por el usuario
n = int(input('Numero limite: '))
for i in range(1, n+1):
    if (i % 2 == 0 ):
        print(i)
    
    

