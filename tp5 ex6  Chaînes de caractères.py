def taille_chaine(T):
    return len(T)

T=str(input("Chaînes de caractères:"))
print(taille_chaine(T))



'''
def pourcentage_voyelles(T):
    voyelles = 0
    total = 0
    while T[total] != 0:
        if T[total] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            voyelles += 1
        total += 1
    return voyelles / total * 100

def chercher_sous_chaine(T, sous_chaine):
    for i in range(len(T) - len(sous_chaine) + 1):
        if T[i:i+len(sous_chaine)] == sous_chaine:
            return i
    return -1

def nombre_occurrences(T, sous_chaine):
    occurrences = 0
    for i in range(len(T) - len(sous_chaine) + 1):
        if T[i:i+len(sous_chaine)] == sous_chaine:
            occurrences += 1
    return occurrences
'''