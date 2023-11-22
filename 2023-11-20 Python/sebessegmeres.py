sebesseg = []

with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-20 Python/sebessegmero.txt", mode="r", encoding="utf-8") as fajl:
    for sor in fajl:
        sebesseg.append(sor.strip().split(" "))

negativ = 0
pozitiv = 0
for i in sebesseg:
    if int(i[0]) > 0:
        pozitiv+=1
    else:
        negativ+=1

if negativ > pozitiv:
    print("A bal irányba nagyobb volt a forgalom!")
elif negativ == pozitiv:
    print("Mindkét irányba egyenlő volt a forgalom!")
else:
    print("A jobb irányba nagyobb volt a forgalom!")