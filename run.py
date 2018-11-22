"""
This module runs the application
"""

"""
This is the main module
"""
from flask import Flask
from flask_jwt_extended import JWTManager
import flasgger
from api.routes.urls import Urls
from api.models.users import Users
from api.models.database import DatabaseUtilities




APP = Flask(__name__)
APP.config.from_object('api.config.DevelopmentConfig')
flasgger.Swagger(APP)
APP.config['JWT_SECRET_KEY'] = 'code@256#love'
jwt = JWTManager(APP)

@APP.before_first_request
def create_tables():
    admin_user=Users()
    table_handler=DatabaseUtilities()
    table_handler.create_tables()
    admin_user.add_admin()
    # user = Users()
    # user.set_admin(1)

Urls.generate_url(APP)
if __name__ == '__main__':
    
    APP.run()