luku = input('Syötä kokonaislukuja. Tyhjä lopettaa: ')

lista = []

while luku != '':
    lista.append(int(luku))
    for i in lista:
        lista.sort(reverse = True)

    luku = input('Syötä kokonaislukuja. Tyhjä lopettaa: ')

else:
    print(lista[0:5])