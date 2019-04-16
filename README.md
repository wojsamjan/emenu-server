# eMenu API

## Requirements
Python, PIP, virtualenv

[Install PostgreSQL](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)

Run PostgreSQL:
```psql```

Create emenu user:
```CREATE USER emenu;```

Set privilege to create db (for running tests):
```ALTER USER emenu CREATEDB;```

Create emenudb by our user:
```CREATE DATABASE emenudb OWNER emenu;```


## Installation
```
virtualenv --python=python3 venv
source venv/bin/activate
git clone git@github.com:wojsamjan/emenu-server.git
cd emenu-server
pip install -r requirements.txt
```


## Migrations and seeding DB
```
python manage.py migrate --settings=emenu.local_settings
python manage.py loaddata meals
python manage.py loaddata menus
```


## Creating superuser (for Django Admin)
```
python manage.py createsuperuser
```


## Running tests
#### [Hint] Look at our code test coverage (external libs are not a subject of our tests)
```
coverage run manage.py test menus -v 2 --settings=emenu.local_settings
coverage report
```

or

```coverage html```


## Test coverage
[Coverage result](https://github.com/wojsamjan/emenu-server/blob/master/eMenu_coverage.png)


## Running project
```
python manage.py runserver --settings=emenu.local_settings
```


## Description
SECRET_KEY and DB credentials are set separately for both development and production environments

[React App for this API](https://github.com/wojsamjan/emenu-client)

## Implementation

This project is implemented using Django REST Framework, PostgreSQL
