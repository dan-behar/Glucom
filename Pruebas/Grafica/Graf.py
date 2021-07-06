import matplotlib.pyplot as plot
import seaborn as sb

edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

intervalos = range(min(edades), max(edades) + 2)

sb.displot(edades, color='#F2AB6D', bins=intervalos, kde=True) #creamos el gráfico en Seaborn

#configuramos en Matplotlib
plot.xticks(intervalos)
plot.ylabel('Frecuencia')
plot.xlabel('Edades')
plot.title('Histograma de edades - Seaborn - codigopiton.com')

plot.show()