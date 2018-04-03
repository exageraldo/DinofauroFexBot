from .. import config
from .user import User
from datetime import datetime

user = User(**config.get("mongo", {}))

def inline_counter(function):
    def func_wrapper(bot, update):
        function(bot, update)
        user.inline_user(update.message.from_user.id)
    return func_wrapper


def echo_counter(function):
    def func_wrapper(bot, update):
        function(bot, update)
        user.echo_user(update.message.from_user.id)
    return func_wrapper
