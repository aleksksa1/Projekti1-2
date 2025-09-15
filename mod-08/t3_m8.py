import mysql.connector
from geopy.distance import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         database='flight_game',
         user='aleksi',
         password='koivunoksa32',
         autocommit=True
         )

from geopy import distance

def hae_koordinaatit(koodi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()

    if tulos:
        return (tulos["latitude_deg"], tulos["longitude_deg"])
    else:
        return None

code1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
koord1 = hae_koordinaatit(code1)

code2 = input("Syötä toisen lentokentän ICAO-koodi: ")
koord2 = hae_koordinaatit(code2)

if koord1 and koord2:
    valimatka = distance.distance(koord1, koord2).kilometers
    print(f"Etäisyys: {valimatka:.0f} km")
else:
    print("Toisen tai molempien kenttien koordinaatteja ei löytynyt.")
