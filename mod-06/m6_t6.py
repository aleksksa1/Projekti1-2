import math

def vastine(hal_cm, hinta_e):
    halkaisija_m = hal_cm / 100
    sade = halkaisija_m / 2
    pinta_ala = math.pi * sade ** 2
    return hinta_e / pinta_ala

print("Syötä ensimmäisen pizzan tiedot:")
hal1 = float(input("Halkaisija (cm): "))
hinta1 = float(input("Hinta (€): "))

print("Syötä toisen pizzan tiedot:")
hal2 = float(input("Halkaisija (cm): "))
hinta2 = float(input("Hinta (€): "))

eka = vastine(hal1, hinta1)
toka = vastine(hal2, hinta2)

if eka < toka:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif toka < eka:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Pizzat ovat samanhintaisia.")