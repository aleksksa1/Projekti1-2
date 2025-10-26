import random

from classes.kilpailu import Kilpailu
from classes.auto10 import Auto

autot = []

for i in range(10):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i + 1), huippunopeus))

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot)

while not kilpailu1.kilpailu_ohi():
    for auto in autot:
        nopeusmuutos = random.randint(-10, 15)
        auto.kiihdyta(nopeusmuutos)
    kilpailu1.tunti_kuluu()