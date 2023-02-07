#Ejercicio 2.2

import numpy as np

m=np.random.randint (0,1,size=(5,4))

for f in range (5):
    for c in range (4):
    
        a=int(input("ingrese un número: "))
        m [f,c]=a
    
print(m) 

for f in range (5):
    for c in range (4):
        print(m[f,c])
   