from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from random import randint

from .libs.ipsum_gen import ipsum_generator
from .libs.translate import translate
from .libs.messages import MESSAGE

def language_keyboard(message):
    keyboard = [[InlineKeyboardButton("🇧🇷", callback_data=f'BR/{message}'),
                 InlineKeyboardButton("🇺🇸", callback_data=f'EN/{message}')]]
    return InlineKeyboardMarkup(keyboard)


def ipsum_keyboard():
    keyboard = [[InlineKeyboardButton('Lorem Ipfum', callback_data='ipsum')]]
    return InlineKeyboardMarkup(keyboard)


def button(bot, update):
    query = update.callback_query
    if query.data == 'ipsum':
        bot.edit_message_text(text=translate(ipsum_generator(randint(1, 6))),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=ipsum_keyboard())
    else:
        language, message = query.data.split("/")
        bot.edit_message_text(text=MESSAGE[language][message],
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              reply_markup=language_keyboard(message))