luku = (input('Syötä luku: '))

maksimi = 0
minimi = 0

while luku != '':

    if maksimi == 0 or luku > maksimi:
        maksimi = luku

    if minimi == 0 or luku < minimi:
        minimi = luku

    luku = (input('Syötä luku: '))

else:
    print(f'Suurin syötetty luku: {maksimi:}')
    print(f'Pienin syötetty luku: {minimi:}')