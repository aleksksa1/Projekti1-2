def laskin(lista):
    summa = 0
    for i in lista:
        summa = summa + i
    return summa

lista = []

numero = (input('Syötä kokonaisluku (Enter lopettaa): '))

while numero != '':
    lista.append(int(numero))
    numero = (input('Syötä kokonaisluku (Enter lopettaa): '))

print(f'Summa {laskin(lista)}')