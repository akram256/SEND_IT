"""
   Module for starting/ running the app
"""
from flask import Flask
from api.routes.urls import Urls
APP = Flask(__name__)
Urls.fetch_urls(APP)
if __name__ == '__main__':
    APP.run()
    