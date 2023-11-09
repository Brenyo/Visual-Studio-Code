panzio = [0]*12

def erkezes():
    while True:
        vendegszam = int(input("Hány vendég érkezett: "))
        if vendegszam == 0:
            break
        while vendegszam > 0:
            for i in range(len(panzio)):
                if panzio[i] == 0:
                    if vendegszam == 1:
                        panzio[i] = 1
                        vendegszam -= 1
                        print(f"{i+1}", end=" ")
                    elif vendegszam >= 2:
                        panzio[i] = 2
                        vendegszam -=2                                       
                        print(f"{i+1}", end=" ")
                    else:
                        break
            if vendegszam > 0:
                break
        if vendegszam > 0:
            print(f"Nincsen több szoba! {vendegszam} vendéget nem tudunk elszállásolni!")
    print(*panzio)

def tavozas():
    while True:
        szobaszam = int(input("Melyik szobából szeretne kijelentkezni?: "))
        if szobaszam < 1 and szobaszam > 12:
            print(f"Nincsen {szobaszam} nálunk!")
        elif panzio[szobaszam-1] == 0:
            print("Ez a szoba üres, ebből nem költözhet ki!")
        else:
            panzio[szobaszam-1] = 0
            break
    print("Köszönjük, hogy minket válaszott!")
    
def listazas():
    for i in range(len(panzio)):
        print(f"{i+1}. szoba: {panzio[i]}") 
   
def recepcio():
    while True:
        print("1. Bejelentkezés\n2. Kijelentkezés\3. Listázás\n4. Vendégek száma\n5. Szilveszteri Bevétel\n6. Szilveszteri bevétel kiesés\n7. Kilépés")
        menu = int(input("Melyik menüt választja: "))
        if menu == 1:
            erkezes()
        elif menu == 2:
            tavozas()
        elif menu == 3:
            listazas()
        elif menu == 7:
            break

def main():
    recepcio()