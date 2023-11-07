konyvtar = []

def main():
    while True:
        print("1. Könyvek listázása\n2. Könyv keresése szerző vagy cím alapján\n3. Új könyv hozzáadása\n4. Könyv kölcsönzése\n5. Könyv visszatétele\n6. Kilépés")
        valasz = int(input("Melyik menüpontot választja: "))
        match valasz:
            case 1: 
                print(*konyvtar, sep="\n")
            case 2:
                kereses = input("Adja meg a könyv címét vagy szerzőjét, amit keresni kiván: ")
                talaltKonyvek = []
                for konyv in konyvtar:
                    if kereses in konyv['szerzo'] or kereses in konyv['cim']:
                        talaltKonyvek.append(konyv)
                if talaltKonyvek:
                    print("A találatok:")
                    for konyv in talaltKonyvek:
                        print(f"Szerző: {konyv['szerzo']}, Cím: {konyv['cim']}")
                else:
                    print("Nincs találat a könyvtárban.")
            case 3:
                szerzo = input("Adja meg a könyv szerzőjét: ")
                cim = input("Adja meg a könyv címét: ")
                if not any(konyv['szerzo'] == szerzo and konyv['cim'] == cim for konyv in konyvtar):
                    konyvtar.append({'szerzo': szerzo, 'cim': cim})
                    print("A könyv hozzáadva a könyvtárhoz.")
                else:
                    print("A könyv már szerepel a könyvtárban.")
            case 4:
                keresett = input("Adja meg a kölcsönzési feltételt (szerző vagy cím): ")
                talaltKonyvek = []
                for konyv in konyvtar:
                    if keresett in konyv['szerzo'] or keresett in konyv['cim']:
                        talaltKonyvek.append(konyv)
                if talaltKonyvek:
                    print("A találatok:")
                    for konyv in talaltKonyvek:
                        print(konyv)
                        konyvtar.remove(konyv)
                    print("A könyv kölcsönadva.")
                else:
                    print(f"A {keresett} című könyv nincs a könyvtárban.")

            case 5: 
                szerzo = input("Adja meg a visszavett könyv szerzőjét: ")
                cim = input("Adja meg a visszavett könyv címét: ")
                if not any(konyv['szerzo'] == szerzo and konyv['cim'] == cim for konyv in konyvtar):
                    print("A könyv visszavéve.")
                else:
                    konyvtar.append({'szerzo': szerzo, 'cim': cim})
                    print("A könyv nem volt kölcsönözve, most hozzáadva a könyvtárhoz.")

            case 6: 
                break  
main()