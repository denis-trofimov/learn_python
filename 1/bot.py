# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging


# Настройки прокси
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
}


'''Функция, которая соединяется с платформой Telegram, "тело" нашего бота'''
def main():
    updater = Updater(open("api.token").readline(), request_kwargs=PROXY)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text,echo))
    
    updater.start_polling()
    updater.idle()

def start(bot, update):
    # print("update " + str(type(update.message)))
    user = update.message.from_user
    greeting = "Hello {0} {1}!".format(user.first_name, user.last_name)
    bot.send_message(chat_id=update.message.chat_id, text=greeting)

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


if __name__ == "__main__":
    # Enable logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.WARNING
    )
    
    # Вызываем функцию - эта строчка собственно запускает бота
    main()
