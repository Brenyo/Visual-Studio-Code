# class: sablon, tudjuk, hogy milyen tujaldonságok, metódusokkal rendelkezik az
#Az objektum konkrét értékkel feltöltött példány
#osztály neve mindig nagybetű!
class Szemely:
    #tulajdonságok: adattag, field, osztályváltozó: mérhető adatok
    #név, életkor, magasság, születési dátum, táplálkozás, tömeg
    #képességek: metódusok
    #táplálkozás, fürdés
    nev = ""
    eletkor = 0
    magassag = 0
    tomeg = 0
    def __init__(self, nevecske, eletkor, magassag, tomeg) -> None:
        self.nev = nevecske
        self.eletkor = eletkor
        self.magassag = magassag
        self.tomeg = tomeg
        

    def taplalkozas(self, mennyiseg):
        self.tomeg += mennyiseg
    def sportolas(self, mennyiseg):
        if self.tomeg-mennyiseg > 0:
            self.tomeg-= mennyiseg
            
def peldanyositas():
    joska = Szemely()
    print(joska.nev)
    print(joska.eletkor)
    print(joska.magassag)
    print(joska.tomeg)

def peldanyositasInitenkeresztul():
    joska = Szemely("Joska", 58, 175, 75.2)
    print(joska.nev)
    print(joska.eletkor)
    print(joska.magassag)
    print(joska.tomeg)
    
    bozsi = Szemely("Bözsi", 79, 200, 102)
    print(bozsi.nev)
    print(bozsi.eletkor)
    print(bozsi.magassag)
    print(bozsi.tomeg)

def __str__(self):
    return f"{self.nev} {self.eletkor}"
szemelyek = []
def falu():
    szemelyek.append(Szemely("Joska", 58, 175, 75.2))
    szemelyek.append(Szemely("Bözsi", 79, 200, 102))
    szemelyek.append(Szemely("Géza", 35, 160, 52.2))
    szemelyek.append(Szemely("Magdi", 34, 155, 45.2))
    for item in szemelyek:
        print(f"{item.nev} {item.eletkor} {item.magassag} {item.tomeg}")

    
def main():
    falu()
    
main()