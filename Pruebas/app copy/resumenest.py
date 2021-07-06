import numpy
from scipy import stats

def Media(x):
    media=numpy.mean(x)
    return media

def Mediana(x):
    mediana=numpy.median(x)
    return mediana

def Moda(x):
    arreglo=numpy.array(x)
    moda=stats.mode(arreglo, axis=None)
    resp=moda[0]
    fija=resp[0]
    return resp

def Maximo(x):
    maximo=max(x)
    return maximo

def Minimo(x):
    minimo=min(x)
    return minimo

def Desviacion(x):
    desviacion=numpy.std(x)
    return desviacion
