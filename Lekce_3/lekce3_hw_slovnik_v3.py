
line = 1

dictionary = {'ahoj':'hi','nashledanou':'goodbye', 'děkuji':'thank you', 'dobrý večer':'good evening', 'kolik':'how', 'čas':'time', 'prosím':'please', 'pomoc':'help','dobrý':'good', 'špatný':'bad'}

word = input ('Zadej slovo: ')

if word not in dictionary:
    print ('\nTakovéto slovo se ve slovníku nenachází! \nJá, jsem jen malý slovníček, ale můžeš mě rozšířit paměť.\nPokud mě chceš rozšířit\n\nVyber a zadej:\n\n"1" pro ANO PŘIDÁNÍ slova do slovníku\n"2" pro návrat na začatek programu\n')


else:
    print('Zadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])


    if line==:
        response = input('yes/ano or no/ne')
        if response =='yes' or 'ano':
            print('Vybral si "Ano" Jsem moc rád, že si se rozhodl mi rozšířit slovní zásobu')
            print('\n')
            slovo_cz = input("zadej slovo česky: ")
            slovo_gb = input("zadej slovo anglicky: ")
            print('\n')
            dictionary[slovo_cz] = slovo_gb
            print('\n Slovo se přidalo na poslední místo slovníku')
            print('\n Chceš zkusit znovu přeložit? A/N:\n')
            yes_no =(input("Zadej ano, nebo ne "))
            if yes_no == 'yes' or "ano":
                print('\n Super douhlasíš a vyzkoušíš mě znovu')
                goto(8)
    else:
        print('\n Mryí mě, že mi nedáš šanci ykusit to ještě jednou.')
    quit

   
else: 
    print( "No nepotěšil si mě, ani já tě nepotěším a rovnou raději ukončíme spolupráci")
    print( "Ještě předtím ti vzpíšu jaké mám slovíčka v paměti...")
    print(dictionary)
    
print('\n')


print('\n')

input("\nStiskněte libovolnou klávesu...")

