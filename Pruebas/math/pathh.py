import os
# path = os.getcwd()
ruta = os.getcwd().replace(chr(92),'/')
print(ruta.replace(chr(92),'/'))

print(f'{ruta}/datos.xlsx')

import pathlib
ruta = pathlib.Path(__file__).parent.resolve()

print(str(ruta).replace(chr(92),'/'))
