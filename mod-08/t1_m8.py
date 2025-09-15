import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         database='flight_game',
         user='aleksi',
         password='koivunoksa32',
         autocommit=True
         )

def haeLentokentta(koodi):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos

code = input('Syötä lentokentän ICAO-koodi: ')
kentta = haeLentokentta(code)

if kentta:
    print(f"Lentökentän nimi: {kentta['name']}")
    print(f"Lentokentän sijaintikunta: {kentta['municipality']}")
else:
    print("Lentokenttää ei löytynyt annetulla koodilla.")
