'''
x=int(input("Entrez un nombre N : "))
i = 0
n = 0
while i < x:
    print(i)
    i += 1
    n=i+i
print("la somme des N entiers naturels %d" %n)

n=100
while True:
    x=int(input("Entrez un nombre N : "))
    if x == n:
        break

i=0
li=[]
while i < 10:
    i += 1
    a=int(input("10 valeur:"))
    if a > 0 and a <20:
       li.append(a)
    else:
        print("entre 0 et 20")
        i -= 1
n1=0
n2=0
n3=0
for i in li:
    if i < 10:
        n1 += 1
    else:
        if i >= 15:
            n3 += 1
        else:
            n2 += 1
print("Le nombre de valeurs inférieur strictement à ",n1,
    "\nLe nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15",n2,
    "\ni<=15",n3)
    
x=int(input("donne la valeur:"))
i=0
n=0
a=0
while i < x:
    i += 1
    a=i-2
    n=i+i
    if n > x:
        print("alors le nombre N recherché est",a)
        break


import random
n=random.randint(1,100)
print(n)
while True:
    x=int(input("donne la valeur:"))
    if x<n:
        print("petit")
    else:
        if x>n:
            print("grand")
        else:
            print("egal")
            break

def func(n):
    res=n
    for i in range(1,n):
        res *= i
    return res


x=int(input("donnez la valeur:"))

print(func(x))

'''

while True:
    heured=int(input("les heures de début:"))
    if 0 <= heured <= 24:
        break
    else:
        print("les heures de début est incoun")
while True:
    heuref=int(input("les heures de fin:"))
    if 0 < heuref <= 24 and heured <= heuref:
        break
    else:
        print("les heures de fin est incoun")

T=0
t=0
prix1=0
prix2=0
if heured==heuref:
    T=t=1
    heuref=1+heured
    print("les heures de fin plus 1 heurs:",heuref)
    if 7<=heured<=17:
        prix1=2
    else:
        prix2=1
elif 7 < heured < 17 and 7 < heuref < 17:
    T= heuref - heured
    prix1 = T * 2
else:
    if 0 <= heured < 7 and 0 < heuref <= 7 or 17 <= heured < 24 and 17 < heuref <= 24:
        t = heuref-heured
        prix1= t * 1
    else:
        if 7 <= heured and 17 < heuref <= 24:
            t = heuref-17
            T = 17-heured
            prix2 = T * 2
            prix1 = t * 1
        else:
            t = 24-heured-10
            T = 10
            prix2 = T * 2
            prix1 = t * 1

prix=prix1+prix2



if prix1 > 0:
    print("%d heure(s) au tarif horaire de 1.0 euro(s)" %(t))
else:
    pass
if prix2 > 0:
    print("%d heure(s) au tarif horaire de 2.0 euro(s)" %(T))
else:
    pass



print("Le montant total à payer est de %d euro(s)"%prix)
