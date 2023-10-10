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
#22 feladat:
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
"""
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