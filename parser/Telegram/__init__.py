import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from Database.data_handler import UserAdder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

user_adder = UserAdder()


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

    bot.editMessageText(text="Selected option: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)



def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))


# Create the Updater and pass it your bot's token.
updater = Updater("335128365:AAGj-kw7xdSqD5zcVnhRiXnuUGBNpJB4F0g")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('read', read))
updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.dispatcher.add_error_handler(error)

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()