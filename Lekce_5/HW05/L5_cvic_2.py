#20-06-2022
#! Cvičeniní 2 - LEKCE 5 - jak vymyslet funkci

#   jak vymyslet funkci
def title(text):
    
   for i in range(0,len(text)+4):  # 'len' Return the length (the number of items) of an object.
       print("*",end="")

   print("\n*",text,"*")

   for i in range(0,len(text)+4):
       print("*",end="")

   print("\n")

title("Sluneční soustava")
title("Slunce")
title("Planety")
title("Planetky")
title("Měsíce")
title("Komety")
title("Asteroidy")

#funkce s parametry
def soucet(a, b):
   print("součet ", a, " + ",b ," =", a+b)

#použití fce s parametry
soucet(3, 8)

#funkce s návratovou hodnotou
def nasobeni(a, b):
   vysledek = a * b
   return (vysledek)

Radek Kitner18:52
def nadpis(text):
    delka = len(text)

    for i in range(delka+4):
        print("*", end="")
    print('')

    print("*",text,"*")

    for i in range(delka+4):
        print("*", end="")
    print('')


nadpis("Sluneční soustava")
nadpis("Slunce")
nadpis("Planety")
nadpis("Planetky")
nadpis("Měsíce")
nadpis("Komety")
nadpis("Asteroidy")