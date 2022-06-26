# Kalkulajda "Majda" - HW05
#Seznam funkcí, které zavoláme pomocí While True...
#?   -zatím úplně nevím, jak ještě zakomponuji odmocninu,ale
#?    pokusím se na to přijít, až rozjedu to a, b.

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

# 5 -Funkce 2.mocnina
def mocnina(x, n):
    return x ** n

#! Seznam matematických funkcí  kalkullajdy Majdy
print("Zadej operaci, co budeme dělat.")
print("1.Sčítání +")
print("2.Odečítání -")
print("3.Násobení *")
print("4.Dělění")
print("5.Mocnění")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        if choice == '1':
            print(num1, "+", num2, "=", soucet(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", odecet(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", nasobek(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", deleni(num1, num2))
        
        elif choice == '5':
            print(num1, "**", num1, "=", mocnina(num1,num1))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Přeješ si pokračovat a vzřešit dalčí příklad? (yes/no): ")
        if next_calculation == "ne":
          break
    
    else:
        print("Invalid Input")