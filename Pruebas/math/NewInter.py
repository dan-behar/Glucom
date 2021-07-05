import numpy as np
import sympy as sym

def Newton(x,y,int):
    a=[]
    divDIF=[]
    if len(x) == len(y):
        n=len(x)
        a=[]
        a.append(y[0])

        divDIF = []
        divDIF.append([])
        for i in range (n-1):  
            divDIF[0].append((y[i+1]-y[i])/(x[i+1]-x[i]))
        
        for j in range (1,n-1):
            for i in range (0,n-j-1):
                if i == 0: 
                    divDIF.append([])
                
                divDIF[j].append((divDIF[j-1][i+1]-divDIF[j-1][i])/(x[j+i+1]-x[i]))

        for j in range (0,n-1):
            a.append(divDIF[j][0])
        
        return a
    else:
        return 0

#Prueba
chinga=[1,2,4,5,7]
damadre=[52,5,-5,-40,10]
a=Newton(chinga,damadre,9)
print(a)

x=sym.Symbol('x')

y=a[0]
for i in range (1,len(a)):
    t=a[i]
    for j in range(i):
        t=t*(x-chinga[j])
    y+=t

print(y)
print(y.subs(x,9))