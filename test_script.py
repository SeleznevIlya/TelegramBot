import requests
import json

r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=RUB&tsyms=USD')
value_ = json.loads(r.content)
#print(value_)

currency_list = {'доллар': 'USD',
                 'евро': 'EUR',
                 'рубль': 'RUB'}

value_text = 'Доступные валюты:'
for key in currency_list.keys():
    value_text = '\n'.join((value_text, key))
print(value_text)