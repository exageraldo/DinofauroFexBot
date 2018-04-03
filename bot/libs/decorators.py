from .. import config
from .user import User
from datetime import datetime

user = User(**config.get("mongo", {}))

def decorator(function):
    def func_wrapper(*args, **kwds):
        print(f"Starts: {datetime.now()}")
        function(*args, **kwds)
        print(f"Ends: {datetime.now()}")
    return func_wrapper