
mots=str.lower(input("Exemples de palindromes : "))

join = ''
for char in mots:
    if char.isalpha():
        join += char
print(join)