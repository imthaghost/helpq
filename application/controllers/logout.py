from flask import session, redirect, url_for, Blueprint, request

out = Blueprint('logout', __name__, static_folder='static')


@out.route('/logout', methods=['GET'])
def root():
    if request.method == 'GET':
        session.clear()
        return redirect(url_for('index.root'))
