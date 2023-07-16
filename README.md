To run this project, you need the following:

- Python 3.9 or later
- Django 3.2 or later

## Additional Packages

In addition to Python and Django, the following packages are required:

- djangorestframework
- django-rest-framework-simplejwt
- psycopg2 
- pytest
- djangorestframework-simplejwt

## Installation

Install all packages. Change into the project directory(cd project-directory/)
Set up a virtual environment(python -m venv env
source env/bin/activate)
pip install -r requirements
Update the settings.py file with your database credentials.
Configure environment variables:
SECRET_KEY: Secret key for Django app.
Apply database migrations: python manage.py migrate
Start the development server:python manage.py runserver
Run the test suite: python manage.py test
