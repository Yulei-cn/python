
while True:
    s1 = input("Donnez date (dd mm yyyy): ")
    date = s1.split(" ")
    day = int(date[0])
    month = int(date[1])
    yyyy = int(date[2])
    if 0<day<32 and 0<month<13 and 0<yyyy<10000:
        break
    else:
        print("pas au bon format:")

if (yyyy % 4 ) == 0:
    if (yyyy % 100 ) == 0:
        if (yyyy % 400 ) == 0:
            print("l’année est bissextile ")
        else:
            print("l’année n'est pas bissextile ")
    else:
        print("l’année est bissextile ")
else:
    print("l’année n est pas bissextile ")