#无论顺序如何
import numpy as np
import random
np.random.seed(20)
x = list(range(1,46))
loto = np.random.choice(x,5,replace=False)
print (loto)
nrb = int(input("entrez combien "))
a=False
b=0
resulat=[]
for i in range (nrb):
    loto1 = np.random.choice(x,5,replace=False)
    y=0
    for i in loto:
        if i in loto1:
           y+=1
    if y==5:
        print(loto1)
        resulat.append(loto1)

        
print(len(resulat))
print(resulat)