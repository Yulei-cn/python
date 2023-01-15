import os
import os.path
import time


file1 = input("Enter file1 : ")
file2 = input("Enter file2 : ")


if os.path.isfile(file1) and os.path.isfile(file2):
    size1 = os.path.getsize(file1)
    size2 = os.path.getsize(file2)
    print("Size of", file1, ":", size1, "bytes")
    print("Size of", file2, ":", size2, "bytes")


    time1 = os.path.getmtime(file1)
    time2 = os.path.getmtime(file2)
    if time1 > time2:
        print(file1, "est le fichier le plus récent.")
    else:
        print(file2, "est le fichier le plus récent.")
else:
    print("Un ou les deux fichiers n'existent pas.")
