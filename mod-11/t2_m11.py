import random
from classes.auto11 import Auto
from classes.auto11 import Sahkoauto
from classes.auto11 import Polttomoottoriauto

sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.nopeus = random.randint(50, 180)
bensa.nopeus = random.randint(50, 180)

sahkoauto.kulje(3)
bensa.kulje(3)

print(f"{sahkoauto.rekisteritunnus} mittarilukema: {sahkoauto.matka}")
print(f"{bensa.rekisteritunnus} mittarilukema: {bensa.matka}")