
from flask import jsonify, make_response, url_for
from ..database import get_db




db = get_db()



def create_message():
    db.helloWorld.insert_one({"_id":"HELLOMESSAGE","message":"HELLO WOLRD"})

def get_message():
   return db.helloWorld.find_one({"_id":"HELLOMESSAGE"})

