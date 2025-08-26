import math

kaikkipisteet = float(input('Syötä arvottavien pisteiden määrä: '))

ympyrapisteet = kaikkipisteet * math.pi / 4

piinlikiarvo = 4 * ympyrapisteet / kaikkipisteet

print(f'Piin likiarvo: {piinlikiarvo}...')