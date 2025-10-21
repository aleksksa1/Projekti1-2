import random

from classes.auto import Auto

autot = []

for i in range(10):
    huippunopeus = random.randint(100, 200)
    autot.append(Auto("ABC-" + str(i + 1), huippunopeus))

kokonaismatka = 0

while kokonaismatka < 10000:
    for auto in autot:
        nopeusmuutos = random.randint(-10, 15)
        auto.kiihdyta(nopeusmuutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kokonaismatka = auto.matka

for auto in autot:
    print(auto.ominaisuudet())





       #arvo nopeuden muutos -10-15
        #kutsu kiihdytä
        #kutsu auto.kulje(1)
        # hae matkan arvo, jos 10000 lopeta kisa asetattamalla kokonaiasmtakasti

#googlaa taulukkokirjasto tulostamiseen
#ehkä metodi joka palauttaa ominaisuudet listana tai dictionary

