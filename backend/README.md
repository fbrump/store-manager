# Backend

On this section, I will describe the process related to the backend application.

# Introduction

The back-end should be based on [Python](https://www.python.org/). Also, in another version, we could create or test the Rust using [Actix Web](https://actix.rs/).

- [Django Restful](https://www.django-rest-framework.org/) (*Django REST framework is a powerful and flexible toolkit for building Web APIs*) or [FastAPI](https://fastapi.tiangolo.com/) (*FastAPI framework, high performance, easy to learn, fast to code, ready for production*)
- [Poetry](https://python-poetry.org/) - Python packaging and dependency management made easy
- [Podman](https://podman.io/) - Manage containers, pods, and images with Podman. Seamlessly work with containers and Kubernetes from your local environment.

# How to

## Run

First, we need to execute the environment.

```bash

poetry shell

```

Or, execute the command to get the env, then execute it.

```bash

poetry env activate
Creating virtualenv backend-api-vFPet_sk-py3.13 in /home/fbrump/.cache/pypoetry/virtualenvs

```

Then, execute the command to entre on this env.

```bash

source /home/fbrump/.cache/pypoetry/virtualenvs/backend-api-vFPet_sk-py3.13/bin/activatepoetry env active

```

Then, update the env with all dependencies.

```shell

poetry install

```

Next, we can check the location of this env, and set it up on VS Code.

```bash

poetry env info --path

```

## Python

After to set up the environment, we need to execute the command.

```bash

python manageq.py runserver -p 8081

```

# Database

For the database, we just need to execute these commands.

```bash

python manageq.py makemigrations

```
Then, update on the database.

```bash

python manageq.py migrate

```

# Create Admin User

So, to create a super user on the admin.

```bash

python manage.py createsuperuser --username admin@storage --email admin@storage.com

```

An example of password:

```
0scNV`6Q160oY1bS0|NWJ._v\
```
