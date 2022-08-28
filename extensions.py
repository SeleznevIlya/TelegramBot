import requests
import json
from config import currency_list


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_prise(base, quote, amount):
        try:
            base_key = currency_list[base.lower()]
        except:
            raise APIException(f'Валюта не найдена')

        try:
            quote_key = currency_list[quote.lower()]
        except:
            raise APIException(f'Валюта не найдена')

        try:
            amount_key = float(amount)
        except:
            raise APIException(f'Неверный ввод количества конвертируемой валюты')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={quote_key}')
        resp = json.loads(r.content)
        prise = resp[quote_key] * amount_key
        prise = round(prise, 5)
        message = f'Стоимость {amount} {base} в {quote}: {prise}'
        return message
