from numpy import arange 
import numpy as np
import sympy as sym


gluco = [0, 1, 4]

minimo = min(gluco)
maximo = max(gluco)

print(minimo, maximo)

rango = []
n = minimo 
while n <= maximo:
    rango.append(n)
    n += minimo + 0.1
    
print(rango)

x=sym.Symbol('x')
y = x*x-2

for i in rango: 
    if abs(y.subs(x,i)) <= 0.001:
        print(i)
