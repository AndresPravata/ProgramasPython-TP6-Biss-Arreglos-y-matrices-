#Ejercicio 1.13

import numpy as np

v= [(33,11,20,2,15,1,12,11,8,14,10)]
v2=[len(v)-1]
a=0
v.sort ()

print (v[0])

i=1

for i in range (len(v)):
    v2.append(v[i])

for c in range (len(v2)):
    a=a+v2[c]
    
d=a/(len(v2))
