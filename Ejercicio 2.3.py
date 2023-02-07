#Ejercicio 2.3

import numpy as np

m=np.random.randint (0,1,size=(4,3))

for f in range (4):
    for c in range (3):
    
        a=int(input("ingrese un número: "))
        m [f,c]=a
    
print(m) 

for f in range (4):
    for c in range (3):
        print(m[f,c])
        
        
print ("La suma de la fila 1 es: "; m[(0,0)]+m[(0,1)]+m[(0,2)])
print ("La suma de la fila 2 es: "; m[1,0]+m[1,1]+m[1,2])
print ("La suma de la fila 3 es: "; m[2,0]+m[2,1]+m[2,2])
print ("La suma de la fila 4 es: "; m[3,0]+m[3,1]+m[3,2])

print ("La suma de la columna 1 es: ";m[0,0]+m[1,0]+m[2,0])
print ("La suma de la columna 1 es: ";m[0,1]+m[1,1]+m[2,1])
print ("La suma de la columna 1 es: ";m[0,2]+m[1,2]+m[2,2])
