import datetime 

fecha1 = datetime.datetime(2020, 6, 1, 0, 0)
fecha2 = datetime.datetime(2020, 6, 4, 0, 0) 

if fecha1 <= fecha2: 
    print('¡Funciona!')


t = str(datetime.time(8, 20))
print(t)
(h, m, s) = t.split(':')
result = int(h) + int(m) / 60 + int(s)/3600
print(result)