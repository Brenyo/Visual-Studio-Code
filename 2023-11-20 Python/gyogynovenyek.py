noveny = []
aprobetu = []
with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-20 Python/novenyek.txt", mode="r", encoding="utf-8") as fajl:
    for sor in fajl:
        noveny.append(sor.strip().split(" "))

for i in noveny:
    x = str(i).lower()
    for i in x:
        aprobetu.append(x)
        x = None
for i in aprobetu:
    print(i, sep=" ")