#Ejercicio 1.7

import random

import numpy as np

b=0
m=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for a in range (20):
    
    b=random.randint (0,10)
    m [a]=b

print(m)

for c in range (20):
    
    if m [c]%2==0:
    
        print ("Número Par ", m [c])
        
    else:
    
        print ("Número Impar ", m [c])