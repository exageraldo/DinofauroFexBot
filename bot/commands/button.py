from random import randint

from .libs.ipsum_gen import ipsum_generator
from .libs.translate import translate
from .libs.messages import MESSAGE
from .keyboards import ipsum_keyboard, language_keyboard, feedback_keyboard


def random_ipsum(bot, update, parameters):
    query = update.callback_query
    rand_int = int(parameters[0])
    bot.edit_message_text(text=translate(ipsum_generator(rand_int)),
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=ipsum_keyboard())


def change_language(bot, update, parameters):
    query = update.callback_query
    language, message = parameters
    bot.edit_message_text(text=MESSAGE[language][message],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          reply_markup=language_keyboard(language, message))


def feedback(bot, update, parameters):
    stars = int(parameters[1])
    if not stars:
        feedback_language(bot, update, parameters)
    else:
        thanks_feedback(bot, update, parameters)


def feedback_language(bot, update, parameters):
    query = update.callback_query
    language, stars = parameters
    bot.edit_message_text(text=MESSAGE[language]['feedback'],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id, 
                          reply_markup=feedback_keyboard(language))


def thanks_feedback(bot, update, parameters):
    query = update.callback_query
    language, stars = parameters
    bot.edit_message_text(text=MESSAGE[language]['thanks_feedback'],
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id, 
                          reply_markup=language_keyboard(language, 'thanks_feedback'))

KEYBOARD = {
    'language': change_language,
    'ipsum': random_ipsum,
    'feedback': feedback
}

def button(bot, update):
    query = update.callback_query
    function, *parameters = query.data.split("|")
    KEYBOARD[function](bot, update, parameters)
