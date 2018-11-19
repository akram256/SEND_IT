#Send_it

#Send_it
send_it is an application for parcel couriers around the world




## Getting started
The information below  will be of use n the setup  plus running  the application on your local machine.

## Prerequisites
The  following are needed:
* GIT
* IDE
* Postman
* Internet


## Project links:
**API endpoints:** The code of the endpoints can be accessed at my github account: https://github.com/akram256/send_it
HEROKU LINK:    

## Project features
**API endpoints**
* Create User accounts that can signin/signout from the application
* Place an order for food.
* Get list of orders.
* Get a specific order.
* Update the status of an order.
* Get the menu
* Add food option to the menu
* View the order history for a particular user.

## getting the application on the local machine.
Clone the remote repository to your local machine using the following command: `git  clone https://github.com/akram256/fast-food-fast-db.git`
You can now access the project on your local machine by pointing to the local repository using `cd` and `code .` 
if using Visual Studio code will open the code location.

- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /env/bin/activate

## Databases 
		Env
         --Production =' sendit'
         --Testing         =sendittest

## Running tests:
**Testing the API endpoints.**
Run the `run.py` file and test the endpoints in Postman as shown below:

|     Endpoint                        | Verb          | Action                     |   Parameters     | Privileges |
| ----------------------------------- |:-------------:|  ------------------------- | ----------------- | -----------|
| api/v1/auth/signup                     | POST          | Register a user          | username,email,password,is_admin  | user/admin |
| api/v1/auth/login        | POST           | Login a user          | email, password  | client/admin |
| /api/v1/users/orders        | POST          | Place an order for a parcel          | item_id | client |
| /api/v1/users/orders | GET     | Get the order history of particular user | none  | client |
| /api/v1/orders | GET     | Get all orders | none | admin |
| /api/v1/orders/<int:orderId> | GET     | Fetch specific order | order_id(URL) | admin |
| /api/v1/orders/<int:orderId> | PUT     | Update status of an order | order_now | admin |
| /api/v1/menu | GET     | Get available menu | none  | client/admin |
| /api/v1/menu | POST     | Add a meal option to the menu | item_name | admin |

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
