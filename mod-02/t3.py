kanta = input('Syötä suorakulmion kannan pituus: ')
korkeus = input('Syötä suorakulmion korkeus: ')

piiri = float(korkeus) * 2 + float(kanta) * 2
pinta_ala = float(kanta) * float(korkeus)

print(f'Suorakulmion piiri: {piiri}')
print(f'Suorakulmion pinta-ala: {pinta_ala}')