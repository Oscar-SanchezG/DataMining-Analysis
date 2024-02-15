# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 19:25:33 2021

@author: EDUARDO

@Description: More about Pandas
"""

import matplotlib.pyplot as plt
import pandas as pd

w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
f_i = w_d + 'info_students.csv'
df = pd.read_csv(f_i) #Create a DataFrame from  a CSV file

print(df.describe()) #Returns some statistical info about the data

print(df[['age', 'semester']].describe())
df.boxplot(column='age')
df.boxplot()
df[['age', 'semester']].boxplot()

ageMean = df['age'].mean() #Computes average on the data in 'age' column
ageMedian = df['age'].median() #Computes median on the data in the 'age' column
print(df[['age', 'semester']].mean())
print(df[['age', 'semester']].median())
print(df[['age', 'semester']].quantile(.25))

print(df['age'] > 21) #Applies the comparator to very element in the column
                        #and returns the boolean results
                        
sex_filter = (df['sex'] == 'm') #it can be saved and used as a filter
age_filter = (df['age'] > 21) #it can be saved and used as a filter
null_filter = (df['age'].notnull()) #returns not-null values

print(df[sex_filter])
print(df[age_filter])
print(df[null_filter])

print(df.sort_values(by='age')) #ordena conforma a una columna

console_filter = (df['videogame_console'] == 'y')
sex_console_filter = (df['videogame_console' == 'y'] & (df['sex'] == 'm'))
print(df[sex_console_filter])
sex_console_filter = (df['videogame_console' == 'y'] & (df['sex'] == 'h'))
print(df[sex_console_filter])

print(df[sex_console_filter][['age', 'semester']])
print(df[sex_console_filter][['age', 'semester']].describe())
df[sex_console_filter].boxplot(column = 'age')
df[sex_console_filter][['age', 'semester']].boxplot()

# Dataframes can be plotted
df[sex_console_filter].plot(x='age', y='semester', kind='scatter')

df.hist()
df['age'].hist()
df[sex_console_filter].hist('age')
df[sex_console_filter].hist('age', 'semester')

m_filter = (df['sex'] == 'm')
h_filter = (df['sex'] == 'h')











