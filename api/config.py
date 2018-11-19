"""
   Module for for defining the configurations
"""  
import os


class Config(object):
    """
       Method for defining the default environment
    """  
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'codeislove'
    # 'postgresql://username:password@hostname/database'


class DevelopmentConfig(Config):
    """
       Method for defining the development environment
    """   
    DEBUG = True
    # DATABASE_URL = 'postgresql://postgres:12345@localhost/sendit'


class TestingConfig(Config):
    """
        method for defining the development environment
    """
    DEBUG = True
    TESTING = True
    # DATABASE_URL = 'postgresql://postgres:@localhost/sendit_test'







    
