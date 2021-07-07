#Funcion para apartado de meta glucosa
#Xint es el valor que va a ingresar el usuario
def LagrangePol(x,y,Xint):
    sum = 0
    n = len(x)

    for i in range(n):
        producto=y[i]
        for j in range(n):
            print(j,end=' ')
            if i is not j:
                producto=producto*((Xint-x[j])/(x[i]-x[j]))
        sum=sum+producto
    Yinter=sum
    return Yinter
"""
#ejemplo
dato = 8
x = [1,2,4,5,7]
y = [52,5,-5,-40,10]

prueba=LagrangePol(x,y,dato)
print(prueba)
"""