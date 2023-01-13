list=[]
sumc=0
sumn=0
moy=0.0
m=1
for i in range(5):
    s1=str(input("Veuillez entrer la note du module %s et le coefficient correspondant :" % m))
    s2=s1.split(" ")
    s3=float(s2[0])
    if s3<8:
        print(" n’est inférieure à 8")
        vaild=False
        continue
    s4=float(s2[1])
    sumn=s3*s4+sumn
    sumc=s4+sumc
    m+=1

if vaild == False:
    print("NON amdis")
else:    
    moy=sumn/sumc   
    print("moyenne générale :",moy)
    if moy >= 10:
        print("L’étudiant est admis")

