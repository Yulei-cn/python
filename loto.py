import numpy as np
import random
import operator
np.random.seed(20)
x = list(range(1,45))
loto = np.random.choice(x,5,replace=False)

print (loto)
nrb = int(input("entrez combien "))
nombre=0
for i in range (nrb):
    x1 = list(range(1,45))
    loto1 = np.random.choice(x,5,replace=False)
    occu = trouve

print("!!!!loto!!!!")
print(nombre)
