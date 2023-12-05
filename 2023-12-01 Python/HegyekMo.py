class Hegyek:
    def __init__(self, neve, hegyseg, magassag):
        self.neve = neve
        self.hegyseg = hegyseg
        self.magassag = magassag
        
    def __str__(self):
        return f"{self.neve} {self.hegyseg} {self.magassag}"

data = []

def beolvasas():
    f = open("C:/Users/nessu/Documents/Visual Studio Code/2023-12-01 Python/hegyekMo.txt", encoding="UTF-8")
    next(f)
    for item in f:
        reszek = item.strip().split(';')
        nev = reszek[0]
        hegy = reszek[1]
        magas = reszek[2]
        data.append(Hegyek(nev, hegy, magas))

def f3():
    print(f"3. feladat: Hegycsúcsok száma: {len(data)}")
    
def f4():
    osszes = 0
    for item in data:
        osszes += int(item.magassag)
    atlag = osszes / len(data)
    print(f"4. feladat: Hegycsúcsok átlagos magassága: {atlag}")
        
def f5():
    leg = []
    legmagassabb = data[2]
    for item in data:
        leg.append(item.magassag)
    legnagyobb = max(leg)
    for i in data:
        if int(i.magassag) == legnagyobb:
            print(f"5. feladat: A legmagassabb hegycsúcs adatai: \n\tNév: {i.neve}\n\tHegység: {i.hegyseg}\n\tMagasság: {i.magassag} m")
    
def main():
    beolvasas()
    f3()
    f4()
    f5()
    
    
    
main()