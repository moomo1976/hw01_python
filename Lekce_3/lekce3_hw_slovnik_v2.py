#   Translator - jen malinký
#   Chtěl jsem bych přidat i nějaký ten skok na jinou oblast, ale tam si nejsem jistý.
#   Vždy kdzž jsem něco přidal, tak jsem spíš zamotal, ale chybami se učím a posunuji dál.
#   Vím, kde mám mezery, tak na tom jěště pořádně musím máknout.
#
print('\nAhoj jsem jen opravdu malý translátorek')
print('---------------------------------------\n')

dictionary = {'ahoj':'hi','nashledanou':'goodbye', 'děkuji':'thank you', 'dobrý večer':'good evening', 'kolik':'how', 'čas':'time', 'prosím':'please', 'pomoc':'help','dobrý':'good', 'špatný':'bad'}
word = input('Zadej slovo: ')

if word not in dictionary:
    print ('\nTakovéto slovo se ve slovníku nenachází! h\nJá, jsem jen malý slovníček, ale můžeš mě rozšířit paměť.\nPokud mě chceš rozšířit\nzadej ano/yes\n')
    quit
else:
    print('Zadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])

choice=(input())
if choice=='ano'or'ANO'or'yes'or'YES':
    print('\nVýpis aktualního slovníku:',dictionary)    #print(dictionary)
    input("\nPro pokračování k novému překladu input\nStiskněte libovolnou klávesu...\n")
     #   Tady přesné klonuji kód, který už tu jednou mám. Vím, že to je zbztečný a řešit bych to měl jinak.
    word = input ('Zadej slovo: ')
    if word not in dictionary:
        print ('\nTakovéto slovo se ve slovníku nenachází! \nJá, jsem jen malý slovníček, ale můžeš mě rozšířit paměť.\nPokud mě chceš rozšířit\nzadej ano/yes\n')
        input("\nStiskněte libovolnou klávesu a program se ukončí\n")
        quit
    else:
        print('Zadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])

else:
    print('\n')
    input("\nStiskněte libovolnou klávesu a program se ukončí\n")

quit
