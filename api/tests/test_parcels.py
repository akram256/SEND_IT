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
           Method for tesing the get function which returns all parcel_orders
        """
        result = self.client().get('api/v1/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Parcels', respond)
        self.assertIsInstance(respond, dict)
        

