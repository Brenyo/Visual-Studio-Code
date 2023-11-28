class MathOperations:
    szam1 = 0
    szam2 = 0
    def __init__(self, sz1, sz2):
        self.szam1 = sz1
        self.szam2 = sz2
    
    def osszeadas(self):
        self.szam1 + self.szam2
    
    def kivonas(self):
        if self.szam1 > self.szam2:
            self.szam1 - self.szam2
        elif self.szam2 > self.szam1:
            self.szam2 - self.szam1
    
    def szorzas(self):
        if self.szam1 > 0 and self.szam2 > 0:
            self.szam1 * self.szam2
            
    def osztas(self):
        if self.szam1 > self.szam2:
            self.szam1 % self.szam2
        elif self.szam2 > self.szam1:
            self.szam2 % self.szam1