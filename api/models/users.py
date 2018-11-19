"""
    This is a a user model
"""
from werkzeug.security import generate_password_hash, check_password_hash
from api.models.database import Databaseconn



        
class Users:
    """
        This class handles the users
    """


    def register_a_user(self, username, email, password):
        """
           Method for registering a user
        """

        dbhandler = Databaseconn()

        dbhandler.cursor.execute("SELECT * FROM users WHERE email = %s", [email])
        check_email = dbhandler.cursor.fetchone()
        hashed_password = generate_password_hash(password, method='sha256')
        if check_email:
            return "This email already exists, Please use another email"

        insert_user = "INSERT INTO users(username, email, password) VALUES('"+username+"', '"+email+"', '"+hashed_password+"')"
        dbhandler.cursor.execute(insert_user)
        return "Account successfully created, Please login "
    
    def fetch_password(self, email, password):
        """
           Method for fetching the user_password
        """
        dbhandler = Databaseconn()
        dbhandler.cursor.execute("SELECT * FROM users")
        users = dbhandler.cursor.fetchall()
        for user in users:
            if user[2] == email and check_password_hash(user[3], password):
                return user[0]
        return None 
    def check_admin(self, user_id):
        """
           Method for getting an admin
        """
        dbhandler = Databaseconn()
        dbhandler.cursor.execute("SELECT * FROM users WHERE user_id = '{}' AND is_admin = True".format(user_id))
        user_now = dbhandler.cursor.fetchone()
        return user_now

    def set_admin(self, user_id):
        """
        makes a user an admin by setting the is_admin column to true
        """
        dbhandler = Databaseconn()
        query = "UPDATE users SET is_admin = True WHERE user_id=%s" 
        dbhandler.cursor.execute(query, (user_id,))
        updated_rows = dbhandler.cursor.rowcount
        return updated_rows
    