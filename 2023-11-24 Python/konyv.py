class Book:
    KonyvCim = ""
    KonyvSzerzo = ""
    KiadasiEv = 0
    def __init__(self, cim, szerzo, ev):
        self.KonyvCim = cim
        self.KonyvSzerzo = szerzo
        self.KiadasiEv = ev