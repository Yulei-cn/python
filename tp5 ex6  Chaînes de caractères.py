def taille_chaine(T):
    return len(T)

T=str(input("Chaînes de caractères:"))
print(taille_chaine(T))


def pourcentage_voyelles(T):
    voyelles = 0
    for i in T:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            voyelles += 1
    return voyelles / len(T) * 100

print(pourcentage_voyelles(T),"%")



def chercher_sous_chaine(T, sous_chaine):
    index = T.find(sous_chaine)
    if index != -1:
        return index
    else:
        return "La sous-chaîne n'a pas été trouvée."

sous_chaine = "wagon"
print("les mots 'wagon' sont ",chercher_sous_chaine(T,sous_chaine),"ème place")

def nombre_occurrences(T, sous_chaine):
    return T.count(sous_chaine)

print("il y a",nombre_occurrences(T,sous_chaine))