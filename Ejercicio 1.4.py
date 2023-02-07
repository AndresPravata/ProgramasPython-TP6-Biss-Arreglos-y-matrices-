#Ejercicio 1.4

import random
import numpy as np

v1=np.random.randint (0,1,size=(5))
v2=np.random.randint (0,1,size=(5))

for c in range (5):
    
    a=int(input("ingrese un número: "))
    v1 [c]=a
    b=int(input("ingrese un número: "))
    v2 [c]=b

print(v1)

print(v2)