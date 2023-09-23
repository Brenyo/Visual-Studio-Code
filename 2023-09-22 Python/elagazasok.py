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
#if logikai feltétel legyen, ami vagy true vagy false
#if a == 6

szam = int(input("Kérem adjon meg egy számot: "))
if szam > 0:
    print(f"+{szam}")
elif szam < 0:
    print(f"{szam}")
else:
    print(f"Nulla!")

homerseklet = int(input("Kérem adja meg a víz hőmérsékletét: "))
if homerseklet < 0:
    print("szilárd (jég)")
elif homerseklet > 0 and homerseklet < 100:
    print("folyékony (víz)")
elif homerseklet > 100:
    print("légnemű (gőz)")

elsoSz = int(input("Kérem adjon meg egy számot: "))
masodikSz = int(input("Kérem adjon meg egy számot: "))
if elsoSz > 0 and masodikSz > 0:
    print("Első síknegyed!")
elif elsoSz < 0 and masodikSz > 0:
    print("Második síknegyed!")
elif elsoSz < 0 and masodikSz < 0:
    print("Harmadik síknegyed!")
elif elsoSz > 0 and masodikSz < 0:
    print("Negyedik síknegyed!")

dolgozatPontSz = int(input("Kérem a dolgozat pontszámát: "))
if dolgozatPontSz <= 42:
    print("Elégtelen!")
elif dolgozatPontSz <= 57:
    print("Elégséges!")
elif dolgozatPontSz <= 72:
    print("Közepes!")
elif dolgozatPontSz <= 87:
    print("Jó!")
elif dolgozatPontSz <= 100:
    print("Jeles!")

folySuruseg = int(input("Folyadék sűrűség: "))
targySuruseg = int(input("Tárgy sűrűsége: "))
if targySuruseg > folySuruseg:
    print("tárgy elmerült!")
elif folySuruseg > targySuruseg:
    print("tárgy úszik!")
elif folySuruseg == targySuruseg:
    print("tárgy lebeg!")

#24
igazolatlanH = int(input("Kérem az igazolatlan számát: "))
if igazolatlanH == 0:
    print("5!")
elif igazolatlanH < 4:
    print("4!")
elif igazolatlanH < 10:
    print("3!")
else:
    print("2!")
    diakSzulEv = int(input("Kérem a diák születési évét: "))
    Eletkor = 2023 - diakSzulEv
    if Eletkor < 18:
        print("Szülői értesítés szükséges!")
    else:
        print("Felszólítás kiküldése szükséges!")

#26
AutoSebesseg = int(input("Kérem adja meg az autó sebességét(Km/h): "))
if AutoSebesseg >= 0 and AutoSebesseg < 2:
    print("csiga")
elif AutoSebesseg < 7:
    print("csuka")
elif AutoSebesseg < 33:
    print("bálna")
elif AutoSebesseg < 49:
    print("ezüst sirály")
elif AutoSebesseg < 65:
    print("nyúl")
elif AutoSebesseg < 71:
    print("strucc")
elif AutoSebesseg < 111:
    print("gepárd")
elif AutoSebesseg > 111 and AutoSebesseg < 321:
    print("vadászsólyom (zuhanórepülésben)")
else:
    print("túl gyors")

#27
FutarTav = int(input("Kérem adja meg a fuvar távolságát: "))
if FutarTav > 0 and FutarTav < 3:
    print("500 Ft")
elif FutarTav < 6:
    print("700 Ft")
elif FutarTav < 11:
    print("900 Ft")
elif FutarTav < 21:
    print("1400 Ft")
elif FutarTav > 20 and FutarTav < 31:
    print("2000 Ft")

#28
szelesseg = int(input("Telek szélesség: "))
hosszusag = int(input("Telek hosszúság: "))
HelyiTAdo = int(input("Helyi telek adó: "))
if szelesseg <=15 or hosszusag <= 25:
    adoKedvezmeny = HelyiTAdo / 100 * 20
    print(f"{HelyiTAdo + adoKedvezmeny} Ft")
else:
    print("Nincsen kedvezmény!")
"""

