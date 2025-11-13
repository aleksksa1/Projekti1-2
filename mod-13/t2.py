from flask import Flask, request
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         database='flight_game',
         user='aleksi',
         password='koivunoksa32',
         autocommit=True
         )

def haeLentokentta(koodi):
    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    return tulos

app = Flask(__name__)

@app.route('/airport/<ICAO>')
def airport(ICAO):
    tulos = haeLentokentta(ICAO)
    vastaus = {
        "ICAO": tulos['ident'],
        "Name": tulos['name'],
        "Municipality": tulos['municipality']}

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)