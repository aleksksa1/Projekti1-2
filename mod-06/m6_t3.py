def litra(gallona):
    muunnos = gallona * 3.785
    return muunnos

gallona = float(input('Syötä gallona määrä, jonka haluat litroina: '))

while gallona >= 0:
    print(litra(gallona))
    gallona = float(input('Syötä gallona määrä, jonka haluat litroina: '))

else:
    print('Negatiivinen määrä.')