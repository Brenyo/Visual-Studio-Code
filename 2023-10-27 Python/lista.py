import random
def f1():
    szavak = ["eper", "dió", "málna"] #lista: egyszerre több adatot is tudok tárolni egy adatszerkezetben
    szavak.append("alma")
    szavak.append("körte")
    szavak.append("szilva")
    print(szavak)
    print(f"Az elemek száma: {len(szavak)}")
    print(*szavak, sep= ", ")
    print(f"Az első elem: {szavak[0]} ")
    for i in range(0, len(szavak)):
        print(szavak[i])
    print(f"Az utolsó elem: {szavak[len(szavak)-1]}")
    print(f"Az utolsó elem: {szavak[-1]}")
    szavak.sort()
    print(*szavak, sep= ", ")


def f2():
    szamok = []
    for i in range(10):
        szamok.append(random.randint(-10,10))
    print(*szamok, sep= ", ")
    print(f"Az elemek száma: {len(szamok)}")
    #a számok összege:
    osszeg = 0
    for i in range(len(szamok)):
        osszeg += szamok[i]
    print(f"A számok összege: {osszeg}")

    osszeg = 0
    for item in szamok:
        print(item, end= " ")
        osszeg += item
    print()    
    print(f"A számok összege: {osszeg}")

    osszeg= sum(szamok)
    print(f"A számok összege: {osszeg}")
    print(f"A legkisebb elem: {min(szamok)}")
    print(f"A legnagyobb elem: {max(szamok)}")
    print(f"Átlag: {sum(szamok)/len(szamok)}")


def main():
    #f1()
    f2()

main()









