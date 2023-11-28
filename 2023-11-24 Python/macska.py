class Cat:
    Nev = ""
    EletSz = 9
    def __init__(self, nev, elet):
        self.Nev = nev
        self.EletSz = elet
        
    def halal(self):
        for i in range(self.EletSz):
            if self.EletSz > 0:
                self.EletSz -= 1
            elif self.EletSz == 0:
                print("A macska halott!")
                
        