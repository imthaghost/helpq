from flask import session, render_template, request, redirect, Blueprint, url_for
import bcrypt
import application

login = Blueprint('login', __name__)


@login.route('/login', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return redirect(url_for('q.root'))
        else:
            return render_template('login.html')
    if request.method == 'POST':
        if 'user' in session:
            return redirect(url_for('q.root'))
        else:
            credentials = request.form
            email = credentials.get('email')
            password = credentials.get('password')
            # if we find a user in the database return that user exists and redirect the client to the register form with an error message
            # todo: make sure to sanitize unless you want SQL Injection :)
            verify_user = application.user.find_one({'email': email})
            # if the users email is foud in the database and check to see if the password credential matches the encrypted field in the database
            if verify_user is not None:
                if bcrypt.hashpw(password.encode('utf-8'), verify_user['password']) == verify_user['password']:
                    session['user'] = email
                    return redirect(url_for('q.root'))
            else:
                return redirect(url_for('login.root'))
