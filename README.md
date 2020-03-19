`pip install pipenv` - installing the virtual env option
`pipenv shell` - creates a virtual environemnt called "shell"
`pipenv install django` - installs django in the virtual env

This app uses SQLite databse that is default for django.

`django-admin startproject pollster` - create a project called pollster

project - is overall website/application
app - multiple apps (poll app, pages app)

In pollster/pollster:\
`settings.py` is the settings file \
`urls.py` is the routes, with each app having it's own url

To run server: \
`python manage.py runserver 8081`
`python manage.py migrate` - default django tables for the databse

To start an app:
`python manage.py startapp polls`

If using VSCode give directions to the pipenv and virtualenv in `settings.json` file of workspaces settings:\
`{ "python.pipenvPath": "/Users/<user_name>/opt/anaconda3/bin/pipenv", "python.venvPath": "/Users/<user_name>/.local/share/virtualenvs/", "python.pythonPath": "/Users/<user_name>/.local/share/virtualenvs/pollster_project-zQxwDZAu/bin/python" }`

In order to find out where pipenv is installed run `which pipenv`
In order to find out where the virtual environments are installed run `pipenv --py`

Overcome the problem of not finding element module using pylint, run the following command:
`pipenv install pylint-django`, then create a file called `.pylintrc` in root directory and insert `load-plugins=pylint-django`

Create migration:
`python manage.py makemigrations polls`
`python manage.py migrate`

How to manipulate the data within the shell:
`python manage.py shell`
`from polls.models import Question, Choice from django.utils import timezone Question.objects.all() q = Question(question_text='What is your favourite python framework?', pub_date=timezone.now) q.save() Question.objects.filter(id=1) Questions.objects.filter(pk=1) q = Question.objects.get(pk=1) q.choice_set.all() q.choice_set.create(choice_text="Django", votes=3)\ q.choice_set.create(choice_text="Flask", votes=2)\ q.choice_set.create(choice_text="Web2Py", votes=1)\ q.choice_set.all()`

`python manage.py createsuperuser`
username: admin
email address: example@gmail.com
password: 123456

`python manage.py runserver`
