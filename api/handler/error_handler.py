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
        
            'error_message': 'Please use character strings'
            
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
           
            'error_message': 'Some fields have no data'
            
        }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key(keys):
        response_object = {
           
            'Blank space': 'You have missing feilds ' 
          
        }
        return jsonify(response_object), 400
