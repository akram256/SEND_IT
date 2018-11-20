
# SEND_IT
This is an application for sending and recieving parcel orders


TRAVIS BADGE
[![Build Status](https://travis-ci.org/akram256/SEND_IT.svg?branch=challenge_three)](https://travis-ci.org/akram256/SEND_IT)

COVERAGE
[![Coverage Status](https://coveralls.io/repos/github/akram256/SEND_IT/badge.svg?branch=challenge_three)](https://coveralls.io/github/akram256/SEND_IT?branch=challenge_three)

[![Maintainability](https://api.codeclimate.com/v1/badges/12a5a63ac9973e406a37/maintainability)](https://codeclimate.com/github/akram256/SEND_IT/maintainability)


## Getting started
The information below  will be of use n the setup  plus running  the application on your local machine.

## Prerequisites
The  following are needed:
* GIT
* IDE
* Postman
* Internet


## Project links:
**API endpoints:** The code of the endpoints can be accessed at my github account: https://github.com/akram256/sendit
HEROKU LINK:   

## Project features
**API endpoints**
* Create User accounts that can signin/signout from the application
* Place a parcel order.
* Get list of parcel_orders.
* Get a specific parcel_order.
* Update the status of a parcel order.
* Update destination of parcel_order
* Update current location of parcel order
* View the parcel_order history for a particular user.

## getting the application on the local machine.
Clone the remote repository to your local machine using the following command: `git  clone https://github.com/akram256/sendit.git`
You can now access the project on your local machine by pointing to the local repository using `cd` and `code .` 
if using Visual Studio code will open the code location.

- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /env/bin/activate

## Databases 
		Env variables
         --development = sendit'
         --TESTING         = sendittest
         --Production = Heroku postgres

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

    Endpoint                        | Verb          | Action                     |   Parameters     | Privileges |
| ----------------------------------- |:-------------:|  ------------------------- | ----------------- | -----------|
| api/v1/auth/signup                     | POST          | Register a user          | username,email,password,is_admin  | user/admin |
| api/v1/auth/login        | POST           | Login a user          | email, password  | client/admin |
| /api/v1/parcels        | POST          | Make_a_parcel_order          | parcel_name, pickup_location,destination,reciever,current_location,weight | client |
| /api/v1/users/parcels | GET     | Get all parcel_orders for a particular user   | none  | client |
| /api/v1/parcel | GET     | Get all parcel_orders | none | admin |
| /api/v1/parcels/<int:parcel_Id> | GET     | Fetch specific parcel | parcel_id(URL) | admin |
| /api/v1/parcels/<int:parcel_Id>/status | PUT     | Update status of a parcel | parcel_status | admin |
| /api/v1/parcels/<int:parcel_Id>/destination| PUT     | Update destination | destination  | client |
|/api/v1/parcels/<int:parcel_Id>/currenlocation| PUT    | Update currentlocation | current_location | admin |

## Running the tests

- To run the tests, run the following commands

```bash
pytest --cov=.

## Deployment:
N/A

## Built with:
**API endpoints**
* Python 3.6
* Flask
* JWT_Extended
* PostgreSQL

## Authors

* **Mukasa  Akram** -  - [akram256](https://github.com/akram256)

## Acknowledgments

* Andela Development Uganda


