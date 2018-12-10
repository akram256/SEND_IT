"""
This module runs the application
"""
"""
This is the main module
"""     
from flask import Flask
from flask_jwt_extended import JWTManager
import flasgger
from flask_cors import CORS
from api.routes.urls import Urls
from api.models.users import Users
from api.models.database import DatabaseUtilities

APP = Flask(__name__)
CORS(APP)
APP.config.from_object('api.config.DevelopmentConfig')

flasgger.Swagger(APP)
APP.config['JWT_SECRET_KEY'] = 'code@256#love'
jwt = JWTManager(APP)

@APP.before_first_request
def create_tables():
    admin_user = Users()
    table_handler = DatabaseUtilities()
    table_handler.create_tables()
    admin_user.add_admin()

Urls.generate_url(APP)
if __name__ == '__main__': 
    APP.run()
    