gyumolcsok = []


with open("C:/Users/nessu/Documents/Visual Studio Code/2023-11-16 Python/gyumolcsok.csv",mode="r", encoding="utf-8") as raktar:
    for i in raktar:
        gyumolcsok.append(i.strip().split(";"))
        
osszes = 0
for i in gyumolcsok:
    print(*i)        
    osszes += int(i[1])
    
print(f"Gyümölcsök össztömege: {osszes}")
        
        
        
        
        
        
        
        