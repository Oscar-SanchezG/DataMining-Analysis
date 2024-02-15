# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 20:37:03 2021

@author: EDUARDO

@Description: Leer el archivo con los datos de los estudiantes y para todas
las variables intervalo/razon, obtener el resumen de los cinco numeros:
minimo, maximo, 1er cuartil, mediana, 3er cuartil (graficar el boxplot), media,
varianza, desviacion estandar. (todo lo del ejercicio previo). Generar un histograma
con n bins.

para hacerlo sectorizado por genero (h/m), consola(y/n),
mascota(dog/cat/other/n), mascota(y/n)
"""

import matplotlib.pyplot as plt
import pandas as pd

def split_column(df, l_v, val):
    l_v_t = [x for x in l_v]
    l_v_t.append(val)
    records = df[l_v_t].to_records(index=False)
    records = list(records)
    values = []
    for record in records:
        r = []
        if '/' in record[-1]:
            op = record[-1].split('/')
            for o in op:
                r = [e for e in record]
                r[-1] = o
                values.append(r)
        else:
            r = [e for e in record]
            values.append(r)
    df_out = pd.DataFrame(values)
    df_out.columns = l_v_t
    return df_out 

def plots_pandas(df, var, val):
    groups = df.groupby(val)[var].apply(list)
    titles = list(groups.keys())
    n_g = len(groups)
    fig, axs = plt.subplots(1, n_g) 
    for i, (group, title) in enumerate(zip(groups, titles)):
        group.sort()
        x = list(range(len(group))) 
        axs[i].scatter(x, group)
        axs[i].set_title(title)
    plt.suptitle(f'{var} by {val}')
    plt.figure()
    df.boxplot(column=[var],by=val)
    plt.figure()
    df[var].hist(bins=8, by=df[val])
    plt.suptitle(f'{var} by {val}')
    
def summary_pandas(df, l_v, val):
    # Extarct unique values
    labels = df[val].unique().tolist()
    # Iterate over list of interval/ratio variables
    for v in l_v:
        for label in labels:
            label_filter = df[val] == label
            print(f'--Valores completos para {label} para la variable {v}--')
            print(df[label_filter][v].describe())
            print('--------------------------------------------------------')
            #Datos recortados
            #a = 10
            #print(f'+++ Valores recortados para {label} para la variable {v} al {a}% +++ ')
            #n = df[v].count()
            #k = int(a/100*n)
            #df_trim = df.sort_values(by=v, ignore_index=True)
            #df_trim = df_trim[k:n-k]
            #print(df_trim[label_filter][v].describe())
            #print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #print('**********************************************************')
        plots_pandas(df, v, val)
        #plots_pandas(df_trim, v, val)
    
        
w_d = 'C:/Users/EDUARDO/Documents/Mineria de datos/Data/'
i_f = w_d + 'info_students.csv' 
df = pd.read_csv(i_f) # Create a DataFrame from a CSV file    
    
# lista de variables intervalo/razon
l_v = ['age', 'height', 'weight', 'semester', 'courses_taken']
l_v = ['age']

#Using pandas
#Group data using sex (h/m)
summary_pandas(df, l_v, 'sex')

#Group data using console (y/n)
#summary_pandas(df, l_v, 'videogame_console')

#Group data using pet (cat/dog/other)
#df_out = split_column(df, l_v, 'pet')
#summary_pandas(df_out, l_v, 'pet')
    
    
    
            