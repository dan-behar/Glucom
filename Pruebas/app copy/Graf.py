import matplotlib.pyplot as plt
import numpy as np
import pathlib
import sympy as sym
#matplotlib es para grafica, numpy vectoriza python

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

    plt.show()
    #exportador de grafica
    ruta = str(pathlib.Path(__file__).parent.resolve()) # Obtiene la ruta del directorio 
    ruta = ruta.replace(chr(92),'/')+'/static/grafica.png' # Ruta final con el nombre del archivo
    fig.savefig(ruta)

