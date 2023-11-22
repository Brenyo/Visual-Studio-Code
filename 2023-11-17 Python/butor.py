butorok = []

with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-17 Python/butorok.txt", encoding="utf-8", mode="r") as raktar:
    for i in raktar:
        butorok.append(i.strip())
        
def massalhangzo():
    Massalhangzok = ['b', 'd', 'dz', 'dzs', 'g', 'gy', 'j', 'l', 'ly', 'm', 'n', 'ny', 'r', 'v', 'z', 'zs', 'c', 'cs', 'f', 'h', 'k', 'p', 's', 'sz', 't', 'ty']
    for i in butorok:
        for j in Massalhangzok:
            if i[0] == j:
                print(i, end=" ")

def leghosszabbNev():
    for i in butorok:
        if len(i) >= 5:
            print(i, end=" ")

def abcsorrend():
    sorted(butorok)
    for i in butorok:
        print(i)
    
def main():
    massalhangzo()
    print("\n")
    leghosszabbNev()
    print("\n")
    abcsorrend()

main()