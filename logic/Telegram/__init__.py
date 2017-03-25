import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from Database.data_handler import UserAdder, NewsLoader

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

user_adder = UserAdder()
news_loader = NewsLoader()


def read(bot, update):
    keyboard = [[InlineKeyboardButton("5 новостей", callback_data='read5'),
                 InlineKeyboardButton("10 новостей", callback_data='read10')],

                [InlineKeyboardButton("15 новостей", callback_data='read15')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Сколько последних непрочитанных новостей вы хотите прочитать?',
                              reply_markup=reply_markup)


def start(bot, update):
    user_adder.add_user(update.message.chat_id)
    bot.sendMessage(chat_id=update.message.chat_id, text='Привет! Используйте /read, чтобы читать новости.')


def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id
    if query.data.count('read') == 1:
        send_news_headers(bot, update, news_loader.unread_news(
            chat_id, int(query.data[4:])), chat_id)
    elif query.data.count('full') == 1:
        send_news_text(bot, update, query.data[4:], chat_id)


def send_news_headers(bot, update, news, chat_id):
    for news_id, date, header in news:
        user_adder.add_read_entry(news_id, chat_id)
        text = '\n'.join((date, header, ))

        keyboard = [[InlineKeyboardButton("Читать полностью", callback_data='full' + str(news_id))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=chat_id, text=text, reply_markup=reply_markup)


def send_news_text(bot, update, news_id, chat_id):
    query = update.callback_query
    bot.editMessageText(chat_id=chat_id,
                        text=news_loader.get_news_full_text(news_id),
                        message_id=query.message.message_id)


def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("335128365:AAGj-kw7xdSqD5zcVnhRiXnuUGBNpJB4F0g")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('read', read))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_error_handler(error)

def run():
    updater.start_polling()
    updater.idle()