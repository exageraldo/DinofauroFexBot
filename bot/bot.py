from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, CallbackQueryHandler, InlineQueryHandler)

from . import config

from .commands.commands import (start, help, about, ipsum, translation)
from .commands.inline import inlinequery
from .commands.button import button
from .commands.error import error


def run_bot():
    """Start the bot."""

    updater = Updater(config['telegram']['token'])
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ipsum", ipsum))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_handler(InlineQueryHandler(inlinequery))

    dp.add_handler(MessageHandler(Filters.text, translation))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
