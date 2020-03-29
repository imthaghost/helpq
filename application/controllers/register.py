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
        email = request.form.get('email')
        pw = request.form.get('password')
        new_user = User(email=email, password=pw)
        # generate UUID
        new_user.set_uuid()
        new_user.save_new()
        session['user'] = email
        return redirect(url_for('q.root'))
