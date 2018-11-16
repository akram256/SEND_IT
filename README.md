# SEND_IT


# Badges

Travis   [![Build Status](https://travis-ci.org/akram256/SEND_IT.svg?branch=post_an_order)](https://travis-ci.org/akram256/SEND_IT)

[![Coverage Status](https://coveralls.io/repos/github/akram256/SEND_IT/badge.svg?branch=get_user_id)](https://coveralls.io/github/akram256/SEND_IT?branch=get_user_id)


[![Maintainability](https://api.codeclimate.com/v1/badges/12a5a63ac9973e406a37/maintainability)](https://codeclimate.com/github/akram256/SEND_IT/maintainability)



# heroku link

https://send-it-ap.herokuapp.com/api/v1/parcels


***Features***
 * User can fetch all parcel orders.
 * User can fetch a specific parcel order.
 * User can make or post a parcel order. 
 * User can can cancel a parcel order.
 
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development
and testing purposes.

### Prerequisites
What you need to install the software and get started.

```bash
- git : to update and clone the repository
- python3: The base language used to develop the api
- pip: a python package used to install project requirements
```
### Installation
```bash
Type:
```
The UI folder houses the user interface. To access the user interface, open the index.html.

The api folder contains the system backend services.
- To install the requirements, run:
- [Python](https://www.python.org/) A general purpose programming language

- [Pip](https://pypi.org/project/pip/) A tool for installing python packages

- [Virtualenv](https://virtualenv.pypa.io/en/stable/)  A tool to create isolated Python environments

#### Development setup
- Create a virtual environment and activate it
    ```bash
     virtualenv venv
     source /env/bin/activate
    ```
- Install dependencies 
    ```bash
    pip3 install -r requirements.txt
    ```
- Run the application
    ```bash
    cd SEND_IT
   
    python run.py
    ```
- Now you can access the system api Endpoints:

| End Point                                           | Verb |Use                                       |
| ----------------------------------------------------|------|------------------------------------------|
|`/api/v1/parcels/`                                    |GET   |Gets a list of parcel orders              |
|`/api/v1/parcels/<int:parcel_id>/`                     |GET   |Gets a specific parcel order  |
|`/api/v1/parcels/`                                    |POST  |creating a parcel order                        |
|`/api/v1/parcels/<int:parcel_id>/`                     |PUT   |Cancels a parcel order    |

## Running the tests

- To run the tests, run the following commands

```bash
pytest --cov=.
```

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/) - Framework language
* HTML
* CSS

## Authors

* **Mukasa  Akram** -  - [akram256](https://github.com/akram256)

## Acknowledgments

* Andela Development Uganda

