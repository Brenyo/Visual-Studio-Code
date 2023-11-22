szavak = []
with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-16 Python/szovegek/pilotak.txt", mode="r", encoding="utf-8") as fajl:
    for sor in fajl:
        szavak.append(sor.strip().replace("\"","").split(" "))

def szures():
    for i in szavak:
        if len(i)>5:
            print(i)

def Nagybetu():
    for szo in szavak:
        print(szo.upper())
        
def osszesbetu():
    osszesbetukszama = 0
    for i in szavak:
        osszesbetukszama+=len(i)
    print(f"A beolvasott betűk száma: {osszesbetukszama}")        

#szures()
#Nagybetu()
#osszesbetu()

with open("vezeteknev.txt", mode="w", encoding="utf-8") as kiiras:
    for szo in szavak:
        kiiras.writelines(szo[1] + "\n")