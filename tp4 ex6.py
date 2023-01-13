tab = [5, 2, 4, 8, 1, 3]
n = len(tab)

for i in range(n):
    for j in range(i+1, n):
        if tab[i] > tab[j]:
            tab[i], tab[j] = tab[j], tab[i]
    print(tab)

print(sorted(tab))
#faire l'ordre croissant

tab.sort()
print(tab)
#La réorganisation du contenu du conteneur 
#modifiera l'ordre d'origine dans le conteneur