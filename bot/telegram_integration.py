from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

from .messages import MESSAGE
from . import config


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    keyboard = update_keyboard('start')
    update.message.reply_text(
        MESSAGE['BR']['start'], reply_markup=keyboard)


def help(bot, update):
    """Send a message when the command /help is issued."""
    keyboard = update_keyboard('help')
    update.message.reply_text(
        MESSAGE['BR']['help'], reply_markup=keyboard)


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def update_keyboard(message):
    lang_keyboard = [[InlineKeyboardButton("🇧🇷", callback_data=f'BR/{message}'),
                      InlineKeyboardButton("🇺🇸", callback_data=f'EN/{message}')]]
    reply_keyboard = InlineKeyboardMarkup(lang_keyboard)
    return reply_keyboard


def button(bot, update):
    query = update.callback_query
    language, message = query.data.split("/")
    bot.edit_message_text(text=MESSAGE[language][message],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=update_keyboard(message))

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def run_bot():
    """Start the bot."""

    updater = Updater(config['TELEGRAM_TOKEN'])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CallbackQueryHandler(button))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
