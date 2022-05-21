API for vehicles using Django-Rest-Framework, PostgreSQL and Docker.
Have methods GET, POST, PATCH, and DELETE using a bearer token for authorization.

## Installation

Clone the project and install local or using docker.

### Local

Using poetry to use python3.9.5 version and activate virtual environment.

```bash
poetry env use python3.9.5
poetry shell
poetry install
```

### Docker

Exec docker compose and go to http://127.0.0.1:8000

```bash
docker compose build
docker compose up -d

docker exec -it <container_id> bash
python manage.py createsuperuser
```

## Tests

Try to share the requests from postman.

https://www.postman.com/galactic-sunset-507592/workspace/orbitec-vehicle-api

### Endpoints

#### Get user token

```bash
POST /api/token/ { "username": "", "password": "" }
```

#### List, create, update, and delete vehicles

```bash
GET /vehicles/
POST /vehicles/ {
    "name": "",
    "alias": "",
    "company": "",
    "vehicle_type": "",
    "gps_id": ""
}

GET /vehicles/<id> 
PATCH /vehicles/<id> { "field_to_update": "" }
DELETE /vehicles/<id>
```
