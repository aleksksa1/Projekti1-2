import requests
import json

vitsi = "value"

try:
    vastaus = requests.get("https://api.chucknorris.io/jokes/random")
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        print(json_vastaus[vitsi])
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")