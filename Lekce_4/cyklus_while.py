#while

# zadání: napište kód pro průchod seznamem u kterého nevíte jak je dlouhý
# planety = ["Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
# planety = ["Merkur", "Venuše", "Uran", "Neptun", "KONEC"]
# planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
# použijte cyklus WHILE s podmínku dokud není položka rovna “KONEC”


#planety = ["Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
#while pocitej < 100:
#    print(pocitej)
#    pocitej = pocitej + 2
#

#n = 0
#planety = ["Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
#while planety[n] != "KONEC":
#  print(planety[n])
#
#n = n + 1 
#planety = ["Merkur", "Venuše", "Uran", "Neptun", "KONEC"]
#while planety[n] != "KONEC":
#  print(planety[n])
#    n = n + 1 

#n = 0
#planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
#while planety[n] != "KONEC":
#  print(planety[n])
#  n = n + 1 
  
#-----------------------------------------------------
# Vytvořte cyklus (FOR) pro projití celého seznamu
# -máte seznam měsíců
# -mesice = ["leden", "únor", "březen", "duben", 
# "květen", "červen", "červenec", "srpen", "září",
# "říjen", "listopad", "prosinec"]
#-----------------------------------------------------

#print("Výpis měsíců:\n-------------")
#mesice = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]
#index = 1
#for index in range(12):
#  print(index+1, mesice[index]) 
  
# >index+1< z důvodu správného číslovaní měsíců
# pokud bych nepřičetl +1 za index, počítal by mi měsíce od nuly
# což je správně, ale já jsem chtěl přiřadit správné číslovaní měsíců

#print("Násobky")
#for i in range (2,21,2):
#  print(i, end=",")
#print("\n")
#
#
#v=[]
#print("Násobky")
#for i in range(0,21,2):
#  v.append(i)           
#  print(v)
#print("\n")


#n = 0
#while n < 21:
#  print(n, end=", ")
#  n = n + 2


print("Násobky")
for i in range (2,21,2):
  print(i, end=",")
print("\n")


print("Násobky")
for i in range(0,19,2):       
print("\n")

#  v=[]
#  print("Násobky")
#  for i in range(0,21,2):
#  v.append(i)           
#  print(v)
#  print("\n")

