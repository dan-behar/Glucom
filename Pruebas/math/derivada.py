import numpy as np

#dx(1) = (y(2)-y(1))/(x(2)-x(1)); %Diferencia finita hacia adelante
#for i = 2 : n-1;
#dx(i) = (y(i+1)-y(i-1))/(x(i+1)-x(i-1)) %Diferencia finita centrada
#endfor
#dx(n) = (y(n) - y(n-1))/(x(n)-x(n-1)); %Diferencia finita hacia atras
#endfunction

def derivada(x,y):
    n  = len(x)
    print(n)
    dx=np.zeros_like(x)
    print(dx)

    dx[0]=((y[1]-y[0])/(x[1]-x[0])) #adelante
    print(dx)
    for i in range(n-2):
        dx[i+1]=((y[i+2]-y[i])/(x[i+2]-x[i])) #centrada
        print(dx)
    dx[n-1]=((y[n-1]-y[n-2])/(x[n-1]-x[n-1-2])) #atras
    print(dx[n-1])
    return dx

#ejemplo
x=[1,2,4,5,7]
y = [52,5,-5,-40,10]

ans=derivada(x,y)
print(ans)

#el resultado me da diferente a octave