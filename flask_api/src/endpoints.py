from flask import  jsonify
from .repo import create_message,get_message

def test():

    return jsonify({"msg":"Auth API connected.", "sucess": True, "code":200}), 200

def db_test():
    try:
        create_message()
        msg =get_message()[0]
        return jsonify({"msg":"MongoDb connected.", "sucess": True, "code":200,"msg":msg}), 200
    except:
        return jsonify({"msg":"MongoDb not connected.", "sucess": False,}), 500


