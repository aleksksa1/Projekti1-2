import random

luku = random.randint(1,10)

arvaus = float(input('Syötä luku, jota arvaat (1-10): '))

while arvaus != luku:

    if arvaus < luku:
        print('Liian pieni arvaus')
    if arvaus > luku:
        print('Liian suuri arvaus')

    arvaus = float(input('Syötä luku, jota arvaat(1-10): '))

else: print('Oikein!')