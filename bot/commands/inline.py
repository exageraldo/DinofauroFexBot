from telegram import (InlineQueryResultArticle, InputTextMessageContent)
from uuid import uuid4

from .libs.translate import translate

from .libs.decorators import inline_counter


@inline_counter
def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    if query:
        one_f = translate(query, remove=True)
        more_f = translate(query, remove=False)
        results = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="1F",
                input_message_content=InputTextMessageContent(
                    one_f))]
        if one_f != more_f:
            results.append(
                InlineQueryResultArticle(
                    id=uuid4(),
                    title=f"+F",
                    input_message_content=InputTextMessageContent(
                        more_f))
            )

        update.inline_query.answer(results)
