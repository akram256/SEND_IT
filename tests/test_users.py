"""
    Module for making tests on the app for sign up
"""
import os
import json
import unittest
import psycopg2
from api.models.users import Users
from api.models.database import DatabaseUtilities
from api.config import TestingConfig
from . import get_token,get_auth_header,post_auth_header,OTHER_USER
from .test_base import Testbase

class TestViews(Testbase):
    """"
        Class for testing  signing up
        params: unittest.testCase
    """

    def test_signup(self):
        """
            Method for testing the post function which adds new user
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(OTHER_USER)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["message"], 'Account successfully created,Please login')


    def test_sign_with_an_empty_data(self):
        """
            Method for testing the post function for testing user with empty user_name
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", email="a4agmail.com",
                                                         password="codeisgood")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('error_message', respond)        
        self.assertTrue(result.json["error_message"], 'Some fields have no data')
    
    def test_sign_with_wrong_name(self):
        """
            Method for testing the post function for testing user with empty user_name
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name=".......", email="a4agmail.com",
                                                         password="codeisgood")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)        
        self.assertTrue(result.json["message"], 'Wrong format of the user_name')

    def test_login(self):
        self.test_signup()
        result = self.client().post('/api/v2/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(OTHER_USER)))
        self.assertEqual(result.status_code, 200)
        result = json.loads(result.data.decode())
        self.assertTrue(['post_token'])

    def test_sign_wrong_email(self):
        """
                Method for testing the post function for missing email
            """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", email="sgsgsgs",
                                                         password="codeisgood")))

        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertTrue(['message'], 'Enter right format of email thanks')
       
    def test_login_missing_fields(self):
        """
            Method for testing the  logging method for a user with only a user_name
        """
        result = self.client().post('/api/v2/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", password="a4a20242")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('error_message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 404)
        self.assertTrue(result.json["error_message"], 'You have missing fields')

    def test_login_with_without_password(self):
        """
            Method for testing the post function which logins in a user with wrong password
        """
        result = self.client().post('/api/v2/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="a4a@gmail.com", password="mean1233")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn( "message", respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"], 'wrong username or password')
    
    def test_signup_with_short_password(self):
        """
            Method for testing the post function which logins in a user with wrong password format
        """
        result = self.client().post('/api/v2/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="a4a@gmail.com", user_name="akram",password="mean")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn( "message", respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"], 'Password should be more than 8 characters')
