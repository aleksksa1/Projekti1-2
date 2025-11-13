from flask import Flask, request
from classes.funktiot import Funktiot

f = Funktiot()

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    tulos = f.alkuluku(luku)
    vastaus = {
        "Number": luku,
        "isPrime": tulos}

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)