#obsah trouhelniku
def obs_troj (vyska_c, c):
    s = vyska_c*c/2
    return s
vys_c = float(input("Zadej výšku c: "))
str_c = float(input("Zadej stranu c: "))

obsah = obs_troj(vys_c,str_c)
print("Obsah trojůhelníku se str. c délce =", str_c, "a při výšce Vc =", vys_c, "je:", obsah)
qq