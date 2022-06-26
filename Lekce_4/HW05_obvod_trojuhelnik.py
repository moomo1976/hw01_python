#Obvod trojůhelníku
def obvod():
    strany = []
    print("\n")
    for step in range(3):
        print("zadej ",step+1, ". stranu: ", sep="", end="")
        strany.append(int(input()))
    strany.sort()
    if (strany[0]+strany[1]>strany[2]):
        print("Výsledný obvod je: ",sum(strany))
    else:
        print("Špatný poměr stran, to není možné provést.")
print("\nTady spočítám obvod trojuhelníku")
obvod()