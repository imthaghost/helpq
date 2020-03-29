# external Python Modules
from flask import session, render_template, request, redirect, Blueprint, url_for

# local Python Modules
from application.models.user import User

signup = Blueprint('register', __name__)


@signup.route('/register', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('index.root'))
        else:
            return render_template('register.html')
    if request.method == 'POST':
        credentials = request.form
        email = credentials.get('email')
        pw = credentials.get('password')
        # if we find a user in the database return that user exists and redirect the client to the register form with an error message
        if application.user.find_one({"email": email}):
            # change to login later
            return redirect(url_for('register.root'))
        else:
            new_user = User(email=email, password=pw)
            # generate UUID
            new_user.set_uuid()
            new_user.save_new()
            session['user'] = email
            return redirect(url_for('q.root'))
