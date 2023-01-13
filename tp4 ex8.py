# create a dictionary to store personal information
personal_info = {"nom": "John", "name": "Smith", "promo": 2022, "group": 202}

# display the personal information
#print("votre nom est '{}', prénom est '{}', vous faites partie de la promo '{}' et votre groupe est '{}'".format(personal_info["name"], personal_info["firstname"], personal_info["promo"], personal_info["group"]))

personal_info2={"nom": "toto", "name": "titi", "promo": 2022, "group":202}
#personal_info["nom"] += " toto"

# display the keys of the dictionary
print("Les clés du dictionnaire sont :")
for key in personal_info.keys():
    print("-", key)

# display the values of the dictionary
print("Les valeurs du dictionnaire sont :")
for value in personal_info.values():
    print("-", value)

# display the items (keys and values) of the dictionary
print("Les tuplets du dictionnaire sont :")
for key, value in personal_info.items():
    print("-", "(", key, ",", value, ")")


print("L'étudiant {}  {}  {}  {}".format(personal_info["nom"], personal_info["name"], personal_info["promo"], personal_info["group"]), "\nL'étudiant {}  {}  {}  {}".format(personal_info2["nom"], personal_info2["name"], personal_info2["promo"], personal_info2["group"]))




