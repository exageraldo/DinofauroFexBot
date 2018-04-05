import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    if error.message == "Message is not modified":
        bot.answer_callback_query(
            update.callback_query.id, text="Couldn't load messages")
    else:
        logger.warning('Update "%s" caused error "%s"', update, error)
