"""
#1 feladat
#0-tól 50-ig a számok egymás alá
for i in range(51):
    print(i)

#182-től 212-ig a számok egymás alá
for i in range(182, 213):
    print(i)

#Páros számok 100-tól 200-ig
for i in range(100, 201, 2):
    print(i)

#Páratlan számok 89-től 57-ig visszafelé
for i in range(89, 56, -1):
    if i % 2 != 0:
        print(i)

#Számok és négyzetük 1-től 20-ig
for i in range(1, 21):
    print(f"{i} - {i*i}")

#3-mal osztható számok 99-től csökkenő sorrendben
for i in range(99, 0, -3):
    print(i)

#5-tel osztható számok kétszerese 101-től 50-ig csökkenő sorrendben
for i in range(101, 49, -1):
    if i % 5 == 0:
        print(i * 2)

#Egész számok 1-től 1000-ig, vesszővel elválasztva
for i in range(1, 1001):
    if i == 1000:
        print(i, end=".\n")
    else:
        print(i, end=", ")

#Egész számok 1000-től 1-ig visszafelé 3-asával
for i in range(1000, 0, -3):
    print(i)
    
#2 feladat
#Írjunk ki a képernyőre 100 db csillagot!
for i in range(100):
    print("*", end=" ")

#Írjunk ki a képernyőre bekért darabszámú, bekért karaktert!
darabszam = int(input("Darabszám: "))
karakter = input("Karakter: ")
for i in range(darabszam+1):
    print(karakter,end=" ")

#Kérjünk be egy szöveget, majd keretezzük körbe csillagokkal!
szoveg = input("Kérek egy szöveget: ")
keret = ""
for i in range(len(szoveg)+4):
    keret+= "*"
print(keret)
print(f"* {szoveg} *")
print(keret)

#Rajzoljunk le egy 8*8-as sakktáblát csillagokból és szóközökből!
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    
#3 feladat
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek mégegy számot: "))
lepeskoz = int(input("Lépésköz: "))
kisebb = min(szam1, szam2)
nagyobb = max(szam1, szam2)
for i in range(kisebb,nagyobb+1, lepeskoz):
    print(i)

#4 feladat
n = int(input("Adja meg n értékét: "))
for i in range(1, n + 1):
    print(i*i, end="; ")

#5 feladat 
n = int(input("Adja meg n értékét: "))
for i in range(1, n + 1):
    print(i*i*i)

#6 feladat
import math
a = int(input("Kérem az alsó határt (a): "))
b = int(input("Kérem a felső határt (b): "))
for i in range(a, b + 1):
    if i >= 0:
        gyok = math.sqrt(i)
        print(f"A(z) {i} szám négyzetgyöke: {round(gyok,2)}")
    else:
        print(f"A(z) {i} szám negatív, nincs valós négyzetgyöke.")

#7 feladat
fakt = 1 
n = int(input("Kérem a faktoriális számot (n): "))
for i in range(n,0, -1):
    fakt *= i
print(fakt)

#8 feladat
N = int(input("Kérek egy (n) számot: "))
for i in range(1, N + 1):
    square = i * i
    print(f"{i} négyzetszáma: {square}")

#9 feladat
sum = 0
N = int(input("Kérek egy (n) számot: "))
for i in range(1, N+1):
    if i%2 != 0:
        sum += i
print(f"Páratlan számok összege: {sum}")

#10 feladat
K = int(input("Kérem adja meg a K pozitív egész számot: "))
osszeg = 0
for i in range(1, K + 1):
    osszeg += i * (i + 1)
print(f"A számok összege: {osszeg}")

#11 feladat
N = int(input("Kérek egy (n) számot: "))
for i in range(1, N + 1):
    haromszoros = 3 * i
    if haromszoros <= N:
        print(haromszoros)
    else:
        break
        
#12 feladat
# nem jöttem rá hogy hogy kell

#13 feladat
def prime(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

count = 0
num = 2
N = int(input("Adja meg, hány prímszámot szeretne kiírni: "))
while count < N:
    if prime(num):
        print(num)
        count += 1
    num += 1

#14 feladat
size = int(input("Adja meg a táblázat méretét: "))

print(" *", end=" ")
for i in range(1, size + 1):
    print(i, end=" ")
print("\n", "-" * (size * 4 + 3))

for i in range(1, size + 1):
    print(f"{i} ¦", end=" ")
    for j in range(1, size + 1):
        szorzat = i * j
        print(szorzat, end=" ")
    print()

#15 feladat 
import random

intervallumok = [[0, 10], [0, 25], [0, 50], [10, 75], [-50, 50], [-100, -70]]

for i in intervallumok:
    print(f"Intervallum: {i}",end=": ")
    for i in range(10):
        random_number = random.randint(i[0], i[1])
        print(f"{random_number}", end=", ")
    print()

#16 feladat
n = int(input("Adjon meg egy egész számot a négyzet méretéhez: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#17 feladat
M = int(input("Adja meg az M méretét: "))
N = int(input("Adja meg az N méretét: "))

for i in range(N):
    for j in range(M):
        print("*", end="")
    print()   

#18 feladat
M = int(input("Adja meg az M méretét: "))
N = int(input("Adja meg az N méretét: "))

for i in range(N):
    for j in range(i):
        print(" ", end="")
    for j in range(M):
        print("*", end="")
    print()  

#19 feladat
N = int(input("Adja meg a háromszög sorainak számát: "))
for i in range(1, N + 1):
    spaces = N - i
    stars = 2 * i - 1
    print(spaces,stars)
    print(" " * spaces + "*" * stars)

#20 feladat
M = int(input("Adja meg az M méretét: "))
N = int(input("Adja meg az N méretét: "))
for i in range(N):
    if i == 0 or i == N - 1:
        print("*" * M)
    else:
        print("*" + " " * (M - 2) + "*")

#21
import random

feladatok_szama = int(input("Kérem adja meg, hány feladatot szeretne megoldani: "))
helyes_valaszok = 0
for i in range(feladatok_szama):
    szam1 = random.randint(1, 101)
    szam2 = random.randint(1, 101)

    print(f"{szam1} + {szam2} = ?")
    osszeg_valasz = int(input("Adja meg az összeget: "))
    
    print(f"{szam1} - {szam2} = ?")
    kulonbseg_valasz = int(input("Adja meg a különbséget: "))
    
    helyes_osszeg = szam1 + szam2
    helyes_kulonbseg = szam1 - szam2
    
    if osszeg_valasz == helyes_osszeg and kulonbseg_valasz == helyes_kulonbseg:
        print("Helyes válaszok!")
        helyes_valaszok += 1
    else:
        print("Rossz válaszok!")
arany = (helyes_valaszok / feladatok_szama) * 100
print(f"\nHelyes válaszok: {helyes_valaszok}/{feladatok_szama} ({round(arany)}%)")

#22 feladat
print("Kód  Karakter")
for kod in range(32, 256):
    karakter = chr(kod)
    print(f"{kod:3}  {karakter}")

#23 feladat
szam = int(input("Kérem adjon meg egy pozitív egész számot: "))
print(f"{szam} osztói: ")
for i in range(1, szam + 1):
    if szam % i == 0:
        print(i, end=", ")

#24 feladat
szam = int(input("Kérem adjon meg egy pozitív egész számot: "))
sum = 0
for i in range(1, szam + 1):
    if szam % i == 0:
        sum += i
print(f"Osztóinak összege: {sum}")

#25 feladat
szam = int(input("Kérem adjon meg egy pozitív egész számot: "))
sum = 0
for i in range(1, szam):
    if szam % i == 0:
        sum += i
if sum == szam:
    print(f"{szam} egy tökéletes szám")
else:
    print(f"{szam} nem tökéletes szám")

#26 feladat
alap = float(input("Kérem adja meg a hatvány alapját: "))
kitevo = int(input("Kérem adja meg a kitevőt: "))

hatvany = alap ** kitevo
print(f"A hatványérték: {round(hatvany)}")

#27 feladat
#nem tudtam megoldani
"""