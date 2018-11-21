"""
This module handlesusers and database
"""
import os
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask import request, jsonify
from flask.views import MethodView


class DatabaseUtilities:
    
    """
        This method returns all 
        orders in a JSON format
        :return
    """
    
    def __init__(self):
    

        """
        This method creates the connection object 
        """
       
        try:

            
            if(os.getenv("FLASK_ENV")) == "Production":
                self.connection = psycopg2.connect(os.getenv("DATABASE_URL"))
            elif(os.getenv("FLASK_ENV")) == "TESTING":
                self.connection = psycopg2.connect('postgresql://postgres:12345@localhost/sendittest')
            else:
                self.connection = psycopg2.connect("postgresql://postgres:12345@localhost/sendit")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

        except(Exception, psycopg2.DatabaseError) as error:
            raise error
    

    def create_tables(self):
        """
        This method creates tables in the PostgreSQL database.
        It connects to the database and creates tables one by one
        for command in commands:
        cur.execute(command)
        """
        commands = (
            """
            CREATE TABLE if not exists "users" (
                    user_id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    email VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(80) NOT NULL,
                    is_admin BOOLEAN NULL DEFAULT FALSE
                        
                )
            """,
            """
            CREATE TABLE if not exists "parcels" (
                    parcel_id SERIAL PRIMARY KEY,
                    parcel_name VARCHAR (50) NOT NULL,
                    pickup_location VARCHAR (50) NOT NULL,
                    destination VARCHAR (50) NOT NULL,
                    reciever  VARCHAR (50) NOT NULL,
                    current_location  VARCHAR (50) DEFAULT 'in_transit',
                    weight integer,
                    parcel_status VARCHAR (255) DEFAULT 'pending',
                    user_id integer,
                    FOREIGN KEY (user_id)
                    REFERENCES users(user_id),
                    order_date TIMESTAMP DEFAULT NOW()
                    
                    
          
                )
            """,)
    

        try:
            
            for command in commands:
                self.cursor.execute(command)
        except(Exception, psycopg2.DatabaseError) as error:
            raise error
        
        

    def delete_tables(self):
       
        """
            this method is for dropping tables
        """
        table_names=['users','parcels']
        for name in table_names:
            self.cursor.execute("DROP TABLE IF EXISTS {} CASCADE".format(name))
        

   