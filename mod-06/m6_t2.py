import random

tahkot = int(input('Syötä nopan suurin silmäluku: '))

def nopanheitto(tahkot):
    return random.randint(1, tahkot)

noppa = 0

while noppa != tahkot:
    noppa = nopanheitto(tahkot)

    print(f'Nopan silmäluku: {noppa}')