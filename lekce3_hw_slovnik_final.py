# -----------------------Translator CZ-->ANG    HW-03--------------------------
#        Trochu jsem se zamotal a vím, že to není úplně dokonalé.                           
print('\n            Ahoj jsem jen opravdu malý translátorek                 ')
print('----------------------------------------------------------------------')
print('ahoj-nashledanou-děkuji-dobrý večer-kolik-čas-prosím-pomo-dobrý-špatný')
print('----------------------------------------------------------------------\n')
#    dictionary
dictionary = {'ahoj':'hi','nashledanou':'goodbye', 'děkuji':'thank you', 'dobrý večer':'good evening', 'kolik':'how', 'čas':'time', 'prosím':'please', 'pomoc':'help','dobrý':'good', 'špatný':'bad'}
word = input ('Zadej slovo české slovo k překladu: ')

# info ohledně nanalezeného slova a překladu
if word not in dictionary:
    print ('\nTakovéto slovo se ve slovníku nenachází! \nJá, jsem jen malý slovníček, ale můžeš mě rozšířit paměť.\nPokud mě chceš rozšířit\n\nZadej:\n\n "ano" pro přidání slova do slovníku\n')
else:
    print('\nZadané české slovo: ', word,'se anglicky řekne: ', dictionary[word])
    #stop
    # Rozšíření slovníku
choice=(input())
if choice=='ano':
    print('Vybral si ano. Jsem moc rád, že si se rozhodl mi rozšířit slovní zásobu')
    slovo_cz = input('Zadej slovo česky: ')
    slovo_gb = input('Zadej slovo anglicky: ')
    print('\n')
    dictionary[slovo_cz] = slovo_gb
    print(dictionary)
    print('\n')
    print('\n Slovo se přidalo na poslední místo slovníku')
    
else: 
    print( '\nSlovo jsem ti přeložil, tak ukončím program.\nJeště předtím ti vypíšu jaké mám slovíčka v paměti...\n')
    print(dictionary, '\n\nA to je vše...')

input('\nStiskněte libovolnou klávesu...')