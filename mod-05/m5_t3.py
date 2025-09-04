luku = int(input('Syötä luku: '))

if luku < 2 or luku % 2 == 0:
    print(f'{luku} ei ole alkuluku.')

else:
    alkuluku = True
    for i in range(2, luku - 1):
        if luku % i == 0:
            alkuluku = False


    if alkuluku:
        print(f'{luku} on alkuluku.')

    else:
        print(f'{luku} ei ole alkuluku.')