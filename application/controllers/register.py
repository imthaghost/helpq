from flask import session, render_template, request, redirect, Blueprint

signup = Blueprint('register', __name__)


@signup.route('/register', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('register.html')
