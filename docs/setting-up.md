# Install

At first install Django:

    sudo pip3 install django

# Create a Project

Whether you are on Windows or Linux, just get a terminal or a cmd prompt and navigate to the place you want your project to be created, then use this code:

    django-admin startproject myproject

# The Project Structure

The 'myproject' directory is just your project container, it actually contains two elements:

- manage.py − This file is kind of your project local django-admin for interacting with your project via command line (start the development server, sync db...). 

To get a full list of command accessible via manage.py you can use the code:

    python manage.py help

The `myproject` subdirectory is the actual python package of your project. It contains four files:

- `__init__.py` - Just for python, treat this folder as package.
- `settings.py` - As the name indicates, your project settings.
- `urls.py` - All links of your project and the function to call. A kind -of ToC of your project.
- `wsgi.py` - If you need to deploy your project over WSGI.

# Setting Up

Your project is set up in the SUBDIRECTORY `myproject/settings.py`. Some important options:

    DEBUG = True

This option lets you set if your project is in debug mode or not. Do it only in the development mode.

    DATABASES = {
       'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': 'database.sql',
          'USER': '',
          'PASSWORD': '',
          'HOST': '',
          'PORT': '',
       }
    }

Database is set in the `Database` dictionary. The example is for SQLite engine. Django also supports:

- MySQL (django.db.backends.mysql)
- PostGreSQL (django.db.backends.postgresql_psycopg2)
- Oracle (django.db.backends.oracle) and NoSQL DB
- MongoDB (django_mongodb_engine)

# Secure the secret key

Take a `SECRET_KEY` from `settings.py` and use below command to write it into file:

    echo 'secret_key' > secret_key.txt

And then use:

    # SECURITY WARNING: keep the secret key used in production secret!
    with open('secret_key.txt','r') as f:
        SECRET_KEY = f.read().strip() 

In `settings.py`.

# Secure /admin

In `urls.py` change the default path to `/admin`:

    urlpatterns = [
        #path('admin/', admin.site.urls),
        path('appstaff/', admin.site.urls),
    ]

Also it is a good practice to keep log of what IPs a trying to enter `/admin`.

# Check if project is working

Run below command to start server:

    python3 manage.py runserver

