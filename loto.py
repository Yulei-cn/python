import numpy as np
import random
np.random.seed()
x = list(range(1,45))
loto = np.random.choice(x,5,replace=False)
print (loto)
nrb = int(input("entrez combien "))
a=False
b=0
resulat=[]
for i in range (nrb):
  loto1 = np.random.choice(x,5,replace=False)
  index=0
  for ii in loto:
    if loto1[index] == ii:
      a=True
      break
    else:
      a=False
      break
  if a==True:
   resulat.append(i)
  else: 
   pass
print(len(resulat))


