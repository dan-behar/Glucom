"""
function I = TrapecioM (x,y); 
  n = length(x); 
  suma= 0; 
  for i=1:n-1;
    h = x(i+1)-x(i); 
    suma = suma+(y(i+1)+y(i))*h;
  endfor
I=suma*0.5 
endfunction
"""

def TrapecioM (x, y): 
    n = len(x) 
    suma = 0 
    for i in range(n-1): 
        h = x[i+1]-x[i]
        suma+= (y[i+1]+y[i])*h
    return suma*0.5 


x=[1, 2, 4, 5, 7]

y=[52, 5, -5, -40, 10]

print(TrapecioM (x,y))