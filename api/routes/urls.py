"""
   Class for defining url / routes
"""
from api.controllers.views import GetParcelOrders
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
        parcel_order_post = GetParcelOrders.as_view('post_parcels')
        order.add_url_rule('/api/v1/parcels',
                           view_func=parcel_order_post, methods=['POST',])
        order.add_url_rule('/api/v1/parcels/<int:parcel_id>/cancel',
                           view_func=parcel_order_post, methods=['PUT',])
        