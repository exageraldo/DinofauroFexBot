from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from random import randint

from .libs.ipsum_gen import ipsum_generator
from .libs.translate import translate
from .libs.messages import MESSAGE
from .. import config

from .libs.decorators import echo_counter, command_counter

from .keyboards import language_keyboard, ipsum_keyboard


@command_counter("start")
def start(bot, update):
    """Send a message when the command /start is issued."""
    keyboard = language_keyboard('start')
    update.message.reply_text(
        MESSAGE['BR']['start'], reply_markup=keyboard)


@command_counter("help")
def help(bot, update):
    """Send a message when the command /help is issued."""
    keyboard = language_keyboard('help')
    update.message.reply_text(
        MESSAGE['BR']['help'], reply_markup=keyboard)


@command_counter("about")
def about(bot, update):
    """Send a message when the command /about is issued."""
    keyboard = language_keyboard('about')
    update.message.reply_text(
        MESSAGE['BR']['about'], reply_markup=keyboard)


@command_counter("ipsum")
def ipsum(bot, update):
    keyboard = ipsum_keyboard()
    update.message.reply_text(
        translate(ipsum_generator(randint(1, 6))), reply_markup=keyboard)


@echo_counter
def translation(bot, update):
    """Translate the user message to 'dinosaurese'."""
    one_f = translate(update.message.text)
    more_f = translate(update.message.text, remove=False)
    if one_f == more_f:
        update.message.reply_text(
            one_f, reply_to_message_id=update.message.message_id)
    else:
        message = f"1F:\n{one_f}\n\n+F:\n{more_f}"
        update.message.reply_text(
            message, reply_to_message_id=update.message.message_id)
