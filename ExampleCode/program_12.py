# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:19:03 2021

@author: EDUARDO

@Description: files and general usage of pandas
"""


import pandas as pd

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
f_i = w_d +'file_1.txt'
with open(f_i, 'r', encoding='utf-8') as f_r:
    text = f_r.read() #Read the whole file as a single string
    
text = []
with open(f_i, 'r', encondig='utf-8') as f_r:
    for line in f_r:
        text.append(line) #Read the file one line at time
        
#Every line in text file contains a \n at the end (except maybe the last one)
#Sometimes it is useful to remove such \n --> use strip() from strings
 
text = []
with open(f_i, 'r', encondig='utf-8') as f_r:
    for line in f_r:
        text.append(line.strip()) # Read the file one line at time
        
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv'
 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file
print(df.columns) # Show the comlums of the DataFrame

print(df['name']) # Accessing data using its column name

l = df['name'].tolist()

print(df[['name', 'age', 'height']]) #Accessing more than one comlumn, 
                                            #using a list of names
print(df.describe()) # Returns some statical info about the data

print(df['age'].describe())
print(df[['age', 'semester']].describe())
