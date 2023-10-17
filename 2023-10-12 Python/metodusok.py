"""
# def kulcsszo nev():
#   minden egy tabbal bentebb van, ami a metódussba kerül

def feladat1():
    while True:
        szam = int(input("Kérek egy 0-nál nagyobb számot: "))
        if szam > 0:
            print(f"Bekert szám: {szam}")
            break

def feladat2():
    while True:
        szamÖ = int(input("Kérek egy számot: "))
        szamÖ2 = int(input("Kérek egy számot: "))
        if szamÖ != 0 and szamÖ2 != 0:
            if szamÖ2 < 0:
                print(f"A két szám értéke: {szamÖ - szamÖ2}")
                break
            elif szamÖ < 0:
                print(f"A két szám értéke: {szamÖ2 - szamÖ}")
                break
            elif szamÖ2 > 0 and szamÖ > 0:
                print(f"A két szám értéke: {szamÖ + szamÖ2}")
                break




#ebben hívunk meg mindent, amit futtatni szeretnék
"""
import random

def csekkek():
        osszeg = 0
        while True:
            szam = int(input("szám: "))
            if szam == 0:
                break
            osszeg += szam
        print("A csekkek összege: ", osszeg)

def szamkitalalos():
    veletlen10 = random.randint(1, 10)
    veletlen100 = random.randint(1, 100)
    veletlen1000 =  random.randint(1, 1000)
    hiba = 0
    while True:
        valasz = int(input("Válaszon nehézségi szintet(1, 2, 3): "))
        if valasz >= 1 and valasz <=3:
            break
        else:
            print("Nem megfelelő számot adott meg!")
    if valasz == 1:
        print("1. szintű nehézség")
        while True:
            tipp = int(input("tippelj: "))
            if hiba < 6:
                if veletlen10 < tipp:
                    print("kisebb számra gondoltam!")
                    hiba += 1
                    print(hiba, "Hiba")
                elif veletlen10 > tipp:
                    print("nagyobb számra gondoltam!")
                    hiba += 1
                    print(hiba, "hiba")
                else:
                    print("Gratulálok, eltaláltad!")
                    break
            else:
                print(f"Elfogyott a 7 próbálkozása, gondolt szám: {veletlen10}")
                break
    elif valasz == 2:
        print("2. szintű nehézség")
        while True:
            tipp = int(input("tippelj: "))
            if hiba < 6:
                if veletlen100 < tipp:
                    print("kisebb számra gondoltam!")
                    hiba += 1
                    print(hiba, "Hiba")
                elif veletlen100 > tipp:
                    print("nagyobb számra gondoltam!")
                    hiba += 1
                    print(hiba, "hiba")
                else:
                    print("Gratulálok, eltaláltad!")
                    break
            else:
                print(f"Elfogyott a 7 próbálkozása, gondolt szám: {veletlen100}")
                break
    elif valasz == 3:
        print("3. szintű nehézség")
        while True:
            tipp = int(input("tippelj: "))
            if hiba < 6:
                if veletlen1000 < tipp:
                    print("kisebb számra gondoltam!")
                    hiba += 1
                    print(hiba, "Hiba")
                elif veletlen1000 > tipp:
                    print("nagyobb számra gondoltam!")
                    hiba += 1
                    print(hiba, "hiba")
                else:
                    print("Gratulálok, eltaláltad!")
                    break
            else:
                print(f"Elfogyott a 7 próbálkozása, gondolt szám: {veletlen1000}")
                break
def matematika():
    rndMuvelet = random.randint(1, 4)
    rndSzam1 = random.randint(1, 100)
    rndSzam2 = random.randint(1, 100)
    valasz = 0
    if rndMuvelet == 1:
        while rndSzam1 + rndSzam2 == valasz:
            valasz = int(input(print(f"Adja össze a két számot: {rndSzam1} + {rndSzam2} = ")))
    elif rndMuvelet == 2:
        if rndSzam2 < rndSzam1:
            while rndSzam1 - rndSzam2 == valasz:
                valasz = int(input(print(f"Vonjaki a két számot: {rndSzam1} - {rndSzam2} = ")))
        elif rndSzam1 < rndSzam2:
            while rndSzam2 - rndSzam1 == valasz:
                valasz = int(input(print(f"Vonjaki a két számot: {rndSzam2} - {rndSzam1} = ")))
    elif rndMuvelet == 3:
    
    else:
        
    
def main():
    #csekkek()
    #szamkitalalos()
    matematika()
    
     
main()