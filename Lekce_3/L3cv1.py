#Lekce 3 -Seznam zboží + na skladě
zbozi = {"Olivový olej 5l":15, "Rajčata sušená 150g":25, "Olivy Kalamata 250g":50, "Lilek":100, "Cuketa":80, "Oregáno suš 50g":150,"Feta 1kg":50}
print("Vypis položku zboží: Lilek",zbozi["Lilek"], "ks skladem")
print("Vypis položku zboží: Cuketa",zbozi["Cuketa"], "ks skladem")

# Aktualizace skladu - položka Likek 100 - 30 =70 ks
zbozi["lilek"] =70
print("Lilek změna stavu:", zbozi["lilek"],"aktualizováno ks na skladě")







# PŘIDÁNÍ položkY do SLOVNÍKU
zbozi["Ouzo"] = 55
# mazani položkY do SLOVNÍKU
del zbozi["Ouzo"]
# PŘIDÁNÍ položkY do SLOVNÍKU
zbozi["Ouzo 750ml"] = 55
# Přepsání položky do SLOVNÍKU
zbozi["Ouzo 1l"] = zbozi["Ouzo 750ml"]
del zbozi["Ouzo 750ml"]
# Výpis SLOVNÍKU
print(zbozi)





