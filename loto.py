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

#无论顺序如何
import numpy as np
import random
np.random.seed(20)
x = list(range(1,5))
loto = np.random.choice(x,2,replace=False)
print (loto)
nrb = int(input("entrez combien "))
a=False
b=0
resulat=[]
for i in range (nrb):
  loto1 = np.random.choice(x,2,replace=False)
  print(loto1)
  for n in range(5):
    for i in loto:
      for ii in loto1:
          if i == ii:
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
