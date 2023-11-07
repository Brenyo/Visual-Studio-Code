sutik = ['csokis brownie', 'almás pite', 'mogyorós keksz', 'mézeskalács', 'kókuszos szelet', 
'tejszínes pite', 'citromos muffin', 'vaníliás fánk', 'eperkrém torta', 'almás-fahéjas palacsinta', 
'karamellás popcorn', 'mandulás torta', 'datolyás sütemény', 'túrófánk', 'meggyes pite', 'almás süti', 'puncsos torta', 'citromhabos sütemény', 'diós tekercs', 'narancsos piskóta']

def f1():
    print(f"A sütik száma: {len(sutik)}")

def f2():
    db = 0
    for item in sutik:
        if "csoki" in item:
            db += 1
            print(item, end=" ")
    print(f"Csokis sütik száma: {db}")

def f3():
    maxi = sutik[0]
    for item in sutik:
        if len(item) > len(max):
            max = item
    print(f"A leghoszabb sütinév: {max}")
    
def f4():
    sutik.sort()
    print(*sutik, sep= ", ")
    
def f5():
    muffinok=[]
    for item in sutik:
        if "muffin" in item:
            muffinok.append(item)
    print(muffinok)
    
def f6():
    if "mogyorókrémes linzer" in sutik:
        print("Szerepel a mogyorókrémes linzer a listában")
    else:
        print("Nem szerepel a mogyorókrémes linzer a listában")
        
def f7():
    list = []
    for item in sutik:
        if item[0] in "acm":
            list.append()
    print(*list, sep="\n")     
        
def f8():
    osszkaloria = len(sutik)*2 *120
    print(f"összkalória, ha mindegyikből 2 szeletet eszünk: {osszkaloria}")
        
def f9():
    for i in range(0, len(sutik), 2):
        print(sutik[i])    
        
def f10():
    ujlista = []
    for item in sutik:
        ujlista.append(item[::-1])
    print(*ujlista, sep="\n")
        
def main():
    f7()