# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:04:35 2021

@author: EDUARDO
"""

#lista variables intervalo/razon
#l_v = [salary', 'hours_worked', 'days_worked']
l_v = ['']

#lista variables nominales
#of = df['offer'].tolist()
#st = df['state'].tolist()

#lectura datos
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'salaries1.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file

#discretizar
pet = df['pet'].tolist()
pet = ['y' if m != 'n' else m for m in pet]