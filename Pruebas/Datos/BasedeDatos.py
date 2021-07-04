# Ejecuten en CMD  
# "pip install pandas" 
# "pip install xlrd"
# "pip install openpyxl"

import pandas as pd 
import numpy
import os
import pathlib
import datetime
# Se importa la ruta donde se encuentra la base de datos
def rutaa(filename):
    ruta = str(pathlib.Path(__file__).parent.resolve()) # Obtiene la ruta del directorio 
    ruta = ruta.replace(chr(92),'/')+'/'+filename # 
    return ruta

def BasedeDatos(filename, medi): # filename es el nombre de la base de datos, medi es la hora a la que se toma la medicina 
    ruta = rutaa(filename) # Obtiene la ruta completa donde está el archivo xlsx de la base de datos 
    data = pd.read_excel(ruta) # pd.read_excel abre el archivo con la ruta dada 
    tabla = data.values # Obtiene los valores y los devuelve como un array 
    tabla = tabla.tolist() # Convierte el array a una lista de python 
    tabla.pop(0) # Borra los encabezados de  la base de datos
    n=len(tabla)
    for i in range(n): 
        tabla[i].pop(0) # Elimina la primera comlumna 
    for i in range(n): 
        tabla[i][3] = str(tabla[i][3]).lower() # Convierte los string de la comlumna 4 a minusculas 
    i = 0 
    while i < n: 
        nan = f'{tabla[i][2]}'
        if nan == 'nan':
            tabla.pop(i) # Elimina las filas que tengan un elemeneto nan
            n = len(tabla)
        i+=1 
    # Filtrado de datos de comida
    # Ayuno = 0
    # Desayuno = 1
    # Almuerzo = 2
    # Cena = 3  
    n=len(tabla)
    for i in range(n): 
        if tabla[i][3] == 'ayuno':
            tabla[i][3] = 0
        elif tabla[i][3].find('desayun') >= 0: 
            tabla[i][3] = 1
        elif tabla[i][3] == 'almuerzo': 
            tabla[i][3] = 2
        elif tabla[i][3].find('almuerzo') >= 0: 
            tabla[i][3] = 1   # Si encuentra almuerzo es 1, solo ha desayunado 
        elif tabla[i][3] == 'cena': 
            tabla[i][3] = 3
        elif tabla[i][3].find('cena') >= 0: 
            tabla[i][3] = 2  # Si encuentra cena es 2, solo ha almorzado   

    for row in tabla: 
        t = str(row[2]) # Convierte la hora de tipo datetime.time(H, M) a string 'h:m:s'
        (h, m, s) = t.split(':') # Separa las horas, los minutos y los segundos.
        row[2] = int(h) + int(m)/60 - medi # Covierte la hora a decimal tomando como cero la hora a la que se toma la medicina 
    return tabla 

table = BasedeDatos('datos.xlsx',8)
for row in table: 
    print(row)

print('')
print('')
print('')
def muestra(date1, date2, tabla): 
    lista = []
    for row in tabla: #selecciona los datos que están en el rango de fechas 
        if date1 <= row[0] and row[0] <= date2: 
            lista.append(row) 

    if len(lista) <= 10: 
        return lista
    
    return lista

"""
lista = []
for row in table: #selecciona los datos que están en el rango de fechas 
    if datetime.datetime(2020, 6, 1, 0, 0) <= row[0] and row[0] <= datetime.datetime(2020, 6, 10, 0, 0): 
        lista.append(row)
"""
lista = muestra(datetime.datetime(2020, 6, 1, 0, 0), datetime.datetime(2020, 6, 30, 0, 0), table)
for row in lista: 
    print(row)


