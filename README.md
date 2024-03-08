# Gate

A Gate Entry app.

## Requirements

* Python: 3.9 and above

## Technologies Used
* DJango 4.26 as MVC Backend
* DJangoRestFramework as API
* PostgreSQL and railway.app as DB

## How to run server and Set Up a Dev Enviornment?

* Fork the repository.
* Setup Virtual Environment: $ python3 -m venv gate4_venv
    * Activate the Virtual Environment:
      On Windows: $ gate4_venv\Scripts\activate
      On macOS and Linux: $ source gate4_venv/bin/activate
* Clone The Project: $ git clone https://github.com/steel-bucket/Gate
* cd Gate
* Add a reference to the original repository `$ git remote add upstream https://github.com/steel-bucket/Gate.git`
* Install Dependencies: pip install -r requirements.txt
* Make migrations `$ python manage.py makemigrations`
* Migrate the changes to the database `$ python manage.py migrate`
* Run the server `$ python manage.py runserver`
* Create admin `$ python manage.py createsuperuser`
* Create tables `$ python manage.py migrate --run-syncdb`


