import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         database='flight_game',
         user='aleksi',
         password='koivunoksa32',
         autocommit=True
         )

def lentokentta(koodi):
    sql = "SELECT type, count(*) FROM airport WHERE iso_country = %s GROUP BY type"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchall()
    return tulos

code = input("Syötä lentokentän maakoodi: ")
kentta = lentokentta(code)

print(f"Kenttien määrät: ")
for rivi in kentta:
    print(f"Tyyppi: {rivi['type']}, lukumäärä: {rivi['count(*)']}")