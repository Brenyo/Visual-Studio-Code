egyikirany =[]
masikirany = []
with open("C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/sebessegmero.txt", mode="r", encoding="utf-8") as fajl:
    for i in fajl:
        if '-' in i[0]:
            egyikirany.append(i.strip())
        else:
            masikirany.append(i.strip())

egyik = 0
masik = 0
for f in egyikirany:
    egyik += len(f)
for j in masikirany:
    masik += len(j)
    
if egyik > masik:
    print("Az egyik irányban mentek többen.")
else:
    print("Az másik irányban mentek többen.")

 
total = 0
for i in egyikirany:
    total = total + int(i)
    
print(f"Az egyik irányban {total/len(i)}-el/al mentek átlagben")

totala = 0
for i in masikirany:
    totala = totala + int(i)
    
print(f"A másik irányban {totala/len(i)}-el/al mentek átlagben")


def read_file(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        words = file.read().split()
    return words

def szures(words):
    return [word for word in words if len(word) > 8]

def terkepezes(words):
    return [word.upper() for word in words]


def szamolas(words):
    return sum(len(word) for word in words)


def kivalogatas(words):
    vowel_starting_words = [word for word in words if word[0].lower() in 'aeiou']
    for word in vowel_starting_words:
        print(word)

import random

def veletlen(words):
    random_word = random.choice(words)
    print(f"Véletlenszerűen kiválasztott szó: {random_word}")
    print(f"Visszafelé írva: {random_word[::-1]}")


def reszek(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

filename = "C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/szavak.txt"
szavak = read_file(filename)


hosszabb_szavak = szures(szavak)
nagybetus_szavak = terkepezes(szavak)
osszes_hossz = szamolas(szavak)
kivalogatott_magánhangzós_szavak = kivalogatas(szavak)
veletlen_szó_visszafelé = veletlen(szavak)
szó_előfordulások = reszek(szavak)


def read_plants(filename):
    with open(filename,  mode="r", encoding="utf-8") as file:
        plants = file.read().splitlines()
    return plants


def lowercase_plants(plants):
    return [plant.lower() for plant in plants]


def print_plants(plants):
    for plant in plants:
        print(plant)


def count_plants(plants):
    count = len(plants)
    print(f"A fájlban {count} gyógynövény szerepel.")


def search_plant(plants, search):
    if search.lower() in plants:
        print(f"{search} megtalálható a listában.")
    else:
        print(f"{search} nem található meg a listában.")


def vowel_starting_plants(plants):
    vowel_starting = [plant for plant in plants if plant[0].lower() in 'aeiou']
    return vowel_starting

def sort_and_print_plants(plants):
    sorted_plants = sorted(plants)
    print("Gyógynövények abc szerinti sorrendben:")
    print(", ".join(sorted_plants))


filename = "C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/novenyek.txt"
gyogynovenyek = read_plants(filename)


gyogynovenyek_kisbetus = lowercase_plants(gyogynovenyek)
print_plants(gyogynovenyek_kisbetus)
count_plants(gyogynovenyek)
keresett_noveny = input("Kérem, adjon meg egy gyógynövény nevet: ")
search_plant(gyogynovenyek_kisbetus, keresett_noveny)
magánhangzóval_kezdődő_novenyek = vowel_starting_plants(gyogynovenyek_kisbetus)
sort_and_print_plants(magánhangzóval_kezdődő_novenyek)

def check_names(filename):
    correct_names = []
    corrected_names = []

    with open(filename, mode="r", encoding="utf-8") as file:
        names = file.read().splitlines()

    for name in names:
        words = name.split()
        if all(word.istitle() for word in words) and len(words) >= 2:
            correct_names.append(name)
        else:
            corrected_names.append(' '.join(word.capitalize() for word in words))

    with open('megfeleloek.txt', 'w') as file:
        file.write('\n'.join(correct_names))

    with open('javitott.txt', 'w') as file:
        file.write('\n'.join(corrected_names))

filename = "C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/nevek.txt"
    
def process_students(filename):
    subjects = {}
    students = []

    with open(filename, 'r') as file:
        data = file.readlines()

    for line in data:
        student, subject = line.strip().split(' ')
        students.append(student)
        if subject in subjects:
            subjects[subject].append(student)
        else:
            subjects[subject] = [student]

    num_students = len(set(students))
    chosen_subjects = list(subjects.keys())

    print(f"Az osztályba {num_students} diák jár.")
    print(f"Az osztályban szereplő tantárgyak: {', '.join(chosen_subjects)}")

    for subject, students in subjects.items():
        print(f"{subject} tantárgyat {len(students)} diák választotta.")
        print(f"{subject} tantárgyat választó diákok: {', '.join(students)}")

filename = "C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/vizsga.txt"

def process_vehicle_data(filename):
    print("Út (km) Össz (l) Átlag (l/100 km)")
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        distance, fuel = map(float, line.split())
        avg_consumption = (fuel / distance) * 100
        print(f"{distance} {fuel} {avg_consumption:.1f}")

filename = "C:/Users/Bence Piller/OneDrive - BMSZC Petrik Lajos Két Tanítási Nyelvű Technikum/SULIS ANYAG/PYTHON/2023-11-19/07/fogyasztas.txt"

