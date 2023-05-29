import telebot
import requests
import json
import traceback

# class APIException(Exception):
#     pass
TOKEN = '6013959713:AAEbC-K7Z_-_BkGi9oK2OmIqoOqTEb6Z850'

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}
amount = 100
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = "Чтобы узнать актуальный курс валюты введите боту команду в следуюшем формате: \n <название валюты, цену которой хотите узнать> \ <в какую валюту хотите перевести> \
<количество конвертируемой валюты> \n Список доступных валют по команде: /values"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Список доступных валют:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    # r = requests.get(f"https://api.exchangeratesapi.io/v1/latest?access_key=9292cedcd59123b318a0d3f283882ac5&base={keys[quote]}&symbols={keys[base]}")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={keys[quote]}&from={keys[base]}&amount={amount}"
    payload = {}
    headers = {
    "apikey": "vSo1zpWZTaZGgGxFYFyGTWbMZp0AZQHk"
}
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.text
    s_price = json.loads(result)
    new_price = s_price.get('result')
    text = f"Цена {amount} {quote} в {base} : {new_price}"
    # print(result)
#     total_base = json.loads(r.content)[keys[base]]
#     text = f"Цена {amount} {quote} в {base} - {total_base}"
    bot.send_message(message.chat.id, text)
bot.polling()
# class Convertor:
#     @staticmethod
#     def get_price(base, quote, amount):
#         try:
#             base_key = keys[base.lower()]
#         except KeyError:
#             raise APIException(f"Валюта {base} не найдена!")
#
#         try:
#             quote_key = keys[quote.lower()]
#         except KeyError:
#             raise APIException(f"Валюта {quote} не найдена!")
#
#         if base_key == quote_key:
#             raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
#
#         try:
#             amount = float(amount)
#         except ValueError:
#             raise APIException(f'Не удалось обработать количество {amount}!')
        # r = requests.get(f"http://data.fixer.io/api/://data.fixer.io/api/latest?access_key=\
        #  05a9468c8e9b7e1a8f2461e9ad442ee8? access_key = 05a9468c8e9b7e1a8f2461e9ad442ee8 \
        #  & base = {base_key}& base = {base_key}& symbols = {quote_key}& symbols = {quote_key}")
        # r = requests.get(f"http://data.fixer.io/api/convert?access_key=05a9468c8e9b7e1a8f2461e9ad442ee8&from={base_key}&to={quote_key}")
        # resp = json.loads(r.content)
        # new_price = resp['rates'][quote_key] * amount
        # new_price = round(new_price, 3)
        # message = f"Цена {amount} {base} в {quote} : {new_price}"
        # return message



        # try:
        #     if len(values) != 3:
        #         raise APIException('Неверное количество параметров!')
        #     answer = Convertor.get_price(*values)
        # except APIException as e:
        #     bot.reply_to(message, f"Ошибка в команде:\n{e}")
        # except Exception as e:
        #     traceback.print_tb(e.__traceback__)
        #     bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
        # else:
        #     bot.reply_to(message, answer)



bot.polling()