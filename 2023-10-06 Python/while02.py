"""
osszeg = int(input("Kérem az összeget: "))
cimlet = 200
while osszeg > 5:
    db = osszeg // cimlet
    if db > 1:
        print(f"{cimlet}Ft: {db} db szükséges")
    osszeg %= cimlet
    match cimlet:
        case 200: cimlet = 100
        case 100: cimlet = 50
        case 50: cimlet = 20
        case 20: cimlet = 10
        case 10: cimlet = 5
    if cimlet == 200:
        cimlet = 100
    elif cimlet == 100:
        cimlet = 50
    elif cimlet == 50:
        cimlet =20
    elif cimlet == 20:
        cimlet = 10
    elif cimlet == 10:
        cimlet = 5

    
import random
Anna = "Anni"
Panna = "Panni"
dobas = int(input("Hány alkalommal legyen feldobás? "))

while True:
    if dobas > 0:
        for i in range(dobas):
            random1 = random.randint(1, 6)
            random2 = random.randint(1, 6)
            random3 = random.randint(1, 6)
            dobasosszertek = random1+random2+random3
            if dobasosszertek < 10:
                print(f"{random1} + {random2} + {random3} = {dobasosszertek}\t Nyert: {Anna}")
            else:
                print(f"{random1} + {random2} + {random3} = {dobasosszertek}\t Nyert: {Panna}")
    else:
        print("0-nál kissebbett nem lehet dobni!")
        break

#20. feladat:
igazHamis = False
while igazHamis == False:
    parosSzam = int(input("Kérek egy páros számot: "))
    if parosSzam % 2 == 0:
        print("A megadott szám megfelelő!")
        break
    else:
        igazHamis == False

#21. feladat:
igazHamis = False
while igazHamis == False:
    pSzam = int(input("Kérek egy pozitív számot: "))
    if pSzam > 0:
        print(f"Az osztás maradéka: {pSzam % 5}")
        break
    else:
        igazHamis == False

#22. feladat:
while True:
    hetnapja = int(input("Kérem a hét napját: "))
    if hetnapja >= 1 and hetnapja <= 7:
        break
if hetnapja == 1:
    print("Hétfő")
elif hetnapja == 2:
    print("Kedd")
elif hetnapja == 3:
    print("Szerda")
elif hetnapja == 4:
    print("Csütörtök")
elif hetnapja == 5:
    print("Péntek")
elif hetnapja == 6:
    print("Szombat")
elif hetnapja == 7:
    print("Vasárnap")

#23. feladat:
while True:
    szam = int(input("Kérek egy negatív számot: "))
    szam2 = int(input("Kérek egy páratlan számot: "))
    if szam < 0 and szam2 % 2 != 0:
        break
    else:
        print("Nem megfelelő számot adott meg!")

#24. feladat:
while True:
    szam = int(input("Kérek egy 3-mal és 5-el osztható számot: "))
    if szam % 3 != 0 and szam % 5 != 0:
        print("Nem megfelelő számot adott meg!")
    else:
        print(f"A szám harmada: {int(szam / 3)} ötöde: {int(szam / 5)}")

#25. feladat:
maradek = 0
while True:
    szam = int(input("Kérek egy számot: "))
    if szam > 0:
        maradek = szam % 5
        print(maradek)
        if maradek > 0:
            szam = maradek % 5
            print
    elif szam == 0:
        break
print(maradek)

#26. feladat:
while True:
    Vszam = int(input("Kérek egy valós számot: "))
    Vszam2 = int(input("Kérek még egy valós számot: "))
    if Vszam > Vszam2:
        print(f"{Vszam} nagyobb, mint {Vszam2}")
    elif Vszam < Vszam2:
        print(f"{Vszam2} nagyobb, mint {Vszam}")
    elif Vszam == Vszam2:
        print("Két szám ugyanaz")
        break

#27. feladat:
import random
while True:
    randomSZ = random.randint(1, 12)
    ujSZ = 0
    ujSZ = randomSZ % 3
    print(f"Random szám: {randomSZ} 3-mal osztva vett maradéka: {ujSZ}")
    valasz = str(input("Folytatni szeretné? "))
    if valasz == "i":
        print(f"Új szám: {ujSZ} 3-mal osztva vett maradéka: {ujSZ % 3}")
    elif valasz == "n":
        print("Vége a játéknak!")
        break
"""





