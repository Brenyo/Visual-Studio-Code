"""
import random
import math
#2. feladat:
print("** Fej vagy írás **")
while True:
    randomszam = random.randint(0,1)
    tipp = int(input("Tipp: "))
    if tipp == randomszam:
        print("Sikeresen eltaláltad")
        break
    else:
        print("Nem talált, probálja újra")

#3. feladat:

#4. feladat:
szorzottszam = int(input("Kérek egy számot:"))
while True:
    szam = int(input("Kérek egy számot amivel szorzok:"))
    if szam == 0:
        break
    szorzottszam*=szam
print(szorzottszam)

#5: feladat:
gyumolcs = "alma"
while True:
    szo = input("Szó: ")
    gyumolcs+= " "+szo
    if szo =="":
        break

print(gyumolcs)

#6. feladat:
betu = input("Kérek egy betűt: ")
darabszam = int(input("Hányszor írja ki: "))
for i in range(darabszam):
    print(betu, end=" ")

#7. feladat:
kertszam = int(input("Kérek egy számot: "))
kertszam2 = int(input("Kérek egy számot: "))
lepeskoz = int(input("Kérek egy lépésközt: "))
kissebb = min(kertszam,kertszam2)
nagyobb = max(kertszam,kertszam2)
for i in range(kissebb, nagyobb+1, lepeskoz):
    print(i, end=" ")

#8. feladat:
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

#9. feladat:
osszeg = int(input("Kérem az összeget: "))
cimlet = 200
while osszeg > 5:
    db = osszeg // cimlet
    if db > 1:
        print(f"{cimlet}Ft: {db} db szükséges")
    osszeg %= cimlet
    #match cimlet: case 200: cimlet = 100 case 100: cimlet = 50 case 50: cimlet = 20 case 20: cimlet = 10 case 10: cimlet = 5
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

#10. feladat:
elso_elem = int(input("Kérlek add meg az első elemet: "))
differencia = int(input("Kérlek add meg a differenciát: "))
elemszam = int(input("Kérlek add meg az elemszámot: "))
sorozat = ""
for i in range(elemszam):
        elem = elso_elem + i * differencia
        sorozat += " " + str(elem)
print("A számtani sorozat:", sorozat)

#11. feladat:
N = int(input("Kérlek add meg a pozitív egész N számot: "))
osszeg = 0

for i in range(1, N+1, 2):
    osszeg += i

print("Az N-nél nem nagyobb pozitív páratlan számok összege:", osszeg)

#12. feladat:
n = int(input("Kérlek add meg a pozitív egész n számot: "))
faktorial = math.factorial(n)
print(f"{n}! = {faktorial}")

#13. feladat:
eredmeny = 0
szam1 = int(input("Kérlek add meg az első számot: "))
szam2 = int(input("Kérlek add meg a második számot: "))
for i in range(szam2):
    eredmeny += szam1

print(f"{szam1} * {szam2} = {eredmeny}")

#14. feladat:
eredmeny = 1
szam = float(input("Kérlek add meg a valós számot: "))
kitevo = int(input("Kérlek add meg a pozitív egész kitevőt: "))
for i in range(kitevo):
    eredmeny *= szam

print(f"{szam}^{kitevo} = {eredmeny}")

#15. feladat:
szam1 = int(input("Kérlek add meg az első pozitív egész számot: "))
szam2 = int(input("Kérlek add meg a második pozitív egész számot: "))
while szam2:
    szam1, szam2 = szam2, szam1 % szam2
print(f"A két szám legnagyobb közös osztója (LNKO): {szam1}")

#16. feladat:
def lnko(szam1, szam2):
    while szam2:
        szam1, szam2 = szam2, szam1 % szam2
    return szam1

def lkkt(szam1, szam2):
    return (szam1 * szam2) // lnko(szam1, szam2)

szam1 = int(input("Kérlek add meg az első pozitív egész számot: "))
szam2 = int(input("Kérlek add meg a második pozitív egész számot: "))

lkkteredmeny = lkkt(szam1, szam2)
print(f"A két szám legkisebb közös többszöröse (LKKT): {lkkteredmeny}")

#17. feladat:
def lnko(a, b):
    while b:
        a, b = b, a % b
    return a

szamlalo = int(input("Kérlek add meg a tört számlálóját: "))
nevezo = int(input("Kérlek add meg a tört nevezőjét: "))

lnko_eredmeny = lnko(szamlalo, nevezo)

egyszerusitett_szamlalo = szamlalo // lnko_eredmeny
egyszerusitett_nevezo = nevezo // lnko_eredmeny

print(f"Az egyszerűsített tört: {egyszerusitett_szamlalo}/{egyszerusitett_nevezo}")

#18. feladat:
osszeg = 0
parosdb = 0
paratlandb = 0

while osszeg <= 100:
    szam = int(input("Kérlek add meg egy egész számot: "))
    osszeg += szam

    if szam % 2 == 0:
        parosdb += 1
    else:
        paratlandb += 1

print("Az összeg meghaladta a 100-at.")
print(f"Bekért páros számok száma: {parosdb}")
print(f"Bekért páratlan számok száma: {paratlandb}")

#19. feladat:
#fogalmam sincs hogy hogy kéne

#20. feladat:
while True:
    szam = int(input("Kérlek adj meg egy páros számot: "))
    
    if szam % 2 == 0:
        print("A megadott szám megfelelő.")
        break
    else:
        print("A megadott szám nem páros. Kérlek adj meg egy páros számot.")

#21. feladat:
while True:
    szam = int(input("Kérlek adj meg egy pozitív számot: "))
    
    if szam > 0:
        maradek = szam % 5
        print(f"A megadott szám 5-tel vett osztási maradéka: {maradek}")
        break
    else:
        print("A megadott szám nem pozitív. Kérlek adj meg egy pozitív számot.")

#22. feladat:
while True:
    hetnapja = int(input("Kérem a hét napját: "))
    if hetnapja >= 1 and hetnapja <= 7:
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