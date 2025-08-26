kayttaja = input('Syötä käyttäjätunnus: ')
salis = input('Syötä salasana: ')

lukitus = 0

while kayttaja != 'python' or salis != 'rules':

    lukitus = lukitus + 1
    if lukitus == 5:
        print('Pääsy evätty')
        break

    print('Käyttäjätunnus ja/tai salasana väärin. Yritä uudelleen.')
    kayttaja = input('Syötä käyttäjätunnus: ')
    salis = input('Syötä salasana: ')

else: print('Tervetuloa!')