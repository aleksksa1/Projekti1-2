import random

lukumaara = int(input('Kuinka monta kertaa noppaa heitetään?: '))

summa = 0

for i in range(lukumaara):
    heitto = random.randint(1, 6)
    summa += heitto

print(f"Silmälukujen summa: {summa}")
