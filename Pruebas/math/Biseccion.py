from numpy import arange 
import numpy as np
import sympy as sym

x=sym.Symbol('x')

def Bis(f,a,b):
    fa=f.subs(x,a)
    fb=f.subs(x,b)

    if fa*fb==0:
        return None
    else:
        p=(a+b)/2
        fp=f.subs(x,p)
        if fp==0:
            return p
        elif fa*fp<0:
            b=p
        else:
            a=p
            fa=fp

#prueba
vector = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
rango = arange(min(vector)-1, max(vector)+1, 0.3)
fx=x*x-1

anterior = 0.0 
actual = 0.0 
rangos = []
for i in range(len(rango)):
    anterior = actual 
    actual = fx.subs(x,rango[i])
    print([anterior,actual])
    if anterior*actual < 0: 
        rangos.append([rango[i-1],rango[i]])

print(rangos)
# print(Bis(fx,2.84217094304040e-14,-0.189999999999974))
# print(Bis(fx,-4.26325641456060e-14,0.209999999999952))

res = []
for i in rangos: 
    res.append(Bis(fx,i[0],i[1]))

print(res)
