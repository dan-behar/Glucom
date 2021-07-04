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

#ejemplo
x=[1,2,4,5,7]
med=Media(x)
medi=Mediana(x)
md=Moda(x)
maxi=Maximo(x)
mini=Minimo(x)
des=Desviacion(x)

print(f'media: {med}\nmediana:{medi}\nmoda:{md[0]}\nmaximo:{maxi}\nminimo:{mini}\ndesviacion:{des}')