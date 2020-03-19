# Pollster Application

This application is allows creation of various polls that could be managed by the admin and filled in by others to vote in the polls. This app uses SQLite databse that is the default for django.

## Creating python pip environment

`pip install pipenv` - install pipenv to be able to create environments \
`pipenv shell` - enter the virtual environment \
`pipenv install django` - installs django in the virtual env

## Create the project

`django-admin startproject pollster` - create a project called pollster

## Running the app

To run server: \
`python manage.py runserver 8081`
`python manage.py migrate` (default django tables for the databse)

To start an app:
`python manage.py startapp polls`

## VScode pipenv instructions

If using VSCode give directions to the pipenv and virtualenv in `settings.json` file of workspaces settings:\
`{"python.pipenvPath":"/Users/<user_name>/opt/anaconda3/bin/pipenv", "python.venvPath":"/Users/<user_name>/.local/share/virtualenvs/", "python.pythonPath":"/Users/<user_name>/.local/share/virtualenvs/pollster_project-zQxwDZAu/bin/python"}`

In order to find out where pipenv is installed run `which pipenv`
In order to find out where the virtual environments are installed run `pipenv --py`

## Pylint not finding "module"

Overcome the problem of not finding element module using pylint, run the following command:
`pipenv install pylint-django`, then create a file called `.pylintrc` in root directory and insert `load-plugins=pylint-django`

## Create migration after creating the models

Create migration:
`python manage.py makemigrations polls`
`python manage.py migrate`

## Manipulate data within the shell

`python manage.py shell`\
`from polls.models import Question, Choice`\
`from django.utils import timezone`\
`Question.objects.all()`\
`q = Question(question_text='What is your favourite python framework?'`\
`pub_date=timezone.now)`\
`q.save()`\
`Question.objects.filter(id=1)`
`Questions.objects.filter(pk=1)`\
`q = Question.objects.get(pk=1)`\
`q.choice_set.all()`\
`q.choice_set.create(choice_text="Django", votes=3)`\
`q.choice_set.create(choice_text="Flask", votes=2)`\
`q.choice_set.create(choice_text="Web2Py", votes=1)`\
`q.choice_set.all()`

## Create a project admin

`python manage.py createsuperuser` \
username: admin \
email address: example@gmail.com \
password: 123456

## Run the application on localhost

`python manage.py runserver`
