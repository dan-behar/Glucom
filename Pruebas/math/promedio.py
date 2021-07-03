
def Integral(x,y):
    n=len(x)
    h=x[2]-x[1]
    I=(0.5*(y[1]+y[2])*h)
    i=2

    for i in range (n-1):
        h=x[i+1]-x[i]
        I=I+0.5*(y[i]+y[i+1])*h
    return I

def Promedio(x,I):
    n=len(x)
    prom=I/n-1
    return prom

#ejemplo    
x = [1,2,4,5,7]
y = [52,5,-5,-40,10]

inte=Integral(x,y)
print(inte)
prome=Promedio(x,inte)
print(f'el promedio de aceleracion es:\n',prome)