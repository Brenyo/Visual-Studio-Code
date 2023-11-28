mozog = False
allo = False

class Vehicle:
    rendszam = ""
    def __init__(self, AutoRendszam):
        self.rendszam = AutoRendszam
    
    def start():
        if mozog == False:
            print("Az autó elindult!")
            mozog = True
            allo = False
        elif mozog == True:
            print("Az autó már mozog!")
    
    def stop():
        if allo == False:
            print("Az autó megállt!")
            allo == True
            mozog == False
        elif allo == True:
            print("Az autó már megállt!")