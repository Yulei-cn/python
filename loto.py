import numpy as np
import random
import operator
np.random.seed(20)
x = list(range(1,45))
loto = np.random.choice(x,5,replace=False)

print (loto)
nrb = int(input("entrez combien "))

resulat=[]
for i in range (nrb):
    x1 = list(range(1,45))
    loto1 = np.random.choice(x,5,replace=False)
    for i in loto:
        if i in loto1:
            resulat.append(i)

        
#print("!!!!loto!!!!")
#print(len(resulat))
#print(resulat)


#print (loto)
#nrb = int(input("entrez combien "))
#
#resulat=[]
#for i in range (nrb):
#    x1 = list(range(1,45))
#    loto1 = np.random.choice(x,5,replace=False)
#    if loto == loto1:
#        n += 1
#    else:
#        continue
#print("!!!!loto!!!!")
#print(n)
