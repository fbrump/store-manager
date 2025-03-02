# Backend

On this section, I will describe process related to the backend application.

# How to

## Run

First, we need to execute the environment.

```bash

poetry shell

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