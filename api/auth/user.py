from flask import request
""" Module for user_model
"""
class Users():
    """
        class defining all methods
    """
    
    def __init__(self):
        self.userlist = []
        

    def add_user(self,user_name,name,password,user_id ):
        """
           Method to post requests
        """
        users_list = [user for user in self.userlist]

        id = len(users_list) + 1
        user = {
            'user_name': user_name,'name':name,'password':password,
            'id': id
        }

        self.userlist.append(user)
        return {'New user': [
            user for user in self.userlist]}

    def get_all_users(self):
        """
           Method for all get requests of parcels
        """
        if not self.userlist:
            return True
        return self.userlist

    def login_user(self,user_name,password):
        """
           Method to post requests
        """
        users = self.userlist

        for user in users:
            if user['user_name'] ==user_name:
               return user
            return None

