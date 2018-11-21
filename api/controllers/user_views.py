"""
This module provides responses to url requests.
"""
import re
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity
from flask import jsonify, request
from flask.views import MethodView
from api.models.database import DatabaseUtilities
from api.models.users import Users
from api.handler.error_handler import ErrorFeedback




class SignUp(MethodView):
    """
       Class contains method plus all signup performances
    """
    def post(self):
        """
           Method for creating new user
           params: json requests
           response: json data
        """
        new_user = Users()
        keys = ("user_name", "email", "password")
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)

        post_data = request.get_json()
        user_name =request.json['user_name']
        password = request.json['password']  
        
        try:
            user_name = post_data['user_name'].strip()
            password = post_data['password'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not user_name or not password:
            return ErrorFeedback.empty_data_fields()

        pattern = r"(^[a-zA-Z0-9-.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(pattern, request.json['email']):
            return jsonify({'message': 'Enter right format of email thanks',
                            'status':'Failure'}), 400

       
        user_details = new_user.register_a_user(request.json['user_name'], request.json['email'], request.json['password'])
        if user_details == "Email exists boss, Please use another email":
            return jsonify({'message': user_details,
                            'status':'success'}), 400

        return jsonify({'message': user_details}), 201
    

class Login(MethodView):
    """
       Class for logging in the user
    """
    def post(self):
        """
           Method for logging in  user
           params: json requests
           response: json data
        """
        login_user = Users()
        keys = ("email", "password")

        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)

        post_data = request.get_json()
        email =request.json['email']
        password = request.json['password']   
        try:
            email = post_data['email'].strip()
            password = post_data['password'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not email or not password:
            return ErrorFeedback.empty_data_fields()

        
        user_id = login_user.fetch_password(request.json['email'], request.json['password'])

        if user_id:
            return jsonify({
                "access_token" : create_access_token(identity=user_id),
                "message": "User logged in successfully",
                "status":"success"
            }), 200

        return jsonify({"message": "Wrong username or passwerd",
                        'status':'failure'}), 400



