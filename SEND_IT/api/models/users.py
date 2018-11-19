"""
    This is a a user model
"""
from api.models.database import Databaseconn
from werkzeug.security import generate_password_hash, check_password_hash


        
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

    