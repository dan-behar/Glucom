from derivada import derivada

def velocidad(x,y):
    vel=[]
    vel=derivada(x,y)
    return vel

def aceleracion(x,vel):
    ace=[]
    ace=derivada(x,vel)
    return ace

x = [1,2,4,5,7]
y = [52,5,-5,-40,10]

velocity=velocidad(x,y)
aceleration=aceleracion(x,velocity)

print(f'Las aceleraciones son:\n',aceleration)
maxima=max(aceleration)
minima=min(aceleration)
print(f'la aceleracion maxima:\n',maxima)
print(f'la aceleracion minimia:\n',minima)