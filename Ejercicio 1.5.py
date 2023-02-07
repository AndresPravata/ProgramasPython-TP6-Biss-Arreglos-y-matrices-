#Ejercicio 1.5

import random

import numpy as np

b=0
d=0
m=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for a in range (20):
    
    b=random.randint (0,10)
    m [a]=b

print(m)

for c in range (20):
    
    d=d+m [c]

print(d)
