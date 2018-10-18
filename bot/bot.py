# -*- coding: UTF-8 -*-
import logging
import datetime
import os
from glob import glob
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

import settings
from utils import is_cat


"""Функция, которая соединяется с платформой Telegram, "тело" нашего бота"""
def main():
    updater = Updater(settings.TELEGRAM_API_KEY, request_kwargs=settings.PROXY)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("planet", planet))
    dispatcher.add_handler(CommandHandler("wordcount", wordcount))
    dispatcher.add_handler(CommandHandler('cat', send_cat_image))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(
        Filters.photo, check_user_photo, pass_user_data=True))


    updater.start_polling()
    updater.idle()


"""Send random cat image."""
def send_cat_image(bot, update):
    cat_files = glob('images/cat*')
    filename = choice(cat_files)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(filename, 'rb'))


"""Check that cat is on received photo."""
def check_user_photo(bot, update, user_data):
    update.message.reply_text('Обрататывается фото...')
    os.makedirs('downloads', exist_ok=True)
    photo_file = bot.getFile(update.message.photo[-1].file_id
    )
    filename = os.path.join('downloads', f'{photo_file.file_id}.jpg')
    photo_file.download(filename)
    update.message.reply_text('Файл сохранен.')
    if is_cat(filename):
        update.message.reply_text('Найдена кошатина! Добавляю в библиотеку.')
        os.makedirs('images', exist_ok=True)
        new_file_name = os.path.join(
            'images', f'cat_{photo_file.file_id}.jpg')
        os.rename(filename, new_file_name)
    else:
        update.message.reply_text('Это не кошка и не кот, 100 пудов!')
        os.remove(filename)


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
