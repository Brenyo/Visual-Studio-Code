"""
szam = int(input("szám: "))
csekkosszeg = 0
while szam != 0:
    csekkosszeg += szam
    szam = int(input("szám: "))
print(csekkosszeg)

osszeg = 0
while True:
    szam = int(input("szám: "))
    osszeg += szam
    if szam == 0:
        break
print(osszeg)
i = 1
while i < 10:
    print(i, end=" ")
    i+=1
    
import random
print("* Fej vagy írás játék *\n")
while True:
    veletlen = random.randint(0,1)
    tipp = int(input("tipp: "))
    if veletlen == tipp:
        print("Gratulálok nyert!")
        break
    else:
        print("Nem talált!\n\nPróbálja újra!")

szoveg = "alma"
while True:
    szo = str(input("szó: "))
    szoveg += " " + szo
    if szo == "":
        break
print(szoveg)

import random
print("* Gondoltam egy számra egy és tíz között! *\n")
proba = 0
while True:
    veletlen = random.randint(1,10)
    tipp = int(input("tipp: "))
    if veletlen == tipp:
        print("Gratulálok nyert!")
        break
    elif tipp < veletlen:
        proba += 1
        print("Nem talált! Kissebb tipp!")
    elif tipp > veletlen:
        proba += 1
        print("Nem talált! Nagyobb tipp!")
    elif proba == 7:
        print("Elfogyott a próbálkozás!")
        break
#7 feladat
szam1 = int(input("1. szám: "))
szam2 = int(input("2. szám: "))
lepeskoz = int(input("Lépésköz: "))
if szam1 > szam2:
    for i in range(szam2, szam1, lepeskoz):
        print(i, end=" ")
elif szam1 < szam2:
    for i in range(szam1, szam2, lepeskoz):
        print(i, end=" ")
"""
#8 feladat
szam = int(input("szám: "))
while True:
    if szam != 0:
        osszeg = int(input("szám: "))
        osszeg *= szam
    else:
        print(osszeg)
        break