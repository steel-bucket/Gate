# Gate

A Gate Entry app.

## Requirements

* Python: 3.9 and above

## Technologies Used
* DJango 4.26 as MVC Backend
* DJangoRestFramework as API
* PostgreSQL and railway.app as DB

## How to run it?

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

## Contributing

* Create a new branch with a related name of the motive. Branch name should follow these conventions.
    - `feature/*` if you're implementing a new feature or adding some new functionality.
    - `refactor/*` if you're refactoring code or upgrading anything.
    - `bug/*` if you've fixed a bug that's not deployed onto Production yet.
    - `hotfix/*` if you've fixed a bug that is deployed and/or causing problems in Production.
    - Note: DON'T push to `master` or `release` branch.
* Use an IDE linter, like **SonarLint**, to fix common bugs/code quality issues.
* Update your task's status in the provided spreadsheet.
