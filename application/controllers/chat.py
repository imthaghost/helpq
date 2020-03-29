from flask import session, render_template, request, redirect, Blueprint, url_for

message = Blueprint('message', __name__, static_folder='static')


@message.route('/chat', methods=['GET'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('chat.html')
        else:
            return redirect(url_for('register.root'))
