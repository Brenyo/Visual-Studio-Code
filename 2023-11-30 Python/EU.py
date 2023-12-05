import datetime

class Csatlakozas:
    def __init__(self, orszag, datum):
        self.orszag = orszag
        self.datum = datum
    def __str__(self):
        return f"{self.orszag} {self.datum}"

lista = []

def beolvasas():
    f = open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-30 Python/EUcsatlakozas.txt", encoding="UTF-8")
    for item in f:
        reszek = item.strip().split(';')
        orszag = reszek[0]
        format = "%Y.%m.%d"
        datum = datetime.datetime.strptime(reszek[1], format)
        lista.append(Csatlakozas(orszag, datum))

def f3():
    print(f"3. feladat: EU tagállamainak száma: {len(lista)}")
    
def f4():
    db = 0
    for item in lista:
        if item.datum.year == 2007:
            db += 1
    print(f"4. feladat: 2007-ben csatlakozott oszágok száma: {db}")
    
def f5():
    for item in lista:
        if item.orszag == "Magyarország":
            print(f"5. feladat: Magyarország csatlakozási dátuma: {item.datum.date()}")
    
def f6():
    igazhamis = False
    for item in lista:
        if item.datum.month == 5:
            igazhamis = True
    if igazhamis == True:
        print("6. feladat: Májusban volt csatlakozás!")
    else:
        print("6. feladat: Májusban nem volt csatlakozás!")

def f7():
    maxi = lista[0]
    for item in lista:
        if item.datum > maxi.datum:
            maxi = item
    print(f"7. feladat: Legutoljára csatlakozott ország: {maxi.orszag}")

def f8():
    #kulcs: csatlakozás éve
    #érték: adott évben hány ország csatlakozott
    stat = {}
    for item in lista:
        kulcs = item.datum.year
        if kulcs not in stat: #ha még nincsen ilyen kulcs a statban
            stat[kulcs] = 0 #nulla a kerzdőértékkel létrehozom
        stat[kulcs] += 1
    
    print("8. feladat: Statisztika")
    for kulcs in stat:
        print(f"{kulcs} - {stat[kulcs]}")
    
def main():
    beolvasas()
    f3()
    f4()
    f5()
    f6()
    f7()
    f8()

main()
