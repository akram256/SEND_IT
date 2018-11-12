"""
   Module for defining views
"""

from flask import jsonify, request
from flask.views import MethodView
from api.handler.error_handler import ErrorFeedback
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
      
        keys = ("user_name" ,"user_id","parcel_name",  "pickup_location","destination","price")
        
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(keys)
            
        if not isinstance(request.json['price'], int):
            return jsonify({'message': 'enter price as an interger'}), 400

      
        post_data = request.get_json()
        user_name =request.json['user_name']
        user_id = request.json['user_id']
        parcel_name = request.json['parcel_name']
        pickup_location = request.json['pickup_location']
        destination = request.json['destination']
        price = request.json['price']
        status ='pending'
        id = 'id'   
        
        try:
            user_name = post_data['user_name'].strip()
            parcel_name = post_data['parcel_name'].strip()
            pickup_location = post_data['pickup_location'].strip()
            destination = post_data['destination'].strip()
            price = post_data['price']
            user_id = post_data['user_id']
            status ='pending'
            id = 'id'
        except AttributeError:
            return ErrorFeedback.invalid_data_format()

        if not user_name or not parcel_name or not pickup_location or not destination or not price:
            return ErrorFeedback.empty_data_fields()

        parcel_orders.add_parcel(user_name,user_id,parcel_name,pickup_location,destination,price, status,id)

        response_object =  parcel_orders.__dict__
        
        return jsonify(response_object), 201


    def get(self, parcel_id=None, user_id=None):
        """
           method for all get requests and single request
        """
        parcels = parcel_orders.get_all_parcels()
        if not parcels:
            return jsonify({'Parcels': parcel_orders.get_all_parcels()}), 200
        elif parcel_id:
            return jsonify({'Parcels': parcel_orders.get_one_parcel(parcel_id)}), 200  
        elif user_id:
            return jsonify({'Parcels': parcel_orders.get_order_of_specific_user(user_id)}),200
        
    def put(self,parcel_id):
        """
           post method for puts/cancels requests
           param: route /api/parcels/<int:parcel_id>/cancel
           response: json data
        """
        post_data = request.get_json()

        key= 'status'
        if key not in post_data:
            return ErrorFeedback.missing_key
        try:
            status = post_data['status'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if not status:
            return ErrorFeedback.empty_data_fields()

        return jsonify({'Parcel_order':parcel_orders.cancel_a_parcel(parcel_id)}),200
       
        