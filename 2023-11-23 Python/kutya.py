class Kutya:
    def __init__(self, nev, fajta, kor):
        self.nev = nev
        self.fajta = fajta
        self.kor = kor

    def ugat(self):
        return "Vau-vau!"

    def bemutatkozas(self):
        return f"Név: {self.nev}, Fajta: {self.fajta}, Kor: {self.kor} év"

kutya1 = Kutya("Bodri", "Németjuhász", 3)
print(kutya1.bemutatkozas())
print(kutya1.ugat())

kutya2 = Kutya("Foltos", "Bulldog", 2)
print(kutya2.bemutatkozas())
print(kutya2.ugat())
