""" Module for parcel orders
"""
class ParcelOrder():
    """
        class defining all methods
    """
    def __init__(self):
        self.parcelorders = []

    def add_parcel(self, user_name,email, parcel_name, pick_location,destination, price                  , status,parcel_id):
        """
           Method to post requests
        """
        parcel_list = [order for order in self.parcelorders]

        id = len(parcel_list) + 1


        order = {
            'User_name': user_name,'email':email, 'parcel_name': parcel_name,
             'pick_location': pick_location, 'destination': destination,'price': price,'status':status,
            'id': id
        }
        self.parcelorders.append(order)
        return self.parcelorders


