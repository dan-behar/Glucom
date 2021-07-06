def TrapecioM (x, y): 
    n = len(x) 
    suma = 0 
    for i in range(n-1): 
        h = x[i+1]-x[i]
        suma+= (y[i+1]+y[i])*h
    return suma*0.5 
