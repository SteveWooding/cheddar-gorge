# Cheddar Gorge
An online version of Cheddar Gorge - a word relay game.

## About
This is a web-based version of the game
[Cheddar Gorge](https://en.wikipedia.org/wiki/List_of_games_on_I%27m_Sorry_I_Haven%27t_a_Clue#Cheddar_Gorge)
as played on the BBC Radio 4 programme
[I'm Sorry I Haven't A Clue](https://en.wikipedia.org/wiki/I%27m_Sorry_I_Haven%27t_a_Clue). It does differ significantly,
but players still take it in turn to add words to the current story. No players are eliminated, as in the original game.
The goal of this version is to hopefully produce some amusing stories that are created by two or more people. After a
story has at least 64 words, you can choose to start a new story.

## Required Libraries and Dependencies
This project is written in Python and the Django web framework. It is setup to use the PostgreSQL database, though this
could be swapped out for another database that Django supports. The major version numbers for the required software are:

* Python 3.6
* Django 2.0.6
* PostgreSQL 10.4

The project uses Pipenv to manage the required Python packages for production and development environments. Pipenv can be
installed with `pip` like this:

```
pip install pipenv
```

To install the tested versions of the Python packages in a production environment, run the command:

```
pipenv install --ignore-pipfile
```

If you want to install the packages in a development environment and include the development packages, run the command:


```
pipenv install --dev
```

Learn more about Pipenv in the article
[Pipenv: A Guide to the New Python Packaging Tool](https://realpython.com/pipenv-guide/#pipenv-introduction).

## Project contents
The project follows a standard Djano file layout, as shown below:

```
├── cheddargorge
│   ├── cheddargorge
│   │   ├── forms.py                            # Contains user creation form
│   │   ├── __init__.py
│   │   ├── settings.py                         # Main Django settings file
│   │   ├── tests.py
│   │   ├── urls.py                             # Main URL routes
│   │   ├── views.py                            # Contains sign-up and account deletion views
│   │   └── wsgi.py
│   ├── manage.py                               # Main Django project management Python script
│   ├── sent_emails                             # Directory for sent emails in development mode
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap-sketchy.min.css       # Sketchy Bootstrap 4 theme
│   │   │   └── style.css
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
│       ├── admin.py
│       ├── apps.py
│       ├── bannedwords.py                      # List of words that are not accepted
│       ├── forms.py
│       ├── __init__.py
│       ├── migrations
│       ├── models.py
│       ├── templates
│       │   └── wordrelaygame
│       │       ├── home.html
│       │       ├── _new_story_form.html
│       │       └── story_list.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── LICENSE
├── Pipfile
└── Pipfile.lock
```
