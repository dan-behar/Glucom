import numpy as np

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
        
        """
        Yinter=a[0]
        xn=1
        for k in range (2,n):
            xn=xn*(Xint-x[k-1])
            Yinter=Yinter+a[k]*xn

        return Yinter
        """
    else:
        return 0

#Prueba
x=[1,2,4,5,7]
y=[52,5,-5,-40,10]
print(Newton(x,y,9))