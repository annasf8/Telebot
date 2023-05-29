import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            quote_key = exchanges[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")

        if base_key == quote_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote_key}&from={base_key}&amount={amount}"
        headers = {
            "apikey": "vSo1zpWZTaZGgGxFYFyGTWbMZp0AZQHk"
        }
        response = requests.request("GET", url, headers=headers)
        result = response.text
        print(result)
        s_price = json.loads(result)
        new_price = round(s_price.get('result'), 3)
        message = f"Цена {amount} {base} в {quote} : {new_price}"
        return message

