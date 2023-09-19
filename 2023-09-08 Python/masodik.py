print("""
        *
       * *
      *   *
     *     *
    *       *
   *         *
  *           *
 * * * * * * * *
      """)
print("-------------------------------------------------------------------------------\n")

print("\t *\n\t* *\n       *   *\n      *     *\n     *       *\n    * * * * * *\n")

print("-------------------------------------------------------------------------------\n")

print("      *")
print("     * *")
print("    *   *")
print("   *     *")
print("  *       *")
print(" * * * * * *\n")

print("-------------------------------------------------------------------------------\n")

print("""
|-------------|
| Programozás |
|-------------|
| Programozás |
|-------------|
      """)

print("-------------------------------------------------------------------------------\n")

print("|-------------|\n| Programozás |\n|-------------|\n| Programozás |\n|-------------|\n")

print("-------------------------------------------------------------------------------\n")

print("|-------------|")
print("| Programozás |")
print("|-------------|")
print("| Programozás |")
print("|-------------|")

print("-------------------------------------------------------------------------------\n")

print("""
****************
* Falusi Bence *
****************
      """)

print("-------------------------------------------------------------------------------\n")

print("****************\n* Falusi Bence *\n****************")

print("-------------------------------------------------------------------------------\n")

print("****************")
print("* Falusi Bence *")
print("****************")

print("-------------------------------------------------------------------------------\n")

nev = "Bence"
magassag = 178.8 # valós számoknál tizedespontot használunk
szuletesiEv = 2004

print(type(nev), type(magassag), type(szuletesiEv), sep=" - ")

magassag = 179

print(type(magassag))

print("A neved: "+ nev) #konkatenáció: összefűzés
print("A neved:", nev)
print("A magasságod: ", magassag)
print("A magasságod: "+str(magassag))

print(f"A neved: {nev} - A magasságod: {magassag} - Születési Éved: {szuletesiEv}")

eletkor = 2023 - szuletesiEv

print(f"A jelenlegi korod: {eletkor}\n")

print("-------------------------------------------------------------------------------\n")

a = 5
b = 10
# változó létrehozása: deklaráció
# változó értéket adok egy változónak: inicializáció
print(f"A értéke: {a} -  B értéke: {b}")

print(f"B kétszerese = {2 * b}\n")
a = a + 1
a += 1
#operátorok: müveleti jelek
# = értékadó operátor
# += összevont értékadó operátor
#arithmetikai operátorok: + - * / //- egész osztás %- maradákos osztás
c = 10
print(f"{c/3}") #rendes osztás: valós számot: float
print(f"{c//3}") #egészrész osztás: levágja a maradékot
print(f"{c%3}") #csak a maradékot kapjuk eredményül