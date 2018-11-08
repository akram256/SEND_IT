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
            return jsonify({'user_name': 'enter user_name'}), 400

        if (' ' in request.json['user_name']) == True:
            return jsonify({'message': 'user_name should not contain any spaces'}), 400

        if request.json['parcel_name'] == "":
            return jsonify({'parcel_name': 'enter parcel_name'}), 400

        if (' ' in request.json['parcel_name']) == True:
            return jsonify({'message': 'parcel_name should not contain any spaces'}), 400

        if not isinstance(request.json['price'], int):
            return jsonify({'message': 'enter price as an interger'}), 400

        pattern = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
        if not re.match(pattern, request.json['email']):
            return jsonify({'email': 'Enter way of your email'}), 400
        # if request.json['status'] == "":
        #     return jsonify({'status': 'please enter status'}), 400

        # if not isinstance(request.json['status'], str):
        #     return jsonify({'message': 'enter status as an string'}), 400

        user_name = request.json['user_name']
        email = request.json['email']
        parcel_name = request.json['parcel_name']
        pickup_location = request.json['pickup_location']
        destination = request.json['destination']
        price = request.json['price']
        status ='pending'

        id = 'id'
        parcel_orders.add_parcel(user_name, email,parcel_name,pickup_location,destination,  price, status,id)
        response_object = {
            'Parcel_orders': parcel_orders.__dict__
        }
        return jsonify(response_object), 201
     
        