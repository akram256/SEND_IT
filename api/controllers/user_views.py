"""
   Module for defining views
"""

from flask import jsonify, request
from flask.views import MethodView
from api.handler.error_handler import ErrorFeedback
from api.auth.user import Users
import re
# from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity


user_now = Users()
class AuthUser(MethodView):
    """
       class for defining views

    """
   
    def post(self):
        
        """
           method to post all requests
        """
      
        keys = ("user_name" ,"name", "password")
        
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)
            
      
        post_data = request.get_json()
        user_name =request.json['user_name']
        name = request.json['name']
        password = request.json['password']
        id = 'id'   
        
        try:
            user_name = post_data['user_name'].strip()
            name = post_data['name'].strip()
            password = post_data['password'].strip()
            id = 'id'
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not user_name or not password:
            return ErrorFeedback.empty_data_fields()

        user_now.add_user(user_name,name,password,id)

        response_object =  user_now.__dict__
        
        return jsonify(response_object), 201

    def get(self):

        if user_now.get_all_users() is True:
            return jsonify({'Users':'No users'})
        return jsonify({'users':user_now.get_all_users()}), 200

class Login(MethodView):
    

    def post(self):
        
       
        post_data = request.get_json()

        keys = ("user_name", "password")
        if not set(keys).issubset(set(request.json)):
            return jsonify({'blank': 'Your request has Empty feilds'}), 400

        try:
            user_name = post_data['user_name'].strip()
            password = post_data['password'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not user_name and password:
            return ErrorFeedback.empty_data_fields()
        

        userid = user_now.login_user(request.json['user_name'], request.json['password'])
        if userid:
            return jsonify({
                # "access_token" : create_access_token(identity = userid),
                "message": "User logged in successfully"
            }), 200

        return jsonify({"message": "Wrong username or passwerd"}), 400
