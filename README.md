# Cheddar Gorge
[![Build Status](https://travis-ci.org/SteveWooding/cheddar-gorge.svg?branch=master)](https://travis-ci.org/SteveWooding/cheddar-gorge)
[![Coverage Status](https://coveralls.io/repos/github/SteveWooding/cheddar-gorge/badge.svg?branch=master)](https://coveralls.io/github/SteveWooding/cheddar-gorge?branch=master)

An online version of Cheddar Gorge - a word relay game.

## About
This is a web-based version of the game
[Cheddar Gorge](https://en.wikipedia.org/wiki/List_of_games_on_I%27m_Sorry_I_Haven%27t_a_Clue#Cheddar_Gorge)
as played on the BBC Radio 4 programme
[I'm Sorry I Haven't A Clue](https://en.wikipedia.org/wiki/I%27m_Sorry_I_Haven%27t_a_Clue). It does
differ significantly,
but players still take it in turn to add words to the current story. No players are eliminated, as
in the original game. The goal of this version is to hopefully produce some amusing stories that are
created by two or more people. After a story has at least 64 words, you can choose to start a new
story.

## Required libraries and dependencies
This project is written in Python and the Django web framework. It is setup to use the PostgreSQL
database, though this could be swapped out for another database that Django supports. The major
version numbers for the required software are:

* Python 3.6.5
* Django 2.0.6
* PostgreSQL 10.4

You may be able to use previous versions of Python 3 and PostgreSQL. However, this project is
strictly Django 2 and above.

The project uses Pipenv to manage the required Python packages for production and development
environments. Pipenv can be installed with `pip` like this:

```
pip install --user pipenv
```

To install the tested versions of the Python packages in a production environment, run the command:

```
pipenv install --ignore-pipfile
```

If you want to install the packages in a development environment and include the development
packages, run the command:


```
pipenv install --dev
```

Learn more about Pipenv in the article
[Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/#pipenv-introduction).

## Project contents
The project follows a standard Django file layout, as shown below:

```
├── cheddargorge
│   ├── cheddargorge
│   │   ├── forms.py                            # Contains user creation form
│   │   ├── __init__.py
│   │   ├── settings.py                         # Main Django settings file
│   │   ├── tests.py                            # Tests for user sign-up and deletion
│   │   ├── urls.py                             # Main URL routes
│   │   ├── views.py                            # Contains sign-up and account deletion views
│   │   └── wsgi.py                             # WSGI configuration file
│   ├── manage.py                               # Main Django project management Python script
│   ├── sent_emails                             # Directory for sent emails in development mode
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap-sketchy.min.css       # Sketchy Bootstrap 4 theme
│   │   │   └── style.css                       # Custom CSS styles
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery-3.2.1.slim.min.js
│   │       └── popper.min.js
│   ├── templates                               # Contains base and user account templates
│   │   ├── base.html
│   │   └── registration
│   │       ├── delete.html                     # Account deletion confirmation page
│   │       ├── login.html
│   │       ├── password_change_done.html
│   │       ├── password_change_form.html
│   │       ├── password_reset_complete.html    # Page shown after completing a password reset
│   │       ├── password_reset_confirm.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_form.html
│   │       └── signup.html
│   └── wordrelaygame
│       ├── admin.py                            # Admin settings for the Story and Word models
│       ├── apps.py                             # Sets up the app name
│       ├── bannedwords.py                      # List of words that are not accepted
│       ├── forms.py                            # New word form
│       ├── __init__.py
│       ├── migrations                          # Contains database migration scripts
│       ├── models.py                           # Story and Word model definitions
│       ├── templates
│       │   └── wordrelaygame
│       │       ├── home.html                   # HTML template for main homepage
│       │       ├── _new_story_form.html        # HTML fragment of new story form
│       │       └── story_list.html             # HTML template for story archive page
│       ├── tests.py                            # Tests for wordrelaygame app
│       ├── urls.py                             # URL route definitions
│       └── views.py                            # Views for homepage, adding a word, archive, etc.
├── LICENSE
├── Pipfile                                     # Main Pipenv configuration file
└── Pipfile.lock                                # Pipenv conf file that specifies concrete package versions
```

## Database setup
By default, the project is set to use the PostgreSQL database, so this needs to be installed on your
machine.

Create a database with the following parameters:

* Database name: cheddargorge
* Database user: cheddargorge
* Database user password: cheddargorge

The `cheddargorge` database should be owned by the `cheddargorge` user. In order to run the tests,
make sure the `cheddargorge` user has permission to create new databases, as a test database is
created by the Django test suite.

On Linux, the following commands would be run:

```
sudo -u postgres psql -c "create user cheddargorge with createdb password 'cheddargorge';"
sudo -u postgres psql -c "create database cheddargorge owner cheddargorge;"
```

In a production deployment, remove the `createdb` option from the first command.

## How to run the project
Download or clone the repository and navigate to the root of the project. Run the `pipenv` command,
as discussed previously, to install the Python packages.

Next, enter the Python virtual environment using the command:

```
pipenv shell
```

Then change to the `cheddargorge` directory and run the server:

```
cd cheddargorge
python manage.py runserver
```

## How to run the test suite
Use the following command to run the tests:

```
python manage.py test
```

To get a code coverage report, run the tests through the `coverage` command and generate a coverage
report with:

```
coverage run --source='.' manage.py test
coverage report -m
```

## How to contribute
All pull requests and issue submissions are welcome and will be considered. Bug reports are
especially welcome.
