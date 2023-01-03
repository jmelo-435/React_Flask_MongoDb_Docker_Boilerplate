from flask import  jsonify
from .repo import create_message,get_message

def test():

    return jsonify({"msg":"Auth API connected.", "sucess": True, "code":200}), 200

def db_test():
    
        msg =get_message()
        return jsonify({"msg":"MongoDb connected.", "sucess": True, "code":200,"msg":msg}), 200


