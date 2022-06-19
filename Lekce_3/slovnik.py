print('\nAhoj jsem jen opravdu malý translátorek')
print('---------------------------------------\n')

dictionary = {'ahoj':'hi','nashledanou':'goodbye', 'děkuji':'thank you', 'dobrý večer':'good evening', 'kolik':'how', 'čas':'time', 'prosím':'please', 'pomoc':'help','dobrý':'good', 'špatný':'bad'}
word = input('Zadej slovo: ')

if word not in dictionary:
    print ('\nTakovéto slovo se ve slovníku nenachází! h\nJá, jsem jen malý slovníček, ale můžeš mě rozšířit paměť.\nPokud mě chceš rozšířit\nzadej ano/yes\n')

else:
    print('Zadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])
    print('\nSlovíčko jsem ti přeložil, tak to je asi vše.\n\nKonec programu')
    input("\nStiskněte libovolnou klávesu a program se ukončí\n")


choice=(input())
if choice=='yes'or'ano':
    print('\nVybral si "ano" Jsem moc rád, že si se rozhodl mi rozšířit slovní zásobu\n')
    slovo_cz = input("zadej slovo česky: ")
    slovo_gb = input("zadej slovo anglicky: ")
    print('\n')
    dictionary[slovo_cz] = slovo_gb
    print(dictionary)
    print('\n')
    print('\n Slovo se přidalo na poslední místo slovníku')
    print('\nVýpis aktualního slovníku:',dictionary)    #print(dictionary)
    input("\nPro pokračování k novému překladu input\nStiskněte libovolnou klávesu...\n")
    word = input ('Zadej slovo: ')
    if word not in dictionary:
        print ('\nTakovéto slovo se ve slovníku nenachází! \nJá, jsem jen malý slovníček\n')
        input("\nStiskněte libovolnou klávesu a program se ukončí\n")
        quit
    else:
        print('Zadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])
else:
    print('\n')
    input("\nStiskněte libovolnou klávesu a program se ukončí\n")

