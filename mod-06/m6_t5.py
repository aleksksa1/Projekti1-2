def lista2(original):
    parilliset = []

    for numero in original:
        if numero % 2 == 0:
            parilliset.append(int(numero))
    return parilliset

original = []

numero = (input('Syötä kokonaisluku (Enter lopettaa): '))

while numero != '':
    original.append(int(numero))
    numero = (input('Syötä kokonaisluku (Enter lopettaa): '))

print(f'Alkuperäinen lista: {original}')
print(f'Vain parillisten lista: {lista2(original)}')