"""
Module to handle all error responses
"""
from flask import jsonify


class ErrorFeedback:
    """
    Error handler to handle response errors.
    """
    @staticmethod
    def invalid_data_format():
        response_object = {
        
             'status': 'fail',
            'error_message': 'Please use character strings',
            'data': False
            
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
           
            'status': 'failure',
            'error_message': 'Some fields have no data',
            'data': False }
        return jsonify(response_object), 400
        
    @staticmethod
    def order_absent():
        response_object = {
            'status': 'failure',
            'error_message': 'No orders found at the moment for the order_id',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key():
        response_object = {
           
            'status': 'failure',
            'error_message': 'You have missing fields',
            'data': False
          
        }
        return jsonify(response_object), 404
