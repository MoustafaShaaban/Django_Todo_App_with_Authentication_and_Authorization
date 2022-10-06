# Django_Todo_App_with_Authentication_and_Authorization

A project built with Django web framework and Bootstrap

#### What I used:
Django version 4.1.2
Django-Crispy_Forms version 1.14.0
Django Class based views with Create, Read, Update and Delete (CRUD) functionalities.
Django Authentication and Authorization with an extended User Model.
UI components from the official Bootstrap 4.6 website documentation.


To get started with the project:

1- Clone the repository: git clone '[https://github.com/MoustafaShaaban/Django_Todo_App_with_Authentication_and_Authorization.git](https://github.com/MoustafaShaaban/Django_Todo_App_with_Authentication_and_Authorization.git)'

2- Change the directory to the cloned folder and create a virtual environment like venv and activate it.
  
  * Linux:
  * `cd Django_Todo_App_with_Authentication_and_Authorization`
  * `python -m venv venv`
  * `source venv/bin/activate`
  
  * Windows:
  * `cd Django_Todo_App_with_Authentication_and_Authorization`
  * `python -m venv venv`
  * `venv/Scripts/activate`
  
3- Install requirements.txt:
* `python -m pip install -r requirements.txt`

4- Create the database and super user by running the following commands:
* `python manage.py migrate`
* `python manage.py makemigrations users`
* `python manage.py makemigrations tasks`
* `python manage.py migrate`
* `python manage.py createsuperuser`

5- Run the project: 
* `python manage.py runserver`

6- Login using your super user for example an account with user admin at localhost:8000/admin/ to add a few todos, or add todos from the frontend directly.

7- navigate to localhost:8000/ to see the final results

Preview on youtube: [Youtube](https://www.youtube.com/watch?v=3ieGGaWO_J8&list=PLtb0tG6zW4YtsyiseKOZ9DRwrPf6VjrPb&index=1)
