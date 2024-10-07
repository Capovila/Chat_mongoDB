from pymongo import MongoClient
from pymongo.database import Database
import certifi

from database.entities import Message


class Operations:
    def connect(self):
        return MongoClient("mongodb+srv://root:123456qwerty@samples.gvdyi.mongodb.net/?retryWrites=true&w=majority"
                           "&appName=SAMPLES", tlsCAFile=certifi.where())
    
    def get_db(self) -> Database:
        client = self.connect()
        return client["chatpy"]

    def authenticate(self, email: str, password: str):
        user = self.get_db()["users"].find_one({"email": email, "password": password})
        if user:
            return user
        return False
        
    def verify_email(self, email:str):
        user = self.get_db()["users"].find_one({"email": email})
        if user:
            return user
        return False

    def send_new_message(self, message: Message):
        coll = self.get_db()["messages"]
        return coll.insert_one(message.__dict__).inserted_id