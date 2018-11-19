"""
    Module for making tests on the app for sign up
"""
import os
import json
import unittest
import psycopg2
from run import APP
from api.models.users import Users
from api.models.database import Databaseconn
from api.config import TestingConfig
from . import *
class TestViews(unittest.TestCase):
    """"
        Class for testing  signing up
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        APP.config.from_object('api.config.TestingConfig')
        self.client = APP.test_client
        with self.client() as client:
            create_test_tables = Databaseconn()
            create_test_tables.create_tables()
            self.post_token = post_auth_header(client)
            self.get_token = get_auth_header(client)

    def tearDown(self):
        """
           Method for deleting tables in the database object
        """
        with self.client():
            down_tables = Databaseconn()
            down_tables.delete_tables()

    def test_signup(self):
        """
            Method for testing the post function which adds new user
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(OTHER_USER)))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["message"])

    def test_sign_with_only_password(self):
        """
            Method for testing the post function for adding a new user with no username, and email
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(password="codeisgood")))
        
        self.assertEqual(result.status_code, 400)
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('New user', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["New user"])


    def test_sign_with_an_empty_user_name(self):
        """
            Method for testing the post function for testing user with empty user_name
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", email="a4agmail.com",
                                                         password="codeisgood")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('user_name', respond)        
        self.assertTrue(result.json["user_name"])
            

    def test_sign_with_other_criedientials(self):
        """
            Method for testing the post function for posting a user with other signup credientials
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name  = "mukasa", email = "akra@gmail.com.com", password = "akram256")))
        
        self.assertEqual(result.status_code, 201)
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)        
        self.assertTrue(result.json['message'])

    def test_sign_with_missing_email(self):
        """
            Method for testing the post function for missing email
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", email="",
                                                         password="codeisgood")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('email', respond)        
        self.assertTrue(result.json["email"])

    def test_sign_with_a_wrong_password_formart(self):
        """
            Method for testing the post function for posting a wrong password format
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", email="a4a@gamil.com",
                                                         password="a4a")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Password', respond)        
        self.assertTrue(result.json["Password"])


    def test_login(self):
        self.test_signup()
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(OTHER_USER)))
        self.assertEqual(result.status_code, 200)
        result = json.loads(result.data.decode())
        self.assertTrue(['post_token'])

    
    def test_login_with_a_username(self):
        """
            Method for testing the  logging method for a user with only a user_name
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", password="a4a20242")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_login_with_without_password(self):
        """
            Method for testing the post function which logins in a user with wrong password
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="a4a@gmail.com", password="meand")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn( "message", respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_login_without_email(self):
        """
            Method for testing the  login in a user without a user
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(email="", password="codeisgood")))
        self.assertEqual(result.status_code, 400)
       

    



            