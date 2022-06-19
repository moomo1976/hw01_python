# HW02 - vytvořte seznam všech českých měsíců
# program vypište 3. a 6. měsíc v roce.
#================================================================
# Seznam měsíců v roce 1. až 6.
months = ['Leden','Únor','Březen','Duben','Květen','Červen']

# Rozšíření stávajícího seznamu měsícu o 7. až 12. měsíc.
months.extend(['Červenec','Srpen','Září','Říjen','Listopad','Prosinec'])

# Výběr a výpis ze seznamu je proveden z obou stran za použití znaménka "-"
# Výběr měsíce "Červen := z levé str.indexu [5]  a z pravé strany  hodnotě [-7]
print("\nDle zadání má program vypsat:\n \t\t\t\t 3. a 6. měsíc je:" , months[2], "a", months[-7],"\n\n")
print("Jako bonus výpíšeme měsíce dle období: \n")
print("Jarní měsíce jsou tyto: \t", months[2],"-", months[3],"-", months[-8])
print("Letní měsíce jsou tyto: \t", months[5],"-", months[-6],"-", months[7])
print("Podzimní měsíce jsou tyto: \t", months[8],"-", months[9],"-", months[10])
print("Zimní měsíce jsou tyto: \t", months[11],"-", months[-12],"-", months[1],"\n\n\n")

# Bonus
# Zjištění délky seznamu
delka = len(months)
print("Seznam celkem obsahuje počet měsíců:\t",delka, "\n\n\n")