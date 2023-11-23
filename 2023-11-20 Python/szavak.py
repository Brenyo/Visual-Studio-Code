import random

szavak = []

with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-20 Python/szavak.txt", mode="r", encoding="utf-8") as fajl:
    for sor in fajl:
        szavak.append(sor.strip().split(" "))

def szures():
    for i in szavak:
        if len(i)>8:
            print(i)
        
def szamolas():
    osszesbetukszama = 0
    for i in szavak:
        osszesbetukszama+=len(i)
    print(f"A beolvasott betűk száma: {osszesbetukszama}")        

def kivalogatas():
    maganhangzok = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    for szo in szavak:
        if szo[0] == maganhangzok:
            print(szo)
def veletlen():
    rnd = random.randint(1,524)
    for i in szavak:
        if rnd == i:
            print(i)
            

szures(szavak)
szamolas(szavak)
kivalogatas(szavak)
veletlen(szavak)
