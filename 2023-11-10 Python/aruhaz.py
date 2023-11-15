import random

class Aruhaz:
    def termek(self):
        self.keszlet = {
            "Termék 1": 300,
            "Termék 2": 300,
            "Termék 3": 300,
            "Termék 4": 300,
            "Termék 5": 300,
        }
        self.kosar = {}

    def kiszamol(self, mennyiseg):
        if mennyiseg == 1:
            return 300
        elif mennyiseg == 2:
            return 250
        else:
            return 200

    def keszlet_megjelenites(self):
        print("Elérhető termékek:")
        for termek, ar in self.keszlet.items():
            print(f"{termek}: {ar} Ft")

    def kosarba_helyezes(self, termek, mennyiseg):
        if termek in self.keszlet:
            if termek in self.kosar:
                self.kosar[termek] += mennyiseg
            else:
                self.kosar[termek] = mennyiseg
            print(f"{mennyiseg} db {termek} hozzáadva a kosárhoz.")
        else:
            print("A megadott termék nem található a készletben.")

    def kosar_tartalom_megjelenites(self):
        print("\nKosár tartalma:")
        for termek, mennyiseg in self.kosar.items():
            ar = self.kiszamol(mennyiseg)
            print(f"{termek}: {mennyiseg} db - {ar} Ft")
        teljes_osszeg = sum(self.kiszamol(mennyiseg) for mennyiseg in self.kosar.values())
        print(f"Teljes vásárlási összeg: {teljes_osszeg} Ft")

    def akcio(self):
        akcios_termek = random.choice(list(self.keszlet.keys()))
        print(f"\nMa akciós a(z) {akcios_termek}! Ára: 100 Ft")

        for termek in self.kosar:
            if termek == akcios_termek:
                self.kosar[termek] *= 100 // 300

    def vasarlas(self):
        self.kosar_tartalom_megjelenites()
        teljes_osszeg = sum(self.kiszamol(mennyiseg) for mennyiseg in self.kosar.values())
        print(f"\nVásárlási összeg: {teljes_osszeg} Ft")
        print("Vásárlás megerősítve. Köszönjük a vásárlást!")

        self.kosar = {}

aru = Aruhaz()
aru.keszlet_megjelenites()

aru.kosarba_helyezes("Termék 1", 2)
aru.kosarba_helyezes("Termék 3", 1)
aru.kosarba_helyezes("Termék 2", 3)
aru.kosar_tartalom_megjelenites()

aru.akcio()
aru.kosar_tartalom_megjelenites()

aru.vasarlas()
