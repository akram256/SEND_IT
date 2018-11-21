"""
    Module for making tests on the app for sign up
"""
import os
import json
import unittest
import psycopg2
from run import APP
from api.models.users import Users
from api.models.database import DatabaseUtilities
from api.config import TestingConfig
from . import get_token,get_auth_header,post_auth_header,OTHER_USER


class TestViews(unittest.TestCase):
    """"
        Class for testing  signing up
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
       
        self.client = APP.test_client
        with self.client() as client:
            create_test_tables = DatabaseUtilities()
            create_test_tables.create_tables()
            self.post_token = post_auth_header(client)
            self.get_token = get_auth_header(client)

    def tearDown(self):
        """
           Method for deleting tables in the database object
        """
        with self.client():
            drop_tables = DatabaseUtilities()
            drop_tables.delete_tables()

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
        self.assertTrue(result.json["message"],'Account successfully created,Please login')


    def test_sign_with_an_empty_data(self):
        """
            Method for testing the post function for testing user with empty user_name
        """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="", email="a4agmail.com",
                                                         password="codeisgood")))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('error_message', respond)        
        self.assertTrue(result.json["error_message"],'Some fields have no data')

    def test_login(self):
        self.test_signup()
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(OTHER_USER)))
        self.assertEqual(result.status_code, 200)
        result = json.loads(result.data.decode())
        self.assertTrue(['post_token'])

    def test_sign_wrong_email(self):
        """
                Method for testing the post function for missing email
            """
        result = self.client().post('/api/v1/auth/signup',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", email="sgsgsgs",
                                                         password="codeisgood")))

        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertTrue(['message'],'Enter right format of email thanks')
       
        
    
    def test_login_missing_fields(self):
        """
            Method for testing the  logging method for a user with only a user_name
        """
        result = self.client().post('/api/v1/auth/login',
                                    content_type="application/json",
                                    data=json.dumps(dict(user_name="a4a", password="a4a20242")))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('error_message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["error_message"], 'You have missing fields')

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
        self.assertTrue(result.json["message"],'wrong username or password')


  
       