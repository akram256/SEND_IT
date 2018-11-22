import json
from api.models.users import Users


"""
module init tests
"""

token_user = {
    "user_name": "admin",
    "email": "admin@gmail.com",
    "password": "123456789",
}
OTHER_USER = {
    "user_name": "mukasa",
    "email": "mukasa@gmail.com",
    "password": "12345678",
    "is_admin":False,
}
EMPTY_NAME = {
    "user_name": "       ",
    "email": "a4a@gmail.com",
    "password": "0123456789",
}

LOGIN = {
    "email": "a4a@gmail.com",
    "password": "0123456789",

}
LOGIN_OTHER_USER = {
    "email": "adin@gmail.com",
    "password": "0123456789",
}
ORDER = {
    "parcel_name": "book",
    "pickup_location":"kla",
    "destination":"mbra", 
    "reciever":"akram",
    "weight":12,

    
}
EMPTY_ORDER = {
    "parcel_name": "",
    "pickup_location":"",
    "destination":"mbra", 
    "reciever":"akram",
    "weight":12,
}

EMPTY_PARCEL_STATUS = {
    "parcel_status": "",
}
PARCEL_STATUS = {
    "parcel_status": "completed",
}
CURRENTLOCATION_UPDATE ={
    "current_location":"jinja",
}
EMPTY_UPDATE ={
    "destination":"",
}

DESTINATION_UPDATE ={
    "destination":"Jinja",
}


def get_token(client):
    # signup admin
    result = client.post('/api/v2/auth/signup',content_type="application/json",data=json.dumps(token_user))
    if result.status_code != 201:
        raise Exception("failed to signup user")
    # give user admin rights
    user = Users()
    user.set_admin(1)
    # login user and get access token
    result = client.post('/api/v2/auth/login',content_type="application/json",data=json.dumps(token_user))
    if result.status_code != 200:
        raise Exception("failed to login user")
    response = json.loads(result.data.decode())
    # print(response ['access_token'])
    return response ['access_token']

def post_auth_header(client):
    token = get_token(client)
    return{
        'Content-type':"application/json",
        "authorization": "Bearer {}".format(token) 
    }

def get_auth_header(client):
    token = get_token(client)
    return{
        'Content-Type':"application/json",
        "Token ": token
    }