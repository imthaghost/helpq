from flask import session, render_template, request, redirect, Blueprint, url_for

q = Blueprint('q', __name__, static_folder='static')


@q.route('/dashboard', methods=['GET'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('index.html')
        else:
            return redirect(url_for('register.root'))
