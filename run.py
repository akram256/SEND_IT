"""
This module runs the application
"""

"""
This is the main module
"""
from flask import Flask
from api.routes.urls import Urls
from api.models.database import Databaseconn
from flask_jwt_extended import JWTManager



APP = Flask(__name__)
APP.config.from_object('api.config.DevelopmentConfig')

APP.config['JWT_SECRET_KEY'] = 'codeislove' 
jwt = JWTManager(APP)

@APP.before_first_request
def create_tables():
    table_handler=Databaseconn()
    table_handler.create_tables()
    # user = Users()
    # user.set_admin(1)

Urls.generate_url(APP)
if __name__ == '__main__':
    
    APP.run()