import requests
import telebot
import json
from config import token

currency_list = {'доллар': 'USD',
                 'евро': 'EUR',
                 'рубль': 'RUB'}


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    mess_start_help = 'Для того чтобы узнать текущий курс валюты введите следующее сообщение:' \
                      '<имя валюты, цену которой он хочет узнать> ' \
                      '<имя валюты, в которой надо узнать цену первой валюты> ' \
                      '<количество первой валюты>' \
                      ''
    bot.send_message(message.chat.id, mess_start_help)

@bot.message_handler(commands=['value'])
def value_message(message):
    mess_value = 'Доступные валюты: \nДоллар, \nЕвро, \nРубль'
    bot.send_message(message.chat.id, mess_value)


@bot.message_handler(content_types='text')
def converter(message):
    first_val, second_val, count = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={currency_list[first_val]}&tsyms={currency_list[second_val]}')
    pars_value = json.loads(r.content)
    bot.send_message(message.chat.id, f"{pars_value[currency_list[second_val]]*float(count)}")
    '''if first_val and second_val in list_values:
            if val[0] == list_values[0]:
                bot.send_message(message.chat.id, 'Ахуеть папаша')
                r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=RUB')
                value_ = json.loads(r.content)
                bot.send_message(message.chat.id, f"{value_['RUB']*int(message.text.split()[-1])}")
            if val[0] == list_values[1]:
                bot.send_message(message.chat.id, 'Ахуеть папаша')
                r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=RUB')
                value_ = json.loads(r.content)
                bot.send_message(message.chat.id, f"{value_['RUB']*int(message.text.split()[-1])}")
            if val[0] == list_values[2]:
                bot.send_message(message.chat.id, 'Ахуеть папаша')
                r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=USD&tsyms=RUB')
                value_ = json.loads(r.content)
                bot.send_message(message.chat.id, f"{value_['RUB']*int(message.text.split()[-1])}")
    else:
        bot.send_message(message.chat.id, "Введите корректные данные")'''
    if message.text == "Кнопка":
        bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")







bot.infinity_polling()

