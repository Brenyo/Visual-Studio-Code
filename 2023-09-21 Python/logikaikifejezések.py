"""
egyikSzam = int(input("Kérem az első számot: "))
masikSzam = int(input("Kérem a második számot: "))

#= értékadás. A logikai változó kap értéket.
#AND - két kifejezést kötünk össze egy and -de: ha mindkét feltétel igaz, akkor
logikai = egyikSzam > 0 and masikSzam > 0
print(f"Mindkét szám pozitív: {logikai}")

#OR - ha legalább az egyik feltétel teljesül akkor igaz lesz
logikai = egyikSzam > 0 or masikSzam > 0
print(f"Egyik szám pozitív, másik negatív: {logikai}")
"""

"""
egyikSzam = int(input("Kérem az első számot: "))
masikSzam = int(input("Kérem a második számot: "))

logikai = egyikSzam == 5 and masikSzam != 4
print(f"Egyik szám 5 a másik nem 4 {logikai}")
Táblázatos igazságtábla, melyben az 1: true, a 0 false értéket takar
 A | B | A and B
 1 | 1 |    1
 0 | 1 |    0
 1 | 0 |    0
 0 | 0 |    0    

A = True
B = True
print(f" {'  A'} | {'  B'} | A and B")
print(f" {A:3} | {B:3} | {A and B} ")
A = False
print(f" {A:3} | {B:3} | {A and B} ")
A = True
B = False
print(f" {A:3} | {B:3} | {A and B} ")
A = False
print(f" {A:3} | {B:3} | {A and B} ")
"""
""" 
szam = int(input("Kérem a számot: "))
if szam % 10 == 0:
    print("A szám osztható 10-zel!")
else:
    print(f"A szám nem osztható 10-zel, a maradék: {szam%10}")
"""
szam1 = int(input("Kérem adja meg a törtnek a számlálóját: "))
szam2 = int(input("Kérem adja meg a törtnek a nevezőjét: "))
if szam2 == 0:
    print("A nevezőben nem lehet nulla!")
else:
    print(f"{szam1}\n-\n{szam2}")




