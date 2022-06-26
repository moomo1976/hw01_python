# Kalkulajda "Majda" - HW05
# Seznam funkcí, které zavoláme pomocí While True...
# ?   -zatím úplně nevím, jak ještě zakomponuji odmocninu,ale
# ?    pokusím se na to přijít, až rozjedu to a, b.
#   Zakomponovat mocninu a odmocninu, nebylo tak úplně těžké,
#   Stačilo se nad tím jen trochu zamyslet a projít si definece.
#
#  Kolikrát během psaní programu se mi stane, že už dopředu vidím,
#  co by jsem chtěl opět upravit, doplnit, nebo hlídat.

#? ****************************** Tady mě napadá otázka Radku? *********************************
#? 1) Je lepší si udělat poznámku bokem a zabívat se tím později, až bude kostra programu funkční
#? 2) Nebo ji hned začit řešit ? "Možná to bude asi také záležet jaký to je kus od kusu :)"


rovnase = "Výsledek zadaného přikladu je:"
nanekolikatou = "Výsledek mocněného přikladu je:"
odmocni = "Výsledná odmocnina přikladu je:"
# 1 - Funkce s čítání
def soucet(a, b):
    return a + b

# 2 - Funkce odčítání
def odecet(a, b):
    return a - b

# 3 - Funkce násobené
def nasobek(a, b):
    return a * b

# 4 - Funkce dělění
def deleni(a, b):
    return a / b

# 5 -Funkce mocnina
def mocnina(x, n):
    x, n = num1, num2
    return x ** n

# 6 -Funkce odmocnina
def odmocnina(x, n):
    x = num1
    n = (1 / num2)
    return x ** n


while True:
    # výběr operace ze šesti funkcí
    # ! Seznam matematických funkcí kalkullajdy Majdy
    print("Zadej operaci, co budeme dělat.")
    print("1.Sčítání +")
    print("2.Odečítání -")
    print("3.Násobení *")
    print("4.Dělění /")
    print("5.Mocnění x² (pozn.druhé číslo je mocnitel)")
    print("6.Odmocnění √ (pozn.druhé číslo je mocnitel)")
    vyber_operace = input("Zadej číslo požadované operace (1/2/3/4/5/6): ")

    if vyber_operace in ('1', '2', '3', '4','5','6'):
        num1 = float(input("Prosím zadej první číslo typu float: "))
        num2 = float(input("Prosím zadej druhé číslo typu float: "))
        

        if vyber_operace == '1':
            print(rovnase, num1, "+", num2, "=", soucet(num1, num2))

        elif vyber_operace == '2':
            print(rovnase, num1, "-", num2, "=", odecet(num1, num2))

        elif vyber_operace == '3':
            print(rovnase, num1, "*", num2, "=", nasobek(num1, num2))

        elif vyber_operace == '4':
            print(rovnase,num1, "/", num2, "=", deleni(num1, num2))

        elif vyber_operace == '5':
            print(nanekolikatou,num1, "**", num2, "=", mocnina(num1, num2))

        elif vyber_operace == '6':
            print(odmocni,num1, "√", num2, "=", odmocnina(num1, num2))

    # Ukončení programu po zadání odpovědi (konec)  ---> ostatní pokračuje
    # while smyčka s odpovědí ne pro konec programu
        dalsi_priklad = input("Přeješ si pokračovat a vyřešit další příklad? \n\nPro ANO - Stiskni libovolnou klávesu.\nPro ukončení programu vypiš konec): ")
        if dalsi_priklad == "konec":
            break

    else:
        print("Neplatné zadání")