# Todo-API
A simple python flask todo api

## Installation

To install the dependencies run this command:

`pip install - r requirements.txt`

## Run the api
To start the api run the command:

`python app.py`

The listening port is `5000`

To access the various endpoints use:

`http://127.0.0.1:5000/api` as the base url

## Endpoints

POST `http://127.0.0.1:5000/api` 

Data ```       {
        'title': 'Finish Api',
        'description': 'Finish this api and submit',
        'done': False
    },
    ```

GET   `http://127.0.0.1:5000/api`

GET(One) `http://127.0.0.1:5000/api/<id>`

PUT `http://127.0.0.1:5000/api/<id>`

DELETE `http://127.0.0.1:5000/api/<id>`
