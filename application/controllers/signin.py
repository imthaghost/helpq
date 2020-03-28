from flask import session, render_template, request, redirect, Blueprint

login = Blueprint('login', __name__, static_folder='static')


@login.route('/login', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('login.html')
