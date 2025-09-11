vuodenajat = ("talvi", "kevät", "kesä", "syksy")

numero = int(input("Syötä kuukauden numero: "))

if numero < 1 or numero > 12:
    print("Virheellinen numero")

elif 1 <= numero < 3 or numero == 12:
    print(f"Kuukausi on vuodenaikana {vuodenajat[0]}")

elif numero < 6:
    print(f"Kuukausi on vuodenaikana {vuodenajat[1]}")

elif numero < 9:
    print(f"Kuukausi on vuodenaikana {vuodenajat[2]}")

elif numero < 12:
    print(f"Kuukausi on vuodenaikana {vuodenajat[3]}")