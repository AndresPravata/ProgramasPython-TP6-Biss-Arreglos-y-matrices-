#Ejercicio 2.1

import numpy as np

m=np.random.randint (0,1,size=(4,3))

for f in range (4):
    for c in range (3):
    
        a=int(input("ingrese un número: "))
        m [f,c]=a
    
print(m)    