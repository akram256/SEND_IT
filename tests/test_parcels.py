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

    def test_fetch_all_parcels(self):
        """
           Method for testing the get function which returns all parcel_orders
        """
        result = self.client().get('api/v1/parcels')
        respond = json.loads(result.data.decode("utf"))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Parcels', respond)
        self.assertIsInstance(respond, dict)

    def test_make_a_parcel(self):
        """
            Method for tesing the post function which posts a parcel_order
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_id= 1,user_name="Akram", parcel_name="gift", pickup_location="mbra",destination="kampala", price =10000 ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('parcelorders', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 201)
        self.assertTrue(result.json["parcelorders"])

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

    def test_missing_field(self):
        """
            Method for testing a missing field in the post function
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=18,user_id=1, user_name="Akram",email="akram@gmail.com", parcel_name="gift", pick_location="mbra"  
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Blank space', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
   
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
    # def test_missing_status_field(self)


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
                                    data=json.dumps(dict(parcel_id=1,user_id=1, user_name="Akram",email="akram@gmail.com", parcel_name="gift", pickup_location="mbra",destination="kampala", price ="1000" ,
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["message"])

    def test_invalid_data(self):
        """
            Method for testing invalid data input
        """
        result = self.client().post('api/v1/parcels',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1, user_id=1,user_name="",email="akram@gmail.com", parcel_name=10000, pickup_location="mbra",destination="kampala", price =1000
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('error_message', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 400)
        self.assertTrue(result.json["error_message"])
    
    def test_cancel_order(self):
        """
            Method for testing for cancel order
        """
        result = self.client().put('api/v1/parcels/1/cancel',
                                    content_type="application/json",
                                    data=json.dumps(dict(parcel_id=1,user_id=1,status="cancelled" 
                                                         )))
        respond = json.loads(result.data.decode("utf8"))
        self.assertIn('Parcel_order', respond)
        self.assertIsInstance(respond, dict)
        self.assertEqual(result.status_code, 200)
    
    def test_get_specific_user(self):
        """
            Method for testing the get function which returns one parcel_order
        """
        result = self.client().get('api/v1/users/1/parcels')
        result2 = self.client().get('api/v1/users/a/parcels')
        respond = json.loads(result.data.decode("utf8"))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result2.status_code, 404)
        self.assertIsInstance(respond, dict)
      
    

       
