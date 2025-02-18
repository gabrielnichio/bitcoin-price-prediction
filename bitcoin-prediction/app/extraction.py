import requests
import json

limit = 2000

url_historical = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit={limit}'
url_fear = f"https://api.alternative.me/fng/?limit={limit}"


historical = requests.get(url_historical).json()

fear = requests.get(url_fear).json()

with open("../data/processed/historical.json", "w") as outfile:
    json.dump(historical['Data']['Data'], outfile)

with open("../data/processed/fear.json", "w") as outfile:
    json.dump(fear['data'], outfile)