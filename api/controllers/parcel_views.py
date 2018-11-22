"""
This module provides responses to url requests.
"""
import flasgger
from flask_jwt_extended import  jwt_required,  get_jwt_identity
from flask import jsonify, request
from flask.views import MethodView
from api.models.users import Users
from api.models.parcels import Parcel
from api.handler.error_handler import ErrorFeedback

activate_admin=Users()
class PlaceOrder(MethodView):
    """
        Method for placing an order
    """
    @jwt_required
    @flasgger.swag_from("../docs/post.yml")
    def post(self):
        """
            this is a method for placing an order
        """   
        place_order = Parcel ()
        key = ("parcel_name","pickup_location","destination","reciever","weight",)

        if not set(key).issubset(set(request.json)):
            return ErrorFeedback.missing_key()
        post_data = request.get_json()
        try:
            parcel_name = post_data['parcel_name'].strip()
            pickup_location = post_data['pickup_location'].strip()
            destination = post_data['destination'].strip()
            weight = post_data['weight']
        except AttributeError:
            return ErrorFeedback.invalid_data_format()
        if  not parcel_name or not pickup_location or not destination or not weight:
            return ErrorFeedback.empty_data_fields()
        if place_order.exist_order(request.json['parcel_name']):
                return jsonify({'message':'wait order is being processed, You cant order twice'})
        user_id = get_jwt_identity()
        parcel_data = place_order.make_parcel_order(str(user_id),request.json['parcel_name'],request.json['pickup_location'],request.json['destination'],request.json['reciever'],request.json['weight'])
        if parcel_data:
            response_object = {
            'status': 'Success',
            'message':parcel_data   
        }
            return jsonify(response_object), 201

class GetParcel(MethodView):
    """
       Class to get all orders
       params: order_id
       respone: json data
    """
    
    @jwt_required
    @flasgger.swag_from("../docs/get_all_parcels.yml")
    def get(self, parcel_id):
        """
           get method for get parcel history
           param: route /api/v1/parcels and /api/v1/parcfels/<int:parcel_id>
           response: json data get_all_parcels() and self.get_one_parcel(parcel_id)
        """
        get_parcel = Parcel()
        user_id = get_jwt_identity()
        is_admin = activate_admin.check_admin_status(user_id)
        if user_id and is_admin:
            if parcel_id is None:
                parcels_list = get_parcel.get_all_parcels()
                if parcels_list == "No parcel_orders available at the moment, Please make an order":
                    return jsonify({"Orders": parcels_list}), 404
                return jsonify({"Orders": parcels_list}), 200
            orders_list = get_parcel.get_one_parcel(parcel_id)
            if orders_list == "No parcel_orders available at the moment, Please make an order":
                return ErrorFeedback.order_absent(), 404
            response_object = {
            'status': 'Success',
            'message': orders_list}
            return jsonify(response_object), 200
        return jsonify({'Alert':"Not Authorised to perform this task"})

class UpdateDestination(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
   
    @jwt_required
    @flasgger.swag_from("../docs/update_destination.yml")
    def put(self,parcel_id):
        """
            this method for putting or updating the order_status
        """
        update_destination = Parcel()
        keys = ("destination",)
        if not set(keys).issubset(set(request.json)):
            return ErrorFeedback.missing_key(), 400
        try:
            destination = request.json['destination'].strip()
        except AttributeError:
            return ErrorFeedback.invalid_data_format(),400
        if not destination:
            return jsonify({'message':'You have field has no data, Please fill it',
                                'status':'failure'}),400
        new_parcel_destination = update_destination.update_parcel_destination(str(parcel_id), request.json['destination'].strip())
        if new_parcel_destination == 'No parcel destination to update, please select another parcel_id':
            return jsonify({'message':'No order to update',
            'status':'failure'}),400
        response_object = {
            'status': 'success',
            'message':'destination has been updated'}
        return jsonify(response_object), 200
class UpdateStatus(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
    @jwt_required
    @flasgger.swag_from("../docs/update_status.yml")
    def put(self,parcel_id):
        """
            this method for putting or updating the order_status
        """
        update_status = Parcel()
        user_id = get_jwt_identity()
        is_admin = activate_admin.check_admin_status(user_id)
        if user_id and is_admin:
            post_data =request.get_json()
            keys = ('parcel_status')
            if keys not in post_data:
                return ErrorFeedback.missing_key()
            try:
                parcel_status = post_data['parcel_status'].strip()
            except AttributeError:
                return ErrorFeedback.invalid_data_format(),400
            if not parcel_status:
                return jsonify({'message':'You have field has no data, Please fill it',
                                'status':'failure'}),400
            new_parcel_status = update_status.update_parcel_status(str(parcel_id), request.json['parcel_status'].strip())

            if new_parcel_status == 'No parcel_order to update, please select another parcel_id':
                return jsonify({'message':'No order to update',
                'status':'failure'}),400
            response_object = {
                'status': 'Success',
                'message': 'Status has beeen updated' }
            return jsonify(response_object), 200
            
        return jsonify({'Alert':"Not Authorised to perform this task"})
class UpdateCurrentlocation(MethodView):
    """
        Class to get all orders
       params: order_status
       respone: json data
    """
   
    @jwt_required
    @flasgger.swag_from("../docs/update_current_location.yml")
    def put(self,parcel_id):
        """
            this method for putting or updating current location
        """
        update_current_location = Parcel() 
        user_id = get_jwt_identity()
        is_admin = activate_admin.check_admin_status(user_id)
        if user_id and is_admin:
            post_data =request.get_json()
            keys = ("current_location")
            if keys not in post_data:
                return ErrorFeedback.missing_key()
            try:
                current_location = post_data['current_location'].strip()
            except AttributeError:
                return ErrorFeedback.invalid_data_format(),400
            if not current_location:
                return jsonify({'message':'You have field has no data, Please fill it',
                                'status':'failure'}),400
            new_parcel_location = update_current_location.update_current_location(str(parcel_id), request.json['current_location'].strip())

            if not new_parcel_location == 'No current location to update, please select another parcel_id':
                response_object = {
                'status': 'Success',
                'message': 'current location has been updated'}
                return jsonify(response_object), 200
            return jsonify({'message':'No order to update',
            'status':'failure'}),400
        return jsonify({'Alert':"Not Authorised to perform this task"})

class GetSpecific(MethodView):
    """
        method for getting specific user parcels
    """
    # @flasgger.swag_from("../docs/specific_user.yml")
    @jwt_required
    def get(self,user_id=None,parcel_id=None):
        """
            this method returns parcels for a particular user
        """
        specify_order = Parcel()
        user_id = get_jwt_identity()
        if parcel_id is None:
            user_list = specify_order.specify_user_parcel(user_id)
            if user_list == "no order now":
                return ErrorFeedback.order_absent(), 404
            response_object = {
                'status': 'Success',
                'message': user_list
                }
            return jsonify(response_object), 200
        return jsonify({"Alert":"Not allowed to perform this task"})
