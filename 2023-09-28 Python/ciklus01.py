"""
for i in range(0,51):
    print(i)
for i in range(181, 213):
    print(i)
for i in range(100, 201, 2):
    print(i)
for i in range(89, 57, -2):
    print(i)
for i in range(1,21):
    print(i, i*i)
for i in range(100):
    print('*')
bekertKarakter = str(input("Kérek egy karaktert: "))
bekertSzam = int(input("Kérem, hogy hányszor fusson le: "))
for i in range(bekertSzam):
    print(bekertKarakter)
"""
bekerttSz = str(input("Kérek egy szöveget: "))
keret = ""
for i in range(len(bekerttSz)+4):
    keret += "*"
print(keret)
print(f"* {bekerttSz} *")
print(keret)