"""
   Module for defining views
"""

from flask import jsonify, request
from flask.views import MethodView
from api.models.parcelorder import ParcelOrder
import re

parcel_orders = ParcelOrder()


class GetParcelOrders(MethodView):
    """
       class for defining views

    """

    def post(self):
        """
           method to post all requests
        """
        keys = ("user_name","email", "parcel_name",  "pickup_location","destination","price")

        if not set(keys).issubset(set(request.json)):
            return jsonify({'Blank space': 'Your request has Empty feilds'}), 400

        if request.json['user_name'] == "":
            if request.json['parcel_name'] == "":
                return jsonify({'parcel_name': 'enter parcel_name'}), 400
            return jsonify({'user_name': 'enter user_name'}), 400

        if (' ' in request.json['user_name']) == True:
            if (' ' in request.json['parcel_name']) == True:
                return jsonify({'message': 'parcel_name should not contain any spaces'}), 400
            return jsonify({'message': 'user_name should not contain any spaces'}), 400

        if not isinstance(request.json['price'], int):
            return jsonify({'message': 'enter price as an interger'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter a correct email'}), 400

        user_name = request.json['user_name']
        email = request.json['email']
        parcel_name = request.json['parcel_name']
        pickup_location = request.json['pickup_location']
        destination = request.json['destination']
        price = request.json['price']
        status ='pending'
        user_id="user_id"
        id = 'id'
        parcel_orders.add_parcel(user_name, email,parcel_name,pickup_location,destination,  price, status,user_id,id)
        response_object =  parcel_orders.__dict__
        
        return jsonify(response_object), 201
    def get(self, parcel_id):
        """
           method for all get requests and single request
        """
        if parcel_id is None:
            if parcel_orders.get_all_parcels() is True:
                return jsonify({'Parcels':'No Parcel orders available at the moment,Please make an order'})
            return jsonify({'Parcels': parcel_orders.get_all_parcels()}), 200
        return jsonify({'Parcels': parcel_orders.get_one_parcel(parcel_id)}), 200

    def put(self,parcel_id):
        """
           post method for puts/cancels requests
           param: route /api/parcels/<int:parcel_id>/cancel
           response: json data
        """
        return jsonify({'Parcel_order':parcel_orders.cancel_a_parcel(parcel_id)}),200
       
        