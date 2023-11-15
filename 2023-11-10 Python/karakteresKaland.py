import random

def kezdetiAllapot():
    herculesz_eletero = random.randint(100, 150) // 10 * 10
    victoria_eletero = random.randint(100, 150) // 10 * 10
    return herculesz_eletero, victoria_eletero

def sebzodes(szint, kepesseg):
    if kepesseg == "Ütés":
        return 10 * szint
    elif kepesseg == "Rúgás":
        return 15 * szint
    elif kepesseg == "Kardhasítás":
        return 12 * szint
    elif kepesseg == "Eltűnés":
        return 8 * szint

def kihivas(nehezsegi_szint):
    kepesseg_valasztas = random.choice(["Ütés", "Rúgás", "Kardhasítás", "Eltűnés"])
    sebzes = sebzodes(nehezsegi_szint, kepesseg_valasztas)
    return kepesseg_valasztas, sebzes

def jatek():
    Heletero, Veletero = kezdetiAllapot()

    for kihivas_szint in range(1, 6):
        print(f"\nKihívás {kihivas_szint} - Hősi Herculész és Vakmerő Victoria életerői:")
        print(f"Hősi Herculész: {Heletero} HP")
        print(f"Vakmerő Victoria: {Veletero} HP")

        herculesz_kepesseg, herculesz_sebzes = kihivas(kihivas_szint)
        victoria_kepesseg, victoria_sebzes = kihivas(kihivas_szint)

        Veletero -= herculesz_sebzes
        Heletero -= victoria_sebzes

        print(f"Hősi Herculész használta: {herculesz_kepesseg}, sebzés: {herculesz_sebzes} HP")
        print(f"Vakmerő Victoria használta: {victoria_kepesseg}, sebzés: {victoria_sebzes} HP")

    return Heletero, Veletero

def gyoztes():
    Heletero, Veletero = jatek()

    if Heletero > Veletero:
        print("\nHősi Herculész győzött!")
    elif Veletero > Heletero:
        print("\nVakmerő Victoria győzött!")
    else:
        print("\nA kaland holtverseny lett!")
    
def main():
    gyoztes()
    
main()