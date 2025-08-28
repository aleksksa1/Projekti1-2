vuosi = float(input('Syötä vuosiluku: '))

if (vuosi % 4 == 0 and not vuosi % 100 == 0) or vuosi % 400 == 0:
    print('On karkausvuosi')

else: print('Ei ole karkausvuosi')