"""
This module handels requests to urls.
"""
from flask.views import MethodView
from api.controllers.user_views import SignUp,Login



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
        