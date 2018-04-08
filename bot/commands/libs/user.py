from pymongo import MongoClient
import time
from datetime import datetime

class User(MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_db = self.dinofauro_bot
        self.users_collection = self.user_db.users

    def inline_user(self, user_id):
        self.users_collection.update_one(
            {"_id": user_id}, {"$inc": 
                {"usage.inline": 1, "usage.total": 1}}, upsert=True)

    def echo_user(self, user_id):
        self.users_collection.update_one(
            {"_id": user_id}, {"$inc": 
                {"usage.echo": 1, "usage.total": 1}}, upsert=True)

    def command_user(self, user_id, command):
        self.users_collection.update_one(
            {"_id": user_id}, {"$inc":
                {f"commands.{command}": 1, "commands.total": 1}}, upsert=True)

    def find_feedback(self, user_id):
        current_date = time.strftime('%m')
        find_fb = self.users_collection.find_one(
            {"_id": user_id}, {"feedback": 1, "_id": 0})
        if find_fb and find_fb['feedback'].get(current_date):
            return True
        return False

    def feedback_user(self, user_id, stars):
        current_date = time.strftime('%m')
        self.users_collection.update_one(
            {"_id": user_id}, 
            {"$set": 
                {f"feedback.{current_date}": {"stars": int(stars), "date": datetime.now()}}}, upsert=True)
