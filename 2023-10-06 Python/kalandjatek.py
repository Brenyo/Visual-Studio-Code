import random
harcosHP = 100
szornyHP = 100
while harcosHP > 0 and szornyHP > 0:
    #harcos köre:
    sebzes = 0
    while True:
        print("Dobj egyet a kockával (enter): ")
        input()
        kocka = random.randint(1,6)
        print(f"A dobásod: {kocka}")
        if kocka == 1:
            print("Elestél, ebben akörben nem sebezted meg a szörnyet")
            break
        
        valasz = input("Szeretnél újat dobni? (i/n)")
        sebzes += kocka
        if valasz == "n":
            break
        
        szornyHP -= sebzes
        print(f"A szörny HP-ja: {szornyHP}")
        #szörny köre:
        sebzes = 0
        for i in range (3):
            kocka = random.randint(1,6)
            print(f"A szörny dobása: {kocka}")
            sebzes += kocka
        harcosHP -= sebzes
        print(f"A harcos HP-ja: {harcosHP}")
    if harcosHP > szornyHP:
        print("A harcos véres küzdelemben legyőzte a szörnyet, és elnyerte a hercegnő kezét!")
    else:
        print("A szörny véres küzdelemben legyőzte a rendíthetetlen harcost :(")
        