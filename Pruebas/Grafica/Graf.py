import matplotlib.pyplot as plt
import numpy as np
#matplotlib es para grafica, numpy vectoriza python

#necesario para exportar grafica
fig=plt.figure()

x=np.linspace(-3,3,51)
y=x**2

#graficador + etiquetas
plt.plot(x,y,'b.',label=r'$y_1$')
plt.xlabel('x')
plt.ylabel(r'$y=x^2$') #se pone r para formato "raw" y los $ encierran el texto para armarlo mas legible

plt.title('f(x)')
plt.legend(loc=1)
plt.grid(True)

plt.xticks(np.linspace(-3,3,14)) #(punto inicial, punto final, cantidad de separaciones entre a y b)
#si se quiere separar pero en y se escribe: plt.yticks

#linea horizontal o vertical
plt.axhline(4,color='r',lw=2)
#si se quiere la linea recta vertical es: plt.axvline. Horizontal: plt.axhline

plt.show()
#exportador de grafica
fig.savefig('grafica.png')