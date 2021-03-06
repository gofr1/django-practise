# Migrations

The Django Web Framework uses files, called Django migrations, to make modifications to your database schema.  

Django uses Migration functionality to propagate changes to a model into the given database. These migrations can be done when a model is created, updated, or deleted.

Django uses a model class to represent a database table, and an instance of that class represents a particular record in that database table. This allows Django to represent database objects as Python objects.

## Migration Commands

Django comes with the following migration commands to interact with the database schema.

- `migrate` - used for applying and removing migrations.
- `makemigrations` - create new migrations based on changes made to models.
- `sqlmigrate` - displays SQL statements for a given migration.
- `showmigrations` - lists projects migrations and their status.

## Simple Django Migration

Create `./app/models.py`

    from django.db import models
    from django.core.validators import MinLengthValidator, MaxValueValidator,     MinValueValidator
    
    class Article(models.Model):
        article_id = models.CharField(primary_key=True, max_length=30, validators=    [MinLengthValidator('5')])
        title = models.CharField(max_length=250)
        text = models.CharField(max_length=4096)
    
        def __str__(self):
            return self.article_id + " - " + self.title + " - " +self.text

Now in terminal run:

    >>> python3 manage.py check
    System check identified no issues (0 silenced).
    
    >>> python3 manage.py makemigrations app
    Migrations for 'app':
      app/migrations/0001_initial.py
        - Create model Article

Let's ckeck `0001_initial.py`:

    # Generated by Django 3.1.7 on 2021-04-04 08:16
    
    import django.core.validators
    from django.db import migrations, models


    class Migration(migrations.Migration):
    
        initial = True
    
        dependencies = [
        ]
    
        operations = [
            migrations.CreateModel(
                name='Article',
                fields=[
                    ('article_id', models.CharField(max_length=30,     primary_key=True, serialize=False, validators=[django.    core.validators.MinLengthValidator('5')])),
                    ('title', models.CharField(max_length=250)),
                    ('text', models.CharField(max_length=4096)),
                ],
            ),
        ]

Also we can get SQL script:

    >>> python3 manage.py sqlmigrate app 0001_initial
    BEGIN;
    --
    -- Create model Article
    --
    CREATE TABLE "app_article" ("article_id" varchar(30) NOT NULL PRIMARY     KEY, "title" varchar(250) NOT NULL, "text" varchar(4096) NOT NULL);
    COMMIT;

Finally, we can write the changes to the database using the migrate command. The migrate command is the only function that makes direct changes to the database. Because it is the initial migration of the app, Django will migrate all the necessary administrative models in addition to the user-defined model.

    >>> python3 manage.py migrate
    Operations to perform:
      Apply all migrations: admin, app, auth, contenttypes, post, sessions
    Running migrations:
      Applying app.0001_initial... OK

Let's check `db.sqlite3`:

    >>> import sqlite3
    >>> db = sqlite3.connect('db.sqlite3')
    >>> db.execute("SELECT name FROM sqlite_master WHERE type='table';").    fetchall()
    [('django_migrations',), ('sqlite_sequence',), ('auth_group_permissions',    ), ('auth_user_groups',), ('auth_user_user_permissions',),     ('django_admin_log',), ('django_content_type',), ('auth_permission',),     ('auth_group',), ('auth_user',), ('django_session',), ('post_profile',),     ('post_post',), ('app_article',)]
    >>> 

`app_article` table is onboarded.

## Creating Objects

Utilizing the Django shell, we can create some objects of the Article model. Remember each new object of the Article class is considered a new record in the database. We will create 2 records.

Run `python3 manage.py shell` and then:

    from app.models import Article  
      
    record = Article.objects.create(article_id="A0001",title="Lorem ipsum", text='Lorem ipsum dolor sit amet, ... anim id est laborum. ')  

    record = Article.objects.create(article_id="A0002",title="Sed ut perspiciatis", text='Sed ut perspiciatis, ... repellat. ')

To check records you can use:

    Article.objects.all() 

    Article.objects.all().values()

## Updating objects

    >>>python3 manage.py shell
    Python 3.8.3 (default, May 19 2020, 17:04:53) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: from app.models import Article                                                                        
    
    In [2]: record = Article.objects.get(article_id="A0003")                                                      
    
    In [3]: record.title = 'Hamlet'                                                                               
    
    In [4]: record.save()                                                                                         
    
    In [5]: quit()      