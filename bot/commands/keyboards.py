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
    keyboard = [[InlineKeyboardButton(
        'Lorem Ipfum', callback_data=f'ipsum|{randint(1, 6)}')]]
    return InlineKeyboardMarkup(keyboard)


def feedback_keyboard():
    keyboard = [[InlineKeyboardButton('⭐️', callback_data='feedback|1'),
                 InlineKeyboardButton('⭐️⭐️', callback_data='feedback|2')],
                [InlineKeyboardButton('⭐️⭐️⭐️', callback_data='feedback|3'),
                 InlineKeyboardButton('⭐️⭐️⭐️⭐️', callback_data='feedback|4')],
                [InlineKeyboardButton('⭐️⭐️⭐️⭐️⭐️', callback_data='feedback|5')]]
    return InlineKeyboardMarkup(keyboard)
