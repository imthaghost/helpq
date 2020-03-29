# built-in python modules
import os
# external python modules
from flask import Flask, render_template, redirect, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv

# controllers
from application.controllers.register import signup
from application.controllers.signin import login
from application.controllers.forgot import forgotpassword
from application.controllers.home import home
from application.controllers.googleauth import google
from application.controllers.dashboard import q
from application.controllers.logout import out
from application.controllers.chat import message
from application.controllers.usersettings import settings
# load enviornment variables
load_dotenv()
# application
app = Flask("helpq", template_folder='application/templates',
            static_folder='application/static')
# application configuration from .env file
app.config.from_object(os.getenv('APP_SETTINGS'))
# try to set mongo database

# set default mongodb URI
os.environ['MONGO_URI'] = 'mongodb://localhost:27017/helpq'
# set host env
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/helpq')
# MONGO_URI
app.config['MONGO_URI'] = host
# client
client = MongoClient(host=f'{host}?retryWrites=false')
# instantiate and get default db name
db = client.get_default_database()
# user collection
user = db.user
# register routes
app.register_blueprint(signup)  # register route
app.register_blueprint(login)  # login route
app.register_blueprint(forgotpassword)  # forgot password
app.register_blueprint(home)  # home route
app.register_blueprint(google)  # google route
app.register_blueprint(q)  # dashboard route
app.register_blueprint(out)  # logout route
app.register_blueprint(message)  # chat route
app.register_blueprint(settings)  # user settings


# error handlers
@app.errorhandler(404)
def page_not_found(e):
    # set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    # set the 405 status explicitly
    return render_template('405.html'), 405
