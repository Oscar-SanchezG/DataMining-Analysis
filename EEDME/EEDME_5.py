# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 00:10:25 2022

@author: EDUARDO

5. Utilizando el mismo archivo titanic.csv, escribe un programa en Python que calcule la 
probabilidad condicional de morir dado que el pasajero viajó en 1a, 2a o 3a clase, utilizando 
las variables Pclass (1, 2, 3) and Survived (0, 1). La probabilidad condicional se calcula como

                                𝑃(𝐴∩𝐵)
                    𝑃(𝐴|𝐵) = --------------
                                𝑃(𝐵)

En donde 𝑃(𝐴|𝐵) es la probabilidad que A suceda (morir) dado B (ser hombre/mujer),
𝑃(𝐴 ∩ 𝐵) es la probabilidad que A (morir) y B (ser hombre/mujer) ocurran 
juntos, y 𝑃(𝐵) es la probabilidad de que B (ser hombre/mujer) ocurra. Las probabilidades 
se calculan dividiendo la frecuencia de un evento entre el total de eventos.

Ejemplo:
Dado: muere, clase 2
        muere, clase 2
        muere, clase 2
        sobrevive, clase 2
        muere, clase 1
        sobrevive, clase 1
        sobrevive, clase 1
        B = clase 2
        
Salida (para morir dado que es clase 2): 𝑃(𝐴 ∩ 𝐵) = 3/7, 𝑃(𝐵) = 4/7

            3/7         21
𝑃(𝐴|𝐵) =---------- =  ------- =  0.75
            4/7         28

Explicación: Hay 7 pares de datos en total. Hay 3 casos en que ser clase 2 y muere aparecen 
juntos por lo que 𝑃(𝐴 ∩ 𝐵) = 3/7. Finalmente, hay 4 casos en que aparece 2 en la clase por 
lo que 𝑃(𝐵) = 4/
"""
import pandas as pd


def cond_prod(values_1, values_2, l_1, l_2):
    n = len(values_1)
    num = den =0
    for v_1, v_2 in zip(values_1, values_2):
        if v_1 == l_1 and v_2 == l_2:
            num += 1
        if v_2 == l_2:
            den += 1
            
    num /= n
    den /= n
   
    cp = num/den
    return cp

def cond_prod_iter(values_1, values_2, lab_1, lab_2):
    for l_1 in lab_1:
        for l_2 in lab_2:
            p_c = cond_prod(values_1, values_2, l_1, l_2)
            print(f'Confitional probability of [{l_1}|{l_2}]= {p_c:.3f}')
    pass

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'titanic.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#lista variables nominales
pcl = df['Pclass'].tolist()
surv = df['Survived'].tolist()
#pet = ['y' if m != 'n' else m for m in pet]
surv_1 = set(surv)
pcl_1 = set(pcl)

print('-----------------------------------------------------------')
print('Conditional probability between Survived and Pclas')
cond_prod_iter(surv, pcl, surv_1, pcl_1)
print('-----------------------------------------------------------')

print('-----------------------------------------------------------')
print('Conditional probability between not-Survived and Pclas = 2')
rel =cond_prod(surv, pcl, 0, 2)
print(f'Confitional probability of 0 y 2= {rel:.3f}')
print('-----------------------------------------------------------')