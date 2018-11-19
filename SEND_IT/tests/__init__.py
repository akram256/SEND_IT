import json
from api.models.users import Users


"""
module init tests
"""

token_user = {
    "user_name": "akram",
    "email": "a4a@gmail.com",
    "password": "12345678",
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
    "email": "admin@gmail.com",
    "password": "0123456789",
}

def get_token(client):
    # signup admin
    result = client.post('/api/v1/auth/signup',content_type="application/json",data=json.dumps(token_user))
    if result.status_code != 201:
        raise Exception("failed to signup user")
    # give user admin rights
    user = Users()
    user.set_admin(1)
    # login user and get access token
    result = client.post('/api/v1/auth/login',content_type="application/json",data=json.dumps(token_user))
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