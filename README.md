# Django_Todo_App_with_Authentication_and_Authorization

A project built with Django web framework and Bootstrap

###  Project Goals

* Users can register to our website to create todos.

* Users can Create, Read, Update and Delete the todos form the website.

* Once logged in, Users can access a REST API of the our website, which also allows them to use CRUD (Create, Read, Update and Delete) operations.

### Project Functionalities:

* Only logged in users can add todos from the website or the API.

* The list todo page of the website and the API will show only the todos which the logged in user created. Meaning, Only the author of the todo who can perform CRUD operations.

* If one user tried to test URLs to reach another user's todo a 403 Forbidden page is displayed.

* Once logged in Users can access a REST API which has a filtering framework built with django-filter package, which allows the user to filter the todos by their state (completed or not completed).


### Project Preview

* [Youtube](https://www.youtube.com/watch?v=Ux8aDtOjBOY)

### Libraries and Packages used

* [Django Web Framework](https://www.djangoproject.com/)

* [Django Rest Framework](https://www.django-rest-framework.org/) package

* [django-filter](https://github.com/carltongibson/django-filter/tree/main)

* UI components from the official Bootstrap 4.6 website documentation.
-------------------------------------------------------------------------------

### To get started with this project

* Clone the repository: git clone https://github.com/MoustafaShaaban/Django_Todo_App_with_Authentication_and_Authorization.git

* Change directory to backend ``` cd backend ```

* Open the terminal or CMD to create a virtual environment like Python virtual environment (venv) or pipenv and activate it.

    * ``` python -m venv venv ```           *Create the venv*

    * ``` source venv/bin/activate ```      *On Linux*

    * ``` venv/Scripts/activate ```         *On Windows*

    * ``` source venv/Scripts/activate ```  *Git Bash on Windows*

* Install requirements.txt: ``` python -m pip install -r requirements.txt ```

* Change directory to backend ``` cd backend ```

* Create the database by running the following commands:
``` python manage.py makemigrations todos ```
``` python manage.py migrate ```

* Create a super user: ``` python manage.py createsuperuser ```

* Run the project: ``` python manage.py runserver ```
