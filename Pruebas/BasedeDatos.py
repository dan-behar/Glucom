# Ejecuten en CMD  
# "pip install pandas" 
# "pip install xlrd"
# "pip install openpyxl"

import pandas as pd 
import os
import pathlib
# Se importa la ruta donde se encuentra la base de datos
filename = 'datos.xlsx'
ruta = str(pathlib.Path(__file__).parent.resolve())
ruta = ruta.replace(chr(92),'/')+'/'+filename
print(f'---->{ruta}<----')
print(f'---->C:/Users/Cruz del Cid/Desktop/Glucom/Pruebas/datos.xlsx<----')


# pd.read_excel abre el archivo con la ruta dada 
data = pd.read_excel(ruta)

print(data)
tabla = data.values
# print(tabla[1][3])
# [fila][columna] 
print(tabla)