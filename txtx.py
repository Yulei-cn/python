mm=float(da[1])
while True:
    if 0<mm<13:
        break
    else:
        print("pas au bon format :")
        date=str(input("donne une date : "))

yyyy=float(da[2])
while True:
    if 0<yyyy<1000:
        break
    else:
        print("pas au bon format :")
        date=str(input("donne une date : "))


dd=int(input("donne une date dd :"))
while True:
    if 0<dd<32:
        break
    else:
        print("pas au bon format :")
        dd=int(input("donne une date :"))

mm=int(input("donne une date mm :"))
while True:
    if 0<mm<13:
        break
    else:
        print("pas au bon format :")
        mm=int(input("donne une date :"))

yyyy=int(input("donne une date yyyy :"))
while True:
    if 0<yyyy:
        break
    else:
        print("pas au bon format :")
        yyyy=int(input("donne une date :"))
