hallhato = False
elnemult = False

class Media:
    cim = ""
    eloado = ""
    
    def __init__(self, cim, eloado):
        self.cim = cim
        self.eloado = eloado
    
    def start():
        if hallhato == False:
            print("A zene hallható!")
            hallhato = True
            elnemult = False
        elif hallhato == True:
            print("A zene már megy!")
    
    def stop():
        if elnemult == False:
            print("A zene elnémult!")
            elnemult == True
            hallhato == False
        elif elnemult == True:
            print("Az zene már megy!")
    