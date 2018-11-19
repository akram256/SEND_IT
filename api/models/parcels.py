""" 
    This is an Order model
"""
from api.models.database import Databaseconn

dbhandler = Databaseconn()
class Parcel():
    """
        this class handles all order methods
    """
          
    def make_parcel_order(self, user_id,parcel_name,pickup_location,destination,reciever,current_location,weight):
        """
           Method for placing an order
           params: order_now
        """
        add_order_query = "INSERT INTO parcels(parcel_name,pickup_location,destination,reciever,weight,current_location,user_id) VALUES( %s,%s,%s,%s,%s,%s,%s);"
        dbhandler.cursor.execute(add_order_query,(parcel_name,pickup_location,destination,reciever,current_location,weight,user_id,))
        return "Order has been Placed successfully"
    def get_all_parcels(self):
        """
           Method for getting all parcels
        """
        parcel_query= "SELECT * FROM parcels"
        dbhandler.cursor.execute(parcel_query)
        keys = ["parcel_id", "parcel_name","pickup_location","destination","reciever","current_location" ,"weight","parcel_status","user_id","order_date"]
        parcels = dbhandler.cursor.fetchall()
        parcel_list = []
        for parcel in parcels:
            parcel_list.append(dict(zip(keys, parcel)))
        if not parcel_list:
            return "No parcel_orders available at the moment, Please make an order"
        return parcel_list

    def get_one_parcel(self, parcel_id):
        """
           Method for getting a specific order using an inserted_order_id
        """
        dbhandler.cursor.execute("SELECT * FROM parcels WHERE parcel_id = %s", [parcel_id])
        parcel_list = dbhandler.cursor.fetchone()
        keys=["parcel_id", "parcel_name","pickup_location","destination","reciever","weight","parcel_status","current_location" ,"user_id","order_date"]
        if not parcel_list:
            return "Order not available at the moment"
        one_parcel_list = []
        one_parcel_list.append(dict(zip(keys, parcel_list)))
        return one_parcel_list


    def update_parcel_destination(self,parcel_id,destination):
        """
             this is a method for changing destination by the user
        """
     
        dbhandler.cursor.execute("""SELECT "parcel_id" FROM parcels WHERE parcel_id= %s""",(parcel_id, ) )
        check_destination=dbhandler.cursor.fetchone()
        print(check_destination)
        if not check_destination:
            return "No parcel destination to update, please select another parcel_id"
        put_status_query = "UPDATE  parcels SET destination = %s WHERE parcel_id = %s;"
        dbhandler.cursor.execute(put_status_query,(destination, parcel_id, ))
        updated_rows = dbhandler.cursor.rowcount
        return updated_rows
            
    def exist_order(self, parcel_name):
        dbhandler.cursor.execute("""SELECT "parcel_name" FROM parcels WHERE parcel_name= %s""",(parcel_name, ) )
        check_exist=dbhandler.cursor.fetchone()
        if check_exist:
            return True
        return False



        
   
        
       
        
       