Use this to quickstart flask apps. You can copy or here are my steps.

Set up a virtual environment:
`python -m venv .venv`

Activate using
`source .venv/Scripts/activate`

Grab what you need to start (Flask and python-dotenv)
`pip install -r requirements.txt`

Create source folder, static (CSS), templates (HMTL)

Create __init__.py
```
from flask import Flask, render_template

app = Flask(__name__)
```

Create env files

`.flaskenv` is used to set your flask environment and call the flask app. 
**Note I put the code into a source folder, therefore you have to have an __init__.py file. Then all you have to do in `.flaskenv` is call the folder.** 
```
FLASK_APP=source
FLASK_ENV=development
```
.env.example
 Add your MongoDB URI below.
 Make sure to replace:
- mongodb_user for your database user
- mongodb_password for your user's password
- 127.0.0.1 for your server's hostname
- 27017 for your server's port number
- default_database for the database name you're connecting to

`MONGODB_URI=mongodb://mongodb_user:mongodb_password/127.0.0.1:27017/default_database`

.gitignore
[Boilerplate gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

Deploying to Heroku
check requirements.txt and add gunicorn
Procfile: `web: gunicorn "<source_folder>:create_app()"`
runtime.txt: `python-3.10.3`

If you need to restart/troubleshoot you can remove the venv and restart one.
`deactivate`
`rm -rf .venv`
restart: `python -m venv .venv`

Production example:
`https://movie-watchlist-flask-tap.herokuapp.com/`
