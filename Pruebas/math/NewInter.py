import numpy as np

def Newton(x,y,int):
    a=[]
    divDIF=[]
    if len(x) == len(y):
        n=len(x)
        a=[0]

        for i in range (1,n-1):
            divDIF=(y[i+1]-y[i])/(x[i+1]-x[i])
        
        for j in range (2,n-1):
            for i in range (1,n-j):
                divDIF[i,j]=(y[i+1,j-1]-y[i,j-1])/(x[j+i]-x[i])

        for j in range (2,n):
            a=divDIF(1,j-1)
        
        Yinter=a[0]
        xn=1
        for k in range (2,n):
            xn=xn*(Xint-x[k-1])
            Yinter=Yinter+a[k]*xn

        return Yinter

    else:
        return 0

#Prueba
x=[1,2,4,5,7]
y=[52,5,-5,-40,10]
print(Newton(x,y,9))