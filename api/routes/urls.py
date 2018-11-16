"""
   Class for defining url / routes
"""
from api.controllers.views import GetParcelOrders
from api.controllers.user_views import AuthUser
from api.controllers.user_views import Login
class Urls():
    """
       GetRoutes defines urls
       params:urls
    """
    @staticmethod
    def fetch_urls(order):
        """
           Add url rule defines the routes for http requests
        """
        order_view = GetParcelOrders.as_view('parcels')
        order.add_url_rule('/api/v1/parcels', view_func=order_view,
                           defaults={'parcel_id': None}, methods=['GET',])
        order.add_url_rule('/api/v1/parcels/<int:parcel_id>',
                           view_func=order_view, methods=['GET',])
        order.add_url_rule('/api/v1/users/<int:user_id>/parcels',
                           view_func=order_view, methods=['GET',])
        parcel_order_post = GetParcelOrders.as_view('post_parcels')
        order.add_url_rule('/api/v1/parcels',
                           view_func=parcel_order_post, methods=['POST',])
        order.add_url_rule('/api/v1/parcels/<int:parcel_id>/cancel',
                           view_func=parcel_order_post, methods=['PUT',])
        users = AuthUser.as_view('users_post')
        order.add_url_rule('/api/v1/auth/users/signup',
                           view_func=users, methods=['POST',])
        order.add_url_rule('/api/v1/auth/users',
                           view_func=users, methods=['GET',])
        user_login =Login.as_view('login')
        order.add_url_rule('/api/v1/auth/users/login',
                           view_func=user_login, methods=['POST',])
        