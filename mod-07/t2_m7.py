nimi = input("Anna nimi tai lopeta: (Enter): ")

nimet = set(())

while nimi != "":

    if nimi in nimet:
        print("Aiemmin syötetty nimi")

    else: print("Uusi nimi")

    nimet.add(nimi)

    nimi = input("Anna nimi tai lopeta: (Enter): ")

print("Annetut nimet satunnaisessa järjestyksessä (sama nimi vain kerran):")
for nimi in nimet:
    print(nimi)