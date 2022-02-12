# API COURS DEVELOPPEMENT PYTHON FLASK

## Motivations
Cette API permet de gérer une table etudiants créée dans la base de données.
## Getting Started

### Installing Dependencies

#### Python 3.9.7
#### pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)

Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv 

#### PIP Dependencies

Exécuter la commande ci dessous pour installer les dépendences
```bash
pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the plants_database.sql file provided. From the backend folder in terminal run:
```bash
psql plants_database < plants_database.sql
```

## Running the server

From within the `plants_api` directory first ensure you are working using your created virtual environment.

To run the server on Linux or Mac, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
To run the server on Windows, execute:

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request"
}

The API will return four error types when requests fail:
. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found

## Endpoints
. ## GET/etudiants

    GENERAL: cet endpoint permet de récupérer la liste des étudiants 
    
        
    SAMPLE: curl -i http://localhost:5000/etudiants

        {
    "etudiants": [
        {
            "adresse": "Lome",
            "id": 1,
            "nom": "OURO",
            "prenom": "Badiou"
        },
        {
            "adresse": "Agoe",
            "id": 2,
            "nom": "Ali",
            "prenom": "Baba"
        }
    ],
    "success": true,
    "total_etudiants": 2
}
```

. ## DELETE/etudiants (id)

    GENERAL: Cet endpoint permet de supprimer un etudiant
        Les resulats de cette requete se présentent comme suit:
        SAMPLE: curl -X DELETE http://localhost:5000/etudiants/2
```
         {
    "etudiant": {
        "adresse": "Agoe",
        "id": 2,
        "nom": "Ali",
        "prenom": "Baba"
    },
    "id": 2,
    "success": true,
    "total_etudiants": 1
}
```
. ##PATCH/plants(plant_id)
  GENERAL:
  This endpoint is used to update a primary_color of plant
  We return a plant which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/plants/1 -H "Content-Type:application/json" -d "{"primary_color":"yellow"}"
  ```
  ```
    {
      "id": 1,
      "primary_color": "yellow",
      "success": true
    }
    ```

. ## POST/plants

    GENERAL:    
    This endpoint is used to create a new plant or to search for a plant in relation to the terms contained in the plants.
    When the searchTerm parameter is passed from the json, the endpoint performs the search. Otherwise, it is the creation of a new question.
    In the case of the creation of a new question:
    We return the ID of the new plant created, the plant that was created, the list of plant and the number of plants.

    SAMPLE.....For Search:
    ```
    curl -X POST http://localhost:5000/plants -H "Content-Type:application/json" -d "{"search":"title"}"
    ```

                

    SAMPLE.....For create

    curl -X POST http://localhost:5000/plants -H "Content-Type:application/json" -d "{"name":"Gnato","scientific_name":"Pimento","is_poisonous":false,"state":"Togo","primary_color="Blue"}"
```
    {
    "created": 58,
    "plants": [
        {
            "id": 1,
            "is_poisonous": false,
            "name": "Gnato",
            "primary_color": "Blue",
            "scientific_name": "Gnato Togo",
            "state": "TOGO"
        },
        {
            "id": 2,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 3,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 4,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 5,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 6,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 7,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 8,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 9,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 11,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        }
    ],
    "success": true,
    "totals_plants": 54
}
```      


## Testing
To run the tests, run
```
dropdb plants_database
createdb plants_database
psql plants_database_test < plants_database.sql
python test_flaskr.py
```