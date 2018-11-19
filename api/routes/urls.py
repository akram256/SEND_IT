"""
This module handels requests to urls.
"""
from flask.views import MethodView
from api.controllers.user_views import SignUp,Login
from api.controllers.parcel_views import PlaceOrder,GetParcel,UpdateDestination,UpdateStatus



class Urls(object):
    """
    Class to generate urls
    """
      
    @staticmethod
    def generate_url(app):
        """
         Generates urls on the app context
        :param: app: takes in the app variable
        :return: urls
        """
        app.add_url_rule('/api/v1/auth/signup',
                         view_func=SignUp.as_view('Signup'), methods=['POST',])
        app.add_url_rule('/api/v1/auth/login',
                         view_func=Login.as_view('Login'), methods=['POST',])
        app.add_url_rule('/api/v1/parcels',
                         view_func=PlaceOrder.as_view('parcel order'), methods=['POST',])
        app.add_url_rule('/api/v1/parcels',
                         view_func=GetParcel.as_view('PlaceOrder'),
                         defaults={'parcel_id': None}, methods=['GET',])
        app.add_url_rule('/api/v1/parcels/<int:parcel_id>',
                         view_func=GetParcel.as_view('one_order'), methods=['GET',])
        app.add_url_rule('/api/v1/parcels/<int:parcel_id>/destination',
                         view_func=UpdateDestination.as_view('update destination'), methods=['PUT',])
        app.add_url_rule('/api/v1/parcels/<int:parcel_id>/status',
                         view_func=UpdateStatus.as_view('update status'), methods=['PUT',])
                         