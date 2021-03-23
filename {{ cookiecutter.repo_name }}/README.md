# {{ cookiecutter.project_title }}

> {{ cookiecutter.project_description }}

## Overview

This demo project uses the following technologies to demonstrate a basic RESTful API:

* PyEnv
* Poetry
* Django
* Django REST Framework
* SQLite

This way only python needs to be configured (i.e. there's no need for
Docker/Docker Compose).

> :mega: Please note that I am big fan of Docker, Docker Compose and Postgres
> but in the context of this very basic demo it doesn't make sense to add them
> into the mix.

## Getting started

For macOS and Linux please execute the following command
(sorry, MS Windows is not supported):

```shell
./bin/bootstrap
```

The above script does the following:

* installs pyenv
* installs the projects required version of python
* installs poetry
* installs the project requirements
* runs the project migrations

Please feel free to take a look at the [source](bin/bootstrap).

### Virtual Environment
To activate the virtual environment created by poetry in the bootstrap script please
run the following command.

```shell
source .venv/bin/activate
```

Then you're free to run any of the commands made available by the installed python
packages. E.g.

```shell
python manage.py test
# or
python manage.py runserver
# or
python manage.py startapp <insert app name>
```

You can run also run commands using the Poetry interface, e.g.:

```shell
poety run python manage.py test
# or
poetry run python manage.py runserver
# or
poetry run python manage.py startapp <insert app name>
```

### Adding Dependencies

Given that this project uses Poetry you will be required to follow the

#### Production Deps
```shell
poetry add <package-name>...
```

#### Dev Deps
```shell
poetry add -D <package-name>...
```

### Adding Apps

After you've set up your environment, adding apps can be done using the
following command.

```shell
./bin/startapp <insert app name>
```

The above runs a simple script that wraps Django's `startapp` management command.
It targets a custom app template that can be found [here](templates/apps).
To read more about the `startapp` command please refer to the Django
[docs](https://docs.djangoproject.com/en/3.1/ref/django-admin/#startapp).

After creating the app, you will need to installed packages in settings module,
as well as adding migrations as per a regular Django project.

```
# in {{ cookiecutter.project_name }}.settings
INSTALLED_APPS = [
    ...,
    "{{ cookiecutter.project_name }}.test_app.apps.TestAppConfig",
]

# in {{ cookiecutter.project_name }}.urls
urlpatterns = [
    ...,
    path('test-app/', include('{{ cookiecutter.project_name }}.test_app.urls')),
]
```

```shell
python manage.py makemigrations
python manage.py migrate
pyhton manage.py runserver
```
### Test Factories

This project utilizes `factory-boy` to generate model instances. You can read more
about it [here](https://factoryboy.readthedocs.io/en/stable/). Below is an
example of how to structure a factory off of a Django model.

```python
from factory import Faker
from factory.django import DjangoModelFactory
from django.conf import settings


class UserFactory(DjangoModelFactory):

    email = Faker("email")

    is_superuser = False
    is_staff = False

    class Meta:
        model = settings.AUTH_USER_MODEL
```
