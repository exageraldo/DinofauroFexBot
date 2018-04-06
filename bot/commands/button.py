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

def thanks_feedback(bot, update, parameters):
    query = update.callback_query
    stars = parameters[0]
    bot.edit_message_text(text=f"Obrigado pelas {stars} feedback!",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)

KEYBOARD = {
    'language': change_language,
    'ipsum': random_ipsum,
    'feedback': thanks_feedback
}

def button(bot, update):
    query = update.callback_query
    function, *parameters = query.data.split("|")
    KEYBOARD[function](bot, update, parameters)
