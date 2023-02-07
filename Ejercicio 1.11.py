#Ejercicio 1.11

import numpy as np

v= []

a=0

for i in range (10):
    b=101
    
    while (b<0 or b>100):
        b=int(input("Por favor, ingrese las notas "))
    v.append(b)

for c in range (10):
    a=a+v[c]
    
d=a/10

if d>= 60:
       
    print ("Aprobado")

else:
    print("Desaprobado")