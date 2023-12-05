import datetime

class Pilota:
    def __init__(self, nev, szuletes, nemzet, rajtszam):
        self.nev = nev
        self.szuletes = szuletes
        self.nemzet = nemzet
        self.rajtszam = rajtszam
    
data = []

def beolvasas():
    file = open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-30 Python/pilotak.csv", encoding="UTF-8")
    for item in file:
        reszek = item.strip().split(';')
        nev = reszek[0]
        format = "%Y.%m.%d"
        szuletes = datetime.datetime.strptime(reszek[1], format)
        nemzet = reszek[2]
        rajtszam = reszek[3]
        data.append(Pilota(nev, szuletes, nemzet, rajtszam))

def f3():
    print(f"3. feladat: {len(data)}")
        
        


def main():
    beolvasas()
    f3()
    
    
main()