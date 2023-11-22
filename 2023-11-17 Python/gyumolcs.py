gyumolcs = []

with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-17 Python/gyumolcsok.csv", encoding="utf-8", mode="r") as raktar:
    for i in raktar:
        gyumolcs.append(i.strip().split(";"))
        
print(len(gyumolcs))

osszes = 0
for i in gyumolcs:
    osszes += int(i[1])
    
print(osszes)

darab = len(gyumolcs)
atlag = osszes / darab

print(atlag)

atlagonFelul = []
for j in gyumolcs:
    if atlag < int(j[1]):
        atlagonFelul.append(j)

print(atlagonFelul)

