"""
This module provides responses to url requests.
"""
import re
from flask import jsonify, request
from flask.views import MethodView
from api.models.database import Databaseconn
from api.models.users import Users
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity



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
            return jsonify({'New user': 'Your request has Empty feilds'}), 400

        if request.json['user_name'] == "":
            return jsonify({'user_name': 'enter user_name'}), 400
        if (' ' in request.json['user_name']) == True:
            return jsonify({'message': 'user_name should not contain any spaces'}), 400

        if request.json['email'] == "":
            return jsonify({'email': 'enter email'}), 400

        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'email should not contain any spaces'}), 400

        if request.json['password'] == "":
            return jsonify({'message': 'password should not contain any spaces'}), 400

        if (' ' in request.json['password']) == True:
            return jsonify({'Password': 'Password should not contain any spaces'}), 400

        if len(request.json['password']) < 8:
            return jsonify({'Password': 'Your password should be more than 8 digits'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter right format of email thanks'}), 400

       
        user_details = new_user.register_a_user(request.json['user_name'], request.json['email'], request.json['password'])
        if user_details == "email exits boss, use another email":
            return jsonify({'message': user_details}), 401

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
            return jsonify({'message': 'Your request has Empty feilds'}), 400

        if request.json["email"] == "":
            return jsonify({'message': 'Ennter email'}), 400

        if (' ' in request.json['email']) == True:
            return jsonify({'message': 'email should not contain any spaces'}), 400

        if request.json["password"] == "":
            return jsonify({'message': 'Enter password'}), 400

        
        user_id = login_user.fetch_password(request.json['email'], request.json['password'])

        if user_id:
            return jsonify({
                "access_token" : create_access_token(identity=user_id),
                "message": "User logged in successfully"
            }), 200

        return jsonify({"message": "Wrong username or passwerd"}), 400



