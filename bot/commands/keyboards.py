from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def language_keyboard(message):
    keyboard = [[InlineKeyboardButton("🇧🇷", callback_data=f'BR/{message}'),
                 InlineKeyboardButton("🇺🇸", callback_data=f'EN/{message}')]]
    return InlineKeyboardMarkup(keyboard)


def ipsum_keyboard():
    keyboard = [[InlineKeyboardButton('Lorem Ipfum', callback_data='ipsum')]]
    return InlineKeyboardMarkup(keyboard)
