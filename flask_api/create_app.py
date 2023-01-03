from flask import Flask
from .src.endpoints import test,db_test


def create_app():
    application = Flask(__name__)
    application.debug = True
    
    application.add_url_rule('/api', 'test', test, methods=['OPTIONS','GET'])
    application.add_url_rule('/api/db_test', 'test', db_test, methods=['OPTIONS','GET'])


    
    
    
    return application