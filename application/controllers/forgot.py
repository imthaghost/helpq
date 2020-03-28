from flask import session, render_template, request, redirect, Blueprint

forgotpassword = Blueprint('forgotpassword', __name__, static_folder='static')


@forgotpassword.route('/passwordreset', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('forgotpassword.html')
