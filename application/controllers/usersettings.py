from flask import session, render_template, request, redirect, Blueprint, url_for

settings = Blueprint('settings', __name__, static_folder='static')


@settings.route('/edit', methods=['GET'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('settings.html')
        else:
            return redirect(url_for('register.root'))
