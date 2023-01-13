binome = ("login1", "login2")
print("L'étudiant " + binome[0] + " est en binome avec l'étudiant " + binome[1])

new_login1 = str(input("Entrez le nouveau login1: "))
new_login2 = input("Entrez le nouveau login2: ")
binome = (new_login1,new_login2)

#print("L'étudiant " + binome[0] + " est en binome avec l'étudiant " + binome[1])

binome = list(binome)
del binome[1]
binome = tuple(binome)
#new_login2 = str(input("Entrez le nouveau login2: "))

new_login3 = input("Entrez le nouveau login3: ")
binome = binome + (new_login3,)
print(binome)
