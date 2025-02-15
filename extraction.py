import requests
import json

url_historical = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000'
url_fear = "https://api.alternative.me/fng/?limit=2000"


historical = requests.get(url_historical).json()

fear = requests.get(url_fear).json()

with open("historical.json", "w") as outfile:
    json.dump(historical['Data']['Data'], outfile)

with open("fear.json", "w") as outfile:
    json.dump(fear['data'], outfile)