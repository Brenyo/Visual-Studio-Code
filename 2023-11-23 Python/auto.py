class Szemelyauto:
    def __init__(self, marka, modell, evjarat, szin, uzemanyag):
        self.marka = marka
        self.modell = modell
        self.evjarat = evjarat
        self.szin = szin
        self.uzemanyag = uzemanyag
        self.km = 0

    def vezet(self, tavolsag):
        self.km += tavolsag
        return f"{self.marka} {self.modell} vezetve {tavolsag} km-t. Új km-óra állás: {self.km} km."

    def tankol(self, mennyiseg):
        return f"{self.marka} {self.modell} tankolt {mennyiseg} liter üzemanyagot."

    def bemutatkozas(self):
        return f"{self.marka} {self.modell} ({self.evjarat}), Szín: {self.szin}, Üzemanyag: {self.uzemanyag}, Km-óra állás: {self.km} km"

# Példányosítás és használat
auto1 = Szemelyauto("Toyota", "Corolla", 2022, "fehér", "benzin")
print(auto1.bemutatkozas())
print(auto1.vezet(150))
print(auto1.tankol(40))

auto2 = Szemelyauto("Ford", "Focus", 2021, "kék", "dízel")
print(auto2.bemutatkozas())
print(auto2.vezet(100))
print(auto2.tankol(35))

auto3 = Szemelyauto("Volkswagen", "Golf", 2020, "ezüst", "benzin")
print(auto3.bemutatkozas())
print(auto3.vezet(200))
print(auto3.tankol(45))

auto4 = Szemelyauto("Renault", "Clio", 2023, "piros", "elektromos")
print(auto4.bemutatkozas())
print(auto4.vezet(80))
print(auto4.tankol(30))

auto5 = Szemelyauto("Hyundai", "i30", 2022, "zöld", "benzin")
print(auto5.bemutatkozas())
print(auto5.vezet(120))
print(auto5.tankol(38))
