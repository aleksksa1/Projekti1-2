from classes.auto import Auto


autot = []

auto1 = Auto('ABC-123', '142')
auto2 = Auto('ABC-572', '133')
auto3 = Auto('ABC-777', '112')

autot.append(auto1)
autot.append(auto2)
autot.append(auto3)

for auto in autot:
    print(f"""
    Rekisteritunnus: {auto.rekisteritunnus}
    huippunopeus: {auto.huippunopeus}
    Nopeus: {auto.nopeus}
    Matka: {auto.matka}
    """)
