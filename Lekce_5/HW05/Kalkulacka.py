# Kalkulajda "Majda" - HW05
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


def calculator():
    print("\n")

    try:
        num1 = float(input("Prosím zadej první cislo: "))
        num2 = float(input("Prosím zadej druhé cislo: "))
    except ValueError: #Více o "ValueError" na https://docs.python.org/3/tutorial/errors.html
        print("Zadaná hodnota je špatná\nVypíše se originální chybová hláška v ANG:")
        print(ERROR)
        print("Chyba - nemohl jsem převést řetězec na float: 'lkkl'")
        print("\n"+"Zkus zadat ještě jednou")
        return


    opp = input("Zadej operaci, co budeme dělat?\n""+ pro sčítání\n- pro odečítání\n* pro násobení\n/ pro dělení\n")

    print("Zadal si mi tento příklad:\n",num1, opp, num2)


    if opp == "+":
        ans = num1 + num2

    elif opp == "-":
        ans = num1 - num2

    elif opp == "*":
        ans = num1 * num2

    elif opp == "/":
        try:
            ans = num1 / num2
        except ZeroDivisionError as ERROR:
            print("Invalid equation\n")
            print("\nPodle standardních pravidel aritmetiky není dělení nulou v oborech přirozených čísel, \ncelých čísel, racionálních čísel, reálných čísel a komplexních čísel (nerozšířených o nekonečno) \ndefinováno. neboť jakékoli číslo násobené nulou je nula, nikoli šest. nedává smysl a výsledek \ndělení nulou tak není definován. \nVypíše se originální chybová hláška v ANG:")
            print(ERROR)
            print("\nZkus zadat ještě jednou")
            return

    else:
        ans = "špatná operace, zkus to znovu:"

    print(f"Výsledek příkladu se ={ans}")  # formátování přes f-řetězec.




while True:
    calculator()



