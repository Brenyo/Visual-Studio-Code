huto = []

def main():
    while True:
        print("1. listázás\n 2. kivétel\n3. berakás\n4. takarítás\n5. kilépés")
        valasz = int(input("Melyik menüpontot választja: "))
        match valasz:
            case 1: 
                print(*huto, end=", ")
            case 2: 
                kivetel = str(input("Mit szeretnél kivenni? "))
                if kivetel in huto:
                    huto.remove(kivetel)
                    print("Egészségedre!")
                else:
                    print("Már múlt héten megetted!")
            case 3:
                berakas = str(input("Mit szeretnél betenni? "))
                if berakas in huto:
                    print("Már korábban beraktad!")
                else:
                    huto.append(berakas)
            case 4:
                huto.clear()
            case 5:
                break
main()