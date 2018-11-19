"""
This module provides responses to url requests.
"""
import re
from flask import jsonify, request
from flask.views import MethodView
from api.models.database import Databaseconn
from api.models.users import Users
from api.models.parcels import Parcel
from api.handler.error_handler import ErrorFeedback
from flask_jwt_extended import  jwt_required, create_access_token, get_jwt_identity




class PlaceOrder(MethodView):
    """
        Method for placing an order
    """
    @jwt_required
    def post(self):
        """
            this is a method for placing an order
        """   
        place_order = Parcel ()
        key = ("parcel_name","pickup_location","destination","reciever","weight","current_location",)

        if not set(key).issubset(set(request.json)):
            return ErrorFeedback.missing_key(key)
        post_data = request.get_json()
        try:
            parcel_name = post_data['parcel_name'].strip()
            pickup_location = post_data['pickup_location'].strip()
            destination = post_data['destination'].strip()
            weight = post_data['weight']
            current_location = post_data['current_location']
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if  not parcel_name or not pickup_location or not destination or not weight or not current_location:
            return ErrorFeedback.empty_data_fields()
        if place_order.exist_order(request.json['parcel_name']):
                return jsonify({'Alert':'wait order is being processed, You cant order twice'})
       
        user_id = get_jwt_identity()
        parcel_data = place_order.make_parcel_order(str(user_id),request.json['parcel_name'],request.json['pickup_location'],request.json['destination'],request.json['reciever'],request.json['weight'],request.json['current_location'])
        if parcel_data:
            return jsonify({'message': parcel_data}), 201
        return jsonify({'message':'no order made'})

class GetParcel(MethodView):
    """
       Class to get all orders
       params: order_id
       respone: json data
    """
    @jwt_required
    def get(self, parcel_id):
        """
           get method for get parcel history
           param: route /api/v1/parcels and /api/v1/parcfels/<int:parcel_id>
           response: json data get_all_parcels() and self.get_one_parcel(parcel_id)
        """
       
        get_parcel = Parcel()

        user_id = get_jwt_identity()
        # is_admin = False
        # is_admin_now = get_parcel.activate_admin(user_id,is_admin)
        # if  is_admin_now is True:
        user_id = get_jwt_identity()
        is_admin = get_parcel.activate_admin(user_id)
        if user_id and  not is_admin:
            if parcel_id is None:
                parcels_list = get_parcel.get_all_parcels()
                if parcels_list == "No parcel_orders available at the moment, Please make an order":
                    return jsonify({"Orders": parcels_list}), 404
                return jsonify({"Orders": parcels_list}), 200
            
            orders_list = get_parcel.get_one_parcel(parcel_id)
            if orders_list == "No parcel_orders available at the moment, Please make an order":
                return jsonify({"Order": "No orders found at the moment for the order_id"}), 404
            return jsonify({"Order": orders_list}), 200
        return jsonify({'Alert':"Not Authorised to perform this task"})

class UpdateDestination(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
    @jwt_required
    def put(self,parcel_id):
        """
            this method for putting or updating the order_status
        """
        update_destination = Parcel()
        # user_id = get_jwt_identity()
        # is_admin = True
        # is_admin_now = update_destination.update_parcel_destination(user_id,destination)
        # if  is_admin_now is not True:
        user_id = get_jwt_identity()
        is_admin = update_destination.activate_admin(user_id)
        if user_id and  not is_admin:
            keys = ("destination",)
            if not set(keys).issubset(set(request.json)):
                return ErrorFeedback.missing_key(keys), 400
            try:
                parcel_destination = request.json['parcel_destination'].strip()
            except AttributeError:
                return ErrorFeedback.invalid_data_format(),400
            if not parcel_destination:
                return ErrorFeedback.empty_data_fields(),400

            new_parcel_destination = update_destination.update_parcel_destination(str(parcel_id), request.json['destination'].strip())

            if new_parcel_destination:
                return jsonify({'message': "Destination has been updated"}), 200
            return jsonify({"message":'No Destination to update'})
        return jsonify({'Alert':"Not Authorised to perform this task"}),401


class UpdateStatus(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
    @jwt_required
    def put(self,parcel_id):
        """
            this method for putting or updating the order_status
        """
      
        update_status = Parcel()
        # user_id = get_jwt_identity()
        # is_admin = True
        # is_admin_now = update_status.update_parcel_status(user_id,parcel_status)
        # if  is_admin_now is True:
        user_id = get_jwt_identity()
        is_admin = update_status.activate_admin(user_id)
        if user_id and  not is_admin:
            post_data =request.get_json()
            keys = ("parcel_status",)
            if keys not in post_data:
                return ErrorFeedback.missing_key(keys)
            try:
                parcel_status = post_data['parcel_status'].strip()
            except AttributeError:
                return ErrorFeedback.invalid_data_format(),400
            if not parcel_status:
                return ErrorFeedback.empty_data_fields(),400
            new_parcel_status = update_status.update_parcel_status(str(parcel_id), request.json['parcel_status'].strip())

            if new_parcel_status:
                return jsonify({'message': "Parcel status has been updated"}), 200
            return jsonify({"message":'No Parcel status to update'}), 400
        return jsonify({'Alert':"Not Authorised to perform this task"})

class Activateadmin(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
    @jwt_required
    def put(self,user_id):
        """
            this method for putting or updating the order_status
        """
        # user = Users()
        update_admin = Parcel()
        # user_id = get_jwt_identity()
        # is_admin_now = user.check_admin(user_id)
        # if user_id and is_admin_now :

        admin = update_admin.activate_admin(str(user_id),)

        if admin:
            return jsonify({'message': "Your now admin"}), 200
        
        


        
        
            
