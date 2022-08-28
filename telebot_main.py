import telebot
from config import *
from extensions import *


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Приветствую в конвертере валют'
                                      'перед началом использования обратитесь к инструкции /help')


@bot.message_handler(commands=['help'])
def start_message(message):
    message_start_help = 'Для того чтобы узнать текущий курс валюты введите следующее сообщение:' \
                      '<имя валюты, цену которой он хочет узнать>, ' \
                      '<имя валюты, в которой надо узнать цену первой валюты>, ' \
                      '<количество первой валюты>.' \
                      'Чтобы узнать список доступных валют, введите /value'
    bot.send_message(message.chat.id, message_start_help)


@bot.message_handler(commands=['value'])
def value_message(message):
    value_text = 'Доступные валюты:'
    for key in currency_list.keys():
        value_text = '\n'.join((value_text, key))
    bot.reply_to(message, value_text)


@bot.message_handler(content_types='text')
def converter(message):
    values = message.text.split(' ')
    try:
        if len(values) != 3:
            raise APIException('Неверное кол-во параметров')

        result = Converter.get_prise(*values)

    except APIException as e:
        bot.reply_to(message, f'Ошибка: \n{e}')

    else:
        bot.reply_to(message, result)


bot.infinity_polling()
