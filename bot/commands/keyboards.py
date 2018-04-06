from random import randint
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def language_keyboard(language, message):
    if language == 'BR':
        return InlineKeyboardMarkup(
            [[InlineKeyboardButton(
                "🇺🇸", callback_data=f'language|EN|{message}')]]
        )
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("🇧🇷", callback_data=f'language|BR|{message}')]]
    )


def ipsum_keyboard():
    keyboard = [[InlineKeyboardButton('Lorem Ipfum', callback_data='ipsum')]]
    return InlineKeyboardMarkup(keyboard)
