# built-in python modules
import os
# external python modules
from flask import Flask, render_template, redirect, jsonify
from dotenv import load_dotenv
# controllers
from application.controllers.register import signup
from application.controllers.signin import login
from application.controllers.forgot import forgotpassword
from application.controllers.home import home
from application.controllers.googleauth import google

# load enviornment variables
load_dotenv()
# application
app = Flask("helpq", template_folder='templates',
            static_folder='static')
# application configuration from .env file
app.config.from_object(os.getenv('APP_SETTINGS'))
# register routes
app.register_blueprint(signup)  # register route
app.register_blueprint(login)  # login route
app.register_blueprint(forgotpassword)  # forgot password
app.register_blueprint(home)  # home route
app.register_blueprint(google)  # google route
# error handlers
@app.errorhandler(404)
def page_not_found(e):
    # set the 404 status explicitly
    return render_template('404.html'), 404
