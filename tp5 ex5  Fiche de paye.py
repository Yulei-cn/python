t=input("entez combien heures : ")
while t!='-1':
    t=int(t)
    if t>=160 and t<=200:
        print("salaire: %d" % (160*10+(t-160)*10*25/100))
    elif t>200:
        print("salaire: %d" % (160*10+39*10*25/100+(t-200)*10*50/100))
    else:
        print("salaire: %d" % (t*10))
    t=input("entez combien heures : ")
