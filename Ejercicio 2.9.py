#Ejercicio 2.9

import random

import numpy as np

a=np.random.randint (0,9,size=(4,3))
b=np.random.randint (0,9,size=(4))
c=np.random.randint (0,9,size=(3))

b [(0)]=a [(0,0)] + a [(0,1)]+ a[(0,2)]
b [(1)]=a [(1,0)] + a [(1,1)]+ a[(1,2)]
b [(2)]=a [(2,0)] + a [(2,1)]+ a[(2,2)]
b [(3)]=a [(3,0)] + a [(3,1)]+ a[(3,2)]

c [(0)]=a [(0,0)] + a [(1,0)]+ a[(2,0)]
c [(1)]=a [(0,1)] + a [(1,1)]+ a[(2,1)]
c [(2)]=a [(0,2)] + a [(1,2)]+ a[(2,2)]

print (a)
print (b)
print (c)
