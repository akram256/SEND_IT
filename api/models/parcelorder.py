from flask import request
""" Module for parcel orders
"""
class ParcelOrder():
    """
        class defining all methods
    """
    userlist = []
    def __init__(self):
        # self.userlist = []
        self.parcelorders = []
        

    def add_parcel(self,user_name,user_id, parcel_name, pick_location,destination, price                  , status,parcel_id):
        """
           Method to post requests
        """
        parcel_list = [order for order in self.parcelorders]

        id = len(parcel_list) + 1
        # user_id =len(parcel_list)+1


       
        order = {
            'User_name': user_name, 'user_id':user_id,'parcel_name': parcel_name,
             'pick_location': pick_location, 'destination': destination,'price': price,'status':status,
            'id': id
        }
        self.parcelorders.append(order)
        return {'New order': [
            order for order in self.parcelorders]}

    def get_all_parcels(self):
        """
           Method for all get requests of parcels
        """
        if not self.parcelorders:
            return True
        return self.parcelorders
        
    def get_one_parcel(self, parcel_id):
        """
           Method for  getting single request
        """
        available_parcel_id = [
            order for order in self.parcelorders
            if order ['id'] == parcel_id]
        if not available_parcel_id:
            return {parcel_id:"Parcel_id doesnot exist"}
        return ( [
            order
            for order in self.parcelorders
            if order['id'] == parcel_id])

    def get_order_of_specific_user(self,user_id):
        """
            method for getting orders for a specific user
        """
        self.userlist = []

        for order in self.parcelorders:
            if user_id == order['user_id']:
                for order in self.parcelorders:
                    if user_id == order['user_id']:
                        self.userlist.append(order)
                response= {
                    'Parcels': 'Parcel orders gotten successfully',
                    'data': self.userlist
                }
                return (response)
            return ("No orders at the moment")


    def cancel_a_parcel(self,parcel_id):
        """
           method for updating order status
           params:parcel_id
           response: dictionary
        """
        for order in self.parcelorders:
            if parcel_id == order['id']:
                parcel_json = request.get_json()
                status = parcel_json['status']
                order['status'] = status
                return {parcel_id:'Parcel has been cancelled'}
   
