syote = input("Haluatko syöttää uuden lentoaseman(uusi), "
              "hakea jo syötetyn lentoaseman tiedot(hae) "
              "vai lopettaa(lopeta)?: ")

lentokentat = {"EFHK": "Helsinki-Vantaa",
               "EFJK": "Jyväskylä",
               "EFTU": "Turku"}

while syote != "lopeta":
    if syote == "uusi":
        uusi_icao = input("Syötä lentokentän ICAO-koodi: ")
        uusi_nimi = input("Syötä lentokentän nimi: ")
        lentokentat[uusi_icao] = uusi_nimi

        syote = input("Haluatko syöttää uuden lentoaseman(uusi), "
                      "hakea jo syötetyn lentoaseman tiedot(hae) "
                      "vai lopettaa(lopeta)?: ")

    elif syote == "hae":
        icao = input("Syötä lentokentän ICAO-koodi: ")
        print(lentokentat[icao])

        syote = input("Haluatko syöttää uuden lentoaseman(uusi), "
                      "hakea jo syötetyn lentoaseman tiedot(hae) "
                      "vai lopettaa(lopeta)?: ")

else: print("Kiitos käytöstä!")
