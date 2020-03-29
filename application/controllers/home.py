from flask import session, render_template, request, redirect, Blueprint, url_for

home = Blueprint('index', __name__, static_folder='static')


@home.route('/', methods=['GET'])
@home.route('/index', methods=['GET'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('index.html')
        else:
            return redirect(url_for('login.root'))
