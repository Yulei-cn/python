import numpy as np
np.random.seed(20)
x = np.array(range(1,46))
loto = np.random.choice(x,5,replace=False)
loto.sort()
print (loto)
nrb = int(input("entrez combien "))
resulat = []
for n in range (nrb):
  loto1 = np.random.choice(x,5,replace=False)
  loto1.sort()
  
  if np.all(loto == loto1):
    resulat.append(loto1)


print(len(resulat))
print(resulat)



