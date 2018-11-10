"""
    Module for making tests on the application
"""
import unittest
import json
from run import APP

class TestViews(unittest.TestCase):
    """"
        Class for making tests
        params: unittest.testCase
    """

    def setUp(self):
        """
           Method for making the client object
        """
        self.client = APP.test_client

    def test_make_a_parcel(self):
        """
            Method for tesing the post function which posts a parcel_order
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="Akram",email="akram@gmail.com", parcel_name="gift", pickup_location="mbra",destination="kampala", price =10000 ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Parcel_orders', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["Parcel_orders"])

    def test_missing_field(self):
        """
            Method for testing a missing field in the post function
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18, user_name="Akram",email="akram@gmail.com", parcel_name="gift", pick_location="mbra"  
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Blank space', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    def test_wrong_email_address(self):
        """
            Method for testing a wrong email in the post function
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18, user_name="Akram",email="", parcel_name="gift", pick_location="mbra"  
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Blank space', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
    def test_fetch_all_parcels(self):
        """
           Method for testing the get function which returns all parcel_orders
        """
        result = self.client().get('api/v1/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Parcels', respond)
        self.assertIsInstance(respond, dict)
    def test_get_a_Parcel(self):
        """
            Method for testing the get function which returns one parcel_order
        """
        result = self.client().get('api/v1/parcels/17')
        result2 = self.client().get('api/v1/parcels/a')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)
    def test_cancel_a_Parcel(self):
        """
            Method for testing the update function
        """
        result1 = self.client().put('api/v1/parcels/1/cancel',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1,
                                                         status=
                                                         "Pending")))
       
        respond = json.loads(result1.data.decode("utf8"))
        self.assertIn('Parcel_order', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result1.status_code, 200)

    def test_inputs(self):
        """
            Method for testing the wrong post in-puts
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18
                                                         )))
        result_response = json.loads(result.data.decode("utf8"))
        self.assertTrue(result_response['Blank space'], 'Your request has empty fields')
        self.assertTrue(result.content_type, 'application/json')
        self.assertEqual(result.status_code, 400)
    def test_wrong_price_format(self):
        """
            Method for testing wrong price format
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="Akram",email="akram@gmail.com", parcel_name="gift", pickup_location="mbra",destination="kampala", price ="1000" ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_wrong_email_format(self):
        """
            Method for testing wrong email format
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="Akram",email="akramgmail.com", parcel_name="gift", pickup_location="mbra",destination="kampala", price =1000 ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('email', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["email"])

    def test_missing_user_name(self):
        """
            Method for testing wrong email format
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="",email="akram@gmail.com", parcel_name="gift", pickup_location="mbra",destination="kampala", price =1000 ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('user_name', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["user_name"])
    
    def test_missing_parcel_name(self):
        """
            Method for testing wrong email format
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_name="Akram",email="akram@gmail.com", parcel_name= "", pickup_location="mbra",destination="kampala", price =1000 ,``
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["parcel_name"])
       

