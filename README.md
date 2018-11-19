
# SEND_IT
This is an application for sending and recieving parcel orders


TRAVIS BADGE
[![Build Status](https://travis-ci.org/akram256/SEND_IT.svg?branch=login_db)](https://travis-ci.org/akram256/SEND_IT)


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
		Env
         --Production = sendit'
         --Testing         =sendittest

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

