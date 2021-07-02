import numpy as np

#dx(1) = (y(2)-y(1))/(x(2)-x(1)); %Diferencia finita hacia adelante
#for i = 2 : n-1;
#dx(i) = (y(i+1)-y(i-1))/(x(i+1)-x(i-1)) %Diferencia finita centrada
#endfor
#dx(n) = (y(n) - y(n-1))/(x(n)-x(n-1)); %Diferencia finita hacia atras
#endfunction

def derivada(x,y):
    n  = len(x)
    dx=np.zeros_like(x)

    dx[1]=((y[2]-y[1])/(x[2]-x[1])) #adelante
    for i in range(n-1):
        dx[i]=((y[i+1]-y[i-1])/(x[i+1]-x[i-1])) #centrada
    dx[i]=((y[i]-y[i-1])/(x[i]-x[i-1])) #atras
    return dx

#ejemplo
x=[1,2,4,5,7]
y = [52,5,-5,-40,10]

ans=derivada(x,y)
print(ans)

#el resultado me da diferente a octave