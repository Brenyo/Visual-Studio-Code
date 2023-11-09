#írjunk metódust, ami megkap egy főnevet, és visszatér a hozzá illő névelővel
#írjunk metódust, ami bekér egy főnevet, és kiir egy véletlen mondatot vele. pl:
#sapka
#A sapka kék.
#írjunk metódust, ami véletlenszerűen kiválaszt egy színt (jelzőt), és visszatér vele.
import random

def randomMondat():
    fonev = str(input("Kérek egy főnevet: "))
    print(f"{nevelo(fonev)} {fonev} {randomszin()}")
    
def nevelo(fn):
    mgh = "aáeéoóuúüűöőií"
    if fn[0] in mgh:
        return "Az"
    else:
        return "A"
    
def randomszin():
    szinek = ["piros", "zöld", "fehér", "sárga", "kék"]
    return random.choice(szinek)
    
def main():
    randomMondat()
    

main()