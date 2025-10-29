import json
import requests

paikkakunta = input("Syötä paikkakunta, jonka säätilan haluat tietää: ")

limit = 1
API_key = "4f66c57a8df8a5d0924759bce7d6f6db"


vastaus = ""
json_vastaus = ""


try:
    vastaus = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={paikkakunta}&limit={limit}&appid={API_key}")
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")


lat = json_vastaus[0]["lat"]
lon = json_vastaus[0]["lon"]


weather = ""
json_vastaus2 = ""

try:
    weather = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&lang=fi&appid={API_key}")
    if vastaus.status_code==200:
        json_vastaus2 = weather.json()

        temp = json_vastaus2["list"][0]["main"]["temp"]
        kuvaus = json_vastaus2["list"][1]["weather"][0]["description"]

        print("------------------------------------------------")
        print(f"Säätilan kuvaus: {kuvaus}")
        print(f"Lämpötila: {temp}°C")

except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
