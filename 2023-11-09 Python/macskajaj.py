import random

def egyeniPontszam():
    return random.randint(0, 5) * 10

def csapatPontszam(csapat):
    pontok = []
    for i in range(4):
        pontok.append(egyeniPontszam())
    csapat.append(pontok)

def pontOsszesites(csapat):
    return sum([sum(jatekos) for jatekos in csapat])


