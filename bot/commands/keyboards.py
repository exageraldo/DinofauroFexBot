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


def feedback_keyboard(language):
    keyboard = [[InlineKeyboardButton('⭐️', callback_data='feedback|BR|1'),
                 InlineKeyboardButton('⭐️⭐️', callback_data='feedback|BR|2')],
                [InlineKeyboardButton('⭐️⭐️⭐️', callback_data='feedback|BR|3'),
                 InlineKeyboardButton('⭐️⭐️⭐️⭐️', callback_data='feedback|BR|4')],
                [InlineKeyboardButton('⭐️⭐️⭐️⭐️⭐️', callback_data='feedback|BR|5')]]
    if language == 'BR':
        keyboard.append([InlineKeyboardButton(
            "🇺🇸", callback_data=f'feedback|EN|0')])
    else:
        keyboard.append([InlineKeyboardButton(
            "🇧🇷", callback_data=f'feedback|BR|0')])
    return InlineKeyboardMarkup(keyboard)
