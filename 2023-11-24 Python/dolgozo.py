class Employee:
    Nev = ""
    Pozicio = ""
    Fizetes = 0
    def __init__(self, nev, pozi, fizu):
        self.Nev = nev
        self.Pozicio = pozi
        self.Fizetes = fizu
    
    def FizetesEmeles(self, emeles):
        self.Fizetes += emeles