class Device:
    Nev = ""
    allapot = False
    
    def __init__(self, nev):
        self.Nev = nev
        
    def bekapcsol(self):
        self.allapot = True
    
    def kikapcsol(self):
        self.allapot = False
    
    def milyenAllapot(self):
        if self.allapot == True:
            return 'Bekapcsolva'
        else:
            return 'Kikapcsolva'
    
    def __str__(self):
        return f"{self.Nev} ({self.milyenAllapot()})"

dev1 = Device('Egér')
dev1.bekapcsol()
dev2 = Device('Párhuzamos Port')

eszkozok = [dev1, dev2, Device('Monitor'), Device('Rajztábla')]

eszkozok[3].bekapcsol()
eszkozok[0].kikapcsol()
for e in eszkozok:
    print(e.milyenAllapot())
    print(e)