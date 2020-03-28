from flask import session, render_template, request, redirect, Blueprint

home = Blueprint('index', __name__, static_folder='static')


@home.route('/', methods=['GET', 'POST'])
@home.route('/index', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('index.html')
