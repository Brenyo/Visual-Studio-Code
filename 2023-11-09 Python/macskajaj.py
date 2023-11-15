import random

def egyeniPontszam():
    return random.randint(1,5)

def csapatPontszam(csapat):
    lista = []
    for i in range(7):
        lista.append(egyeniPontszam() * 10)
    return lista
def pontOsszesites(lista):
    return sum(lista)

def gyoztes(sorszam, urmacska, szupereger):
    urmacskaPont = pontOsszesites(urmacska)
    szuperegerPont = pontOsszesites(szupereger)
    
    print(f"{sorszam}. kör: ")
    print(f"\tűrmacskak: ", end= " ")
    print(*urmacska, sep=" ", end=" ->")
    print(pontOsszesites(urmacska))
    
    print(f"\tszuperegerek: ", end= " ")
    print(*szupereger, sep=" ", end=" ->")
    print(pontOsszesites(szupereger))
    
    return urmacskaPont > szuperegerPont 
    
def jatek():
    gyoztesMecsekSzama = 0
    for i in range(1,8):
        urmacskak = csapatPontszam()
        szuperegerek = csapatPontszam()
        gyozE = gyoztes(i, urmacskak, szuperegerek)
        if gyozE:
            gyoztesMecsekSzama +1
    print(f"Ádám győzelmeinek száma: {gyoztesMecsekSzama}")
def main():
    jatek()
    
    
main()