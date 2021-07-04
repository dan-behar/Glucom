import pathlib
# Se importa la ruta donde se encuentra la base de datos
def ruta(filename):
    ruta = str(pathlib.Path(__file__).parent.resolve())
    ruta = ruta.replace(chr(92),'/')+'/'+filename
    return ruta

print(ruta('datos.xlsx'))