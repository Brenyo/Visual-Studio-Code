"""
szoveg = "Egy fecske nem csinál nyarat!"

#for i in range(kezdőérték, végérték, lépésköz)
for i in range(10):
    print(szoveg, end=" ")
for i in range(2, 21, 2):
    print(i, end=" ")
print()


N = int(input("Kérem mondja meg, hányszor írjuk ki a szöveget: "))
for i in range(1, N+1):
    print(f"{i}. Megmondtam már {N}-szer, hogy nem írom ki kétszer!")
for i in range(1,100):
    if i % 7 == 0:
        print(i, end=" ")

#3
for i in range(7,100,7):
    print(i, end=" ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
kicsi = min(a,b)
nagyobb = max(a,b)
for i in range(kicsi, nagyobb+1,c):
    print(i, end=" ")
print()

num = 0
num2 = 0
for i in range(43):
    num += i
print(num)
print(num2)
num = 0
for i in range(1000, -1, -1):
    if i % 2 == 0 and i % 3 == 0:
        num += 1
print(num)
data = int(input("Kérek egy számot!: "))
num = 1
for i in range(1,data+1):
    num *= i
print(num)
"""
for i in range(1, 11):
    for j in range(1, 8):
        print(f"{i:2}*{j:2} = {i*j:3}", end="   ")











