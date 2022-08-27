import telebot
from telebot_main import bot


class APIException(Exception):
    def attention(self):
        @bot.message_handler(content_types='text')
        def message_reply(message):
            if message.text == "Кнопка":
                bot.send_message(message.chat.id, "https://habr.com/ru/users/lubaznatel/")
