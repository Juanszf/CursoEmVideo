import numpy as np

start = 0.001
stop = 0.031
step = 0.001
lista = np.arange(start,stop,step)

for i in lista:
    y = (5535.4*i)+33.262
    print(y)