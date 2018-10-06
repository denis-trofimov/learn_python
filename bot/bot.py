#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import logging
import datetime


# Настройки прокси
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
}


"""Функция, которая соединяется с платформой Telegram, "тело" нашего бота"""
def main():
    updater = Updater(open("api.token").readline(), request_kwargs=PROXY)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("planet", planet))
    dispatcher.add_handler(CommandHandler("wordcount", wordcount))
    dispatcher.add_handler(MessageHandler(Filters.text,echo))
    
    updater.start_polling()
    updater.idle()


def start(bot, update):
    # print("update " + str(type(update.message)))
    user = update.message.from_user
    text = "Hello {0} {1}!".format(user.first_name, user.last_name)
    bot.send_message(chat_id=update.message.chat_id, text=text)


"""Reply echo message."""
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


"""Reply given planet constellation position now."""
def planet(bot, update):
    words = update.message.text.split()
    text = 'No such planet name!' 
    if len(words) > 1:
        words[1] = words[1].lower().capitalize()
        try:
            planet_object = getattr(ephem, words[1])
        except AttributeError:
            bot.send_message(chat_id=update.message.chat_id, text=text)
            return
        planet_position = planet_object(datetime.datetime.now())
        text = "The planet is now in the {0} constellation.".format(
            str(ephem.constellation(planet_position))
            )
    bot.send_message(chat_id=update.message.chat_id, text=text)


"""Count total words in double quotes."""
def wordcount(bot, update):
    text = update.message.text
    
    responce = "Insert text in double quotes, please."
    opening_quote_index = text.find('"')
    closing_quote_index = text.find('"', opening_quote_index + 1)
    
    if opening_quote_index > 0 and opening_quote_index < closing_quote_index:
        quoted_text = text[opening_quote_index + 1:closing_quote_index]
        word_list = quoted_text.split()
        responce = "I count total {0} words.".format(len(word_list))

    bot.send_message(chat_id=update.message.chat_id, text=responce)


if __name__ == "__main__":
    # Enable logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.WARNING
    )
    
    # Вызываем функцию - эта строчка собственно запускает бота
    main()
