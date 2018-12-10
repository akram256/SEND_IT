from run import APP
import unittest
import json
import psycopg2
from api.models.database import DatabaseUtilities  
from . import get_token,get_auth_header,post_auth_header,get_normal_user_token,post_normal,OTHER_USER,ORDER,EMPTY_PARCEL_STATUS,PARCEL_STATUS,CURRENTLOCATION_UPDATE,DESTINATION_UPDATE    

class Testbase(unittest.TestCase):

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
            self.get_user_token=post_normal(client)
            
    def tearDown(self):
        """
           Method for deleting tables in the database object
        """
        with self.client():
            drop_tables = DatabaseUtilities()
            drop_tables.delete_tables()
