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

n = 0
planety = ["Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
while planety[n] != "KONEC":
  print(planety[n])

n = n + 1 
planety = ["Merkur", "Venuše", "Uran", "Neptun", "KONEC"]
while planety[n] != "KONEC":
  print(planety[n])
    n = n + 1 

planety = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun", "KONEC"]
while planety[n] != "KONEC":
  print(planety[n])
  n = n + 1 