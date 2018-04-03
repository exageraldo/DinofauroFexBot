from pymongo import MongoClient


class User(MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_db = self.user
        self.users_collection = self.user_db.users

    def inline_user(self, user_id):
        self.users_collection.update_one(
                {"_id": user_id}, {"$inc": 
                    {"usage.inline": 1, "usage.total": 1}}, upsert=True)

    def echo_user(self, user_id):
        self.users_collection.update_one(
                {"_id": user_id}, {"$inc": 
                    {"usage.echo": 1, "usage.total": 1}}, upsert=True)
