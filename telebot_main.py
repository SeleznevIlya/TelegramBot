import requests
import telebot
import json
from config import token

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
    mess_value = 'Доллары, евросики, рубели'
    bot.send_message(message.chat.id, mess_value)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Кнопка":
        bot.send_message(message.chat.id,"https://habr.com/ru/users/lubaznatel/")






bot.infinity_polling()

