import math
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import pathlib
#matplotlib es para grafica, numpy vectoriza python

def reglin(x,y):
    n=len(x)

    if len(y)!= n:
        print("DEBE DE HABER LA MISMA CANTIDAD DE VALORES EN AMBOS VECTORES")
    
    sx=sum(x) #suma de todo el vector x
    sy=sum(y) #suma de todo el vector y
    #sumatorias cuadraticas
    sx2=0
    sxy=0
    sy2=0
    for i in range(n):
        sx2+=(x[i]*x[i])
    
    for i in range(n):
        sxy+=(x[i]*y[i])

    for i in range(n):
        sy2+=(y[i]*y[i])

    pendiente=((n*sxy-sx*sy)/(n*sx2-sx**2))
    intercepto = sy/n-pendiente*sx/n

    r2=((n*sxy-sx*sy)/math.sqrt(n*sx2-sx**2)/math.sqrt(n*sy2-sy**2))**2 #coeficiente

    return pendiente,intercepto,r2


def graf(x,y,xp,yp):
    #necesario para exportar grafica
    fig=plt.figure()

    #graficador + etiquetas
    plt.plot(x,y,'b.',xp,yp)
    plt.xlabel('Tiempo')
    plt.ylabel('Glucosa en la Sangre') #se pone r para formato "raw" y los $ encierran el texto para armarlo mas legible

    plt.title('Relación Tiempo-Glucosa')
    plt.legend(loc=1)
    plt.grid(True)

    plt.xticks(np.linspace(-3,3,3)) #(punto inicial, punto final, cantidad de separaciones entre a y b)
    #si se quiere separar pero en y se escribe: plt.yticks

    #exportador de grafica
    ruta = str(pathlib.Path(__file__).parent.resolve()) # Obtiene la ruta del directorio 
    ruta = ruta.replace(chr(92),'/')+'/static/grafica.png' # Ruta final con el nombre del archivo
    fig.savefig(ruta)


def grafreglin(x,y,a):
    xp=np.linspace(min(x),max(x),2)
    yp=a[0]*xp+a[1]

    return yp,xp