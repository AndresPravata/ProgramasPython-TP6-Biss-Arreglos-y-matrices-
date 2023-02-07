#Ejercicio 1.10

import numpy as np

v= []

a=int(input("Por favor, coloque la cantidad de números a ingresar "))

for i in range (a):
    b=int(input("Por favor, ingrese los números "))
    v.append(b)

v.sort ()
a=a-1
        
print ("El número mayor es el ", v[a])