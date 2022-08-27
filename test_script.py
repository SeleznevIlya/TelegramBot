import requests
import json

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=USD')
value_ = json.loads(r.content)
print(value_['USD'])


