"""
    Module for making tests on the app for sign in
"""
import unittest
import json
import psycopg2
import os
from run import APP
from api.models.database import DatabaseUtilities
from api.models.users import Users
from api.models.parcels import Parcel
from . import get_token,get_auth_header,post_auth_header,OTHER_USER,ORDER,EMPTY_PARCEL_STATUS,PARCEL_STATUS,CURRENTLOCATION_UPDATE,DESTINATION_UPDATE

class TestViews(unittest.TestCase):
    """"
        Class for making tests on sign in
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

    def test_post_with_an_empty_without_a_token(self):
        """
            Method for testing the post function for checking a token
        """
        result = self.client().post('/api/v2/parcels',
                                    content_type="application/json",
                                    data=json.dumps(ORDER))        
        
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('msg', respond)        
        self.assertTrue(result.json["msg"],'Missing Authorization order')

    def test_place_an__order(self):
        """
            Method for testing to place an order
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        print(str(respond))
        self.assertEqual(result.status_code, 201)
        self.assertIn('message' ,respond)
        self.assertIsInstance(respond, dict)
        self.assertTrue(result.json["message"], 'Order has been Placed successfully')
    
    def test_fetch_no_parcels(self):
        """
           Method for testing get all no parcel orders 
        """
        result = self.client().get('/api/v2/parcels',headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        print(str(respond))
        self.assertEqual(result.status_code, 404)
        self.assertIn('Orders', respond)
        self.assertIsInstance(respond, dict)
        self.assertTrue(result.json["Orders"], 'No parcel_orders available at the moment, PLease make an order')

    def test_fetch_all_parcels(self):
        """
           Method for testing get all orders 
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().get('/api/v2/parcels',headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Orders', respond)
        self.assertIsInstance(respond, dict)
    
    def test_getting_one_parcel(self):
        """
            This method tests for getting one parcel 
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().get('/api/v2/parcels/1',headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertTrue(result.json["status"],'Success' )    


    def test_updating_order_status(self):
        """
            Method for testing to update an parcel_status by admin
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().put('/api/v2/parcels/2/status', data=json.dumps(PARCEL_STATUS), headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(['message'], 'order has been updated' )
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict, )
    
    def test_updating_with_empty_order_status_fields(self):
        """
            Method for testing to updating empty fields
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().put('/api/v2/parcels/2/status', data=json.dumps(ORDER), headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code,400)
        self.assertIn('error_message', respond)
        self.assertTrue(['error_message'], 'You have missing fields')
        self.assertIsInstance(respond, dict, )


    def test_updating_destination(self):
        """
            Method for testing to update an parcel_status by admin
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().put('/api/v2/parcels/2/destination', data=json.dumps(DESTINATION_UPDATE), headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(['mes'], 'successfully changed destination' )
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict, )
    
    
    
    def test_updating_current_location(self):
        """
            Method for testing to update an parcel_current location
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().put('/api/v2/parcels/2/currentlocation', data=json.dumps(CURRENTLOCATION_UPDATE), headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(['message'], 'successfully changed current location' )
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict, )

    def test_fetch_all_user_parcels(self):
        """
           Method for testing get all user parcel 
        """
        result = self.client().post('/api/v2/parcels',data=json.dumps(ORDER),headers=self.post_token)
        result = self.client().get('/api/v2/users/parcels',headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertTrue(['status'], 'success' )
    
    def test_fetch_no_user_parcels(self):
        """
           Method for testing get all user parcel 
        """
        result = self.client().get('/api/v2/users/parcels',headers=self.post_token)
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertTrue(['message'], 'user has not made made parcel_orders yet' )
    


    