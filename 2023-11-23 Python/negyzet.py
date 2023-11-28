import math

class Negyzet:
    oldal_a = 0

    def __init__(self, a):
        self.oldal_a = a
    
kocka1 = Negyzet(10)
kocka2 = Negyzet(5)
kocka3 = Negyzet(13)
kocka4 = Negyzet(7)
kocka5 = Negyzet(21)

def kerulet():    
    print(f"1. kocka: {4*kocka1.oldal_a}")
    print(f"2. kocka: {4*kocka2.oldal_a}")
    print(f"3. kocka: {4*kocka3.oldal_a}")
    print(f"4. kocka: {4*kocka4.oldal_a}")
    print(f"5. kocka: {4*kocka5.oldal_a}")

def terulet():
    print(f"1. kocka: {kocka1.oldal_a*kocka1.oldal_a}")
    print(f"2. kocka: {kocka2.oldal_a*kocka2.oldal_a}")
    print(f"3. kocka: {kocka3.oldal_a*kocka3.oldal_a}")
    print(f"4. kocka: {kocka4.oldal_a*kocka4.oldal_a}")
    print(f"5. kocka: {kocka5.oldal_a*kocka5.oldal_a}")

def atlo():
    gyok1 = math.sqrt(kocka1.oldal_a)
    print(f"1. kocka: {gyok1}")
    gyok2 = math.sqrt(kocka2.oldal_a)
    print(f"2. kocka: {gyok2}")
    gyok3 = math.sqrt(kocka3.oldal_a)
    print(f"3. kocka: {gyok3}")
    gyok4 = math.sqrt(kocka4.oldal_a)
    print(f"4. kocka: {gyok4}")
    gyok5 = math.sqrt(kocka5.oldal_a)
    print(f"5. kocka: {gyok5}")

def main():
    kerulet()
    terulet()
    atlo()
    
main()