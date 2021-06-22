# -*- coding: utf-8 -*-
"""
Bot for test something things.
"""
import telebot
from secret import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)
