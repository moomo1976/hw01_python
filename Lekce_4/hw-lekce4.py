# Home Work - Lekce 4 
#! Cvičení 1.
# Pomocí cyklu vypíše malou násobilku pro č.5
# -uvnitř cyklu bude: print(i, "x 5= ", i*5)
#-------- CVIČENÍ 1 CYKLUS FOR ------------
print("CVIČ 1: Násobilka pro číslo - CYKLUS FOR\n-----------------------------------------") 

for i in (1,2,3,4,5):
    print(i, "x 5= ", i*5)  

#----- CVIČENÍ 1 CYKLUS FOR IN RANGE ------
print("\nCVIČ 1: CYKLUS FOR IN RANGE\n-----------------------------\n")

for i in range(1,6):
    print(i, "x 5= ", i*5)

#!Cvičení 2.
# Vytvořte cyklus (FOR) pro projití celého seznamu
# -máte seznam měsíců
# -mesice = ["leden", "únor", "březen", "duben", 
# "květen", "červen", "červenec", "srpen", "září",
# "říjen", "listopad", "prosinec"]
#-----------------------------------------------------

print("\nCVIČ 2:  Projití celého seznamu měsíců\n---------------------------------------\n")

print("Výpis měsíců:\n-------------")
mesice = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
index = 1
for index in range(12):
  print(index+1, mesice[index]) 
print("\n")
# >index+1< z důvodu správného číslovaní měsíců
# pokud bych nepřičetl +1 za index, počítal by mi měsíce od nuly
# což je správně, ale já jsem chtěl přiřadit správné číslovaní měsíců


#!Cvičení 3.
# Vytvořte cyklus (WHILE) který vypíše všechny položky
# seznamu planety aniž by znal počet planet, tady bude
# fungovat i když přidáváte nebo ubíráte ze seznamu.
# Víte jen,že poslední položka seznamu která se 
# nevypisuje je KONEC
#-----------------------------------------------------

#! Horizontální výpis 
print("CVIČ 3: Cyklus (WHILE) který vypíše všechny položky horizontálně\n-----------------------------------------------------------------")
n = 0
planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
while planety[n] != "KONEC":
  planety[7] = "KONEC"
  planety[8] = "Neptun"
  print(planety[n], end=", ")
  n = n + 1 
print(planety[8], end="")
print("\n")
#! Řešil jsem tu podobnou situaci jako v bonus 2, akorat tu je seznam.


#! Verikální výpis 
print("CVIČ 3: Cyklus (WHILE) který vypíše všechny položky - vertikálně\n-----------------------------------------------------------------\n")
n = 0
planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
while planety[n] != "KONEC":
  print(planety[n])
  n = n + 1 

print("\n")

#!-Bonus 2---------------------------------------------------------------
#? Bonus 2 - ten je pro mě oříšek, tak se nechám podat.
#? Pokusím se zítra ještě a uvidíme.

#for i in range (2,21,2):
#  print(i, end=",")
#print("\n")
#
#
#v=[]
#print("Násobky")
#for i in range(0,21,2):
#  v.append(i)           
#print(v)
#print("\n")


