from pymongo import MongoClient
import certifi

from database.entities import Message


class Operations:
    def connect(self):
        return MongoClient("mongodb+srv://root:123456qwerty@samples.gvdyi.mongodb.net/?retryWrites=true&w=majority"
                           "&appName=SAMPLES", tlsCAFile=certifi.where())

    def authenticate(self, email: str, password: str):
        client = self.connect()
        db = client["chatpy"]
        user = db["users"].find_one({"email": email, "password": password})
        if user:
            return user
        else:
            return False


    def add_new_message(self, message: Message):
        cli = self.connect()
        db = cli["chatpy"]
        coll = db.messages
        return coll.insert_one(message.__dict__).inserted_id