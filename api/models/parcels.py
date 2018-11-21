""" 
    This is an Order model
"""
from api.models.database import DatabaseUtilities

dbhandler = DatabaseUtilities()
class Parcel():
    """
        this class handles all order methods
    """
          
    def make_parcel_order(self, user_id,parcel_name,pickup_location,destination,reciever,weight):
        """
           Method for placing an order
           
        """
        add_order_query = "INSERT INTO parcels(parcel_name,pickup_location,destination,reciever,weight,user_id) VALUES(%s,%s,%s,%s,%s,%s);"
        dbhandler.cursor.execute(add_order_query,(parcel_name,pickup_location,destination,reciever,weight,user_id,))
        return "Order has been Placed successfully"
    def get_all_parcels(self):
        """
           Method for getting all parcels
        """
        parcel_query= "SELECT * FROM parcels"
        dbhandler.cursor.execute(parcel_query)
        keys = ["parcel_id", "parcel_name","pickup_location","destination","reciever" ,'current_location',"weight","parcel_status","user_id","order_date"]
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
    

    def update_parcel_status(self,parcel_id,parcel_status):
        """
             this is a method for updating an parcel_status
        """
     
        dbhandler.cursor.execute("""SELECT "parcel_id" FROM parcels WHERE parcel_id= %s""",(parcel_id, ) )
        check_status=dbhandler.cursor.fetchone()
        if not check_status:
            return "No parcel_order to update, please select another parcel_id"
        parcel_status_query = "UPDATE  parcels SET parcel_status = %s WHERE parcel_id = %s;"
        dbhandler.cursor.execute(parcel_status_query,(parcel_status, parcel_id, ))
        updated_rows = dbhandler.cursor.rowcount
        return updated_rows
    
    def update_current_location(self,parcel_id,current_location):
        """
             this is a method for updating a current location
        """
     
        dbhandler.cursor.execute("""SELECT "parcel_id" FROM parcels WHERE parcel_id= %s""",(parcel_id, ) )
        check_current_location=dbhandler.cursor.fetchone()
        if not check_current_location:
            return "No current location to update, please select another parcel_id"
        parcel_current_location_query = "UPDATE  parcels SET current_location = %s WHERE parcel_id = %s;"
        dbhandler.cursor.execute(parcel_current_location_query,(current_location, parcel_id, ))
        updated_rows = dbhandler.cursor.rowcount
        return updated_rows

    def specify_user_parcel(self):
        """
            this method is for getting orders for a specific user
        """
        dbhandler = DatabaseUtilities()
        parcel_user_query= "SELECT * FROM parcels"
        dbhandler.cursor.execute(parcel_user_query)
        keys = ["parcel_id", "parcel_name","pickup_location","destination","reciever","current_location" ,"weight","parcel_status","user_id","order_date"]
        parcels = dbhandler.cursor.fetchall()
        specfic_list = []
        for user_parcel in parcels:
            specfic_list.append(dict(zip(keys, user_parcel)))
        if not specfic_list:
            return "user has not made made parcel_orders yet"
        return specfic_list
    



        
   
        
       
        
       