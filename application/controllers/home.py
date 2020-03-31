from flask import session, render_template, request, redirect, Blueprint, url_for

home = Blueprint('index', __name__, static_folder='static')


@home.route('/', methods=['GET', 'POST'])
@home.route('/index', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        if 'user' in session:
            return render_template('index.html')
        else:
            return redirect(url_for('login.root'))
    if request.method == 'POST':
        if 'user' in session:
            data = request.form
            description = data.get('task-description')
            print(description)
            return render_template('index.html')
        else:
            return redirect(url_for('login.root'))


# given an array of numbers find duplicates


# qs
# will the array have all integers
# no negatives
arr = [1, 2, 3, 4, 7, 8, 7]
# unsorted

# assumption:


def find_duplicates(arr):

    for i in range(len(arr)):
        j = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                return i, j
            j += 1


print(find_duplicates(arr))
