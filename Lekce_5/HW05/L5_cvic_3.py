#20-06-2022
#! Cvičeniní 3 - LEKCE 5 - funkce může být něco jako vzoreček,
# obecný postup nebo algoritmus
#CV3: Vytvořte funkci pro výpočet obsahu trojúhelníku
#

def obsah_trojuhelniku (vyska_c, c):
   s = vyska_c * c / 2
   return s

vc = 10
sc = 4
obsah = obsah_trojuhelniku(vc,sc)
print("Obsah trojůhelníku se stranou c =", sc, "a výškou Vc =", vc, "je:", obsah)

#práce se znaky
print("znaky:")
print(chr(65))
print(ord('A'))
ch = ord('A')+3 