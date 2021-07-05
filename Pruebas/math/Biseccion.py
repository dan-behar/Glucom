import numpy as np
import sympy as sym

x=sym.Symbol('x')

def Bis(f,a,b):
    fa=f.subs(x,a)
    fb=f.subs(x,b)
    print(fa)
    print(fb)

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
fx=x*x-1
res=Bis(fx,-2,0)
print(res)