#1. feladat:
import random
"""
list = []

for i in range (10):
    rnd = random.randint(5, 10)
    list.append(rnd)

print(list)

#2. feladat:
list2 = []
for j in range(15):
    rnd2 = random.randint(0,1)
    list2.append(rnd2)
    if list2[j] < 1:
        print("HAMIS", end= " ")
    else:
        print("IGAZ", end= " ")

#3. feladat:
list3 = []
for i in range(25):
    rnd = random.randint(1,20)
    list3.append(rnd)
    if list3[i] % 2 != 0:
        print(list3[i]*list3[i], end=" ")

#4. feladat:
list = []
for j in range(5):
    rnd = random.randint(1,50)
    list.append(rnd)
for i in range(5):
    bekertSzam = int(input("Kérek egy számot! (1-5):"))
    if bekertSzam > 0 and bekertSzam < 6:
        list.append(bekertSzam)


print(list, end=" ")
print(" ")
list.reverse()
print(list, end=" ")
list.reverse()
print(" ")
for i in range(1,len(list), 2):
    print(list[i], end=" ")

#5. feladat:
a = []
b = []
sum = 0
for i in range (10):
    a.append(random.randint(1,10))
    b.append(random.randint(1,10))
    sum += a[i]
    sum += b[i]
c = []
c.append(sum)
print(c)

#7. feladat:
a = []
input = int(input("Hány elem legyen a listában: "))
for i in range(input):
    a.append(random.randint(1,100))
print(a)
a.reverse()
print(a)   
   
#8. feladat:

a = []
sum = 0
input = int(input("Hány elem legyen a listában: "))
for i in range(input):
    a.append(random.randint(1,20))
    sum += a[i]
print(a)
print(sum)   
"""

#12. feladat:

list = []
for j in range(20):
    rnd = random.randint(-100,100)
    list.append(rnd)
print(list)
for i in range(2,len(list), 3):
    list[i] += 1
print(list)
        
        
    