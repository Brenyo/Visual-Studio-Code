"""
szam = int(input("Kérem adjon egy számot: "))
if szam > 0 and szam <= 9:
    print("A szám amit megadott az 1 és 9 közötti szám!")
else:
    print("A szám kivül esik a megfelelő intervallumon [1-9]")    

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
if a + b > c and b + c > a and a + c > b:
    K = a + b + c
    print(f"A háromszög szerkeszthető! Kerülete = {K} cm")
else:
    print("A háromszög nem szerkeszthető!")
"""
#if logikai feltétel legyen, ami vagy true vagy false
#if a == 6
szam = int(input("Kérem adjon meg egy számot: "))
if szam > 0:
    print(f"+{szam}")
elif szam < 0:
    print(f"{szam}")
else:
    print(f"Nulla!")




