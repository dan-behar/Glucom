import math
import numpy as np

def RegLin(x,y):
    n=len(x)

    if len(y)!= n:
        print("DEBE DE HABER LA MISMA CANTIDAD DE VALORES EN AMBOS VECTORES")
    
    sx=sum(x) #suma de todo el vector x
    sy=sum(y) #suma de todo el vector y
    #sumatorias cuadraticas
    sx2=0
    sxy=0
    sy2=0
    for i in range(n):
        sx2+=(x[i]*x[i])
    
    for i in range(n):
        sxy+=(x[i]*y[i])

    for i in range(n):
        sy2+=(y[i]*y[i])

    pendiente=((n*sxy-sx*sy)/(n*sx2-sx**2))
    intercepto = sy/n-pendiente*sx/n

    r2=((n*sxy-sx*sy)/math.sqrt(n*sx2-sx**2)/math.sqrt(n*sy2-sy**2))**2 #coeficiente

    return pendiente,intercepto,r2

def GrafRegLin(x,y,ejemplo):
    xp=np.linspace(min(x),max(x),2)
    yp=ejemplo[1]*xp+ejemplo[2]

    return xp,yp




#ejemplo
x = [1,2,4,5,7]
y = [52,5,-5,-40,10]

ejemplo=RegLin(x,y)
print(type(ejemplo))

ejemplo2=GrafRegLin(x,y,ejemplo)
print(ejemplo2)
