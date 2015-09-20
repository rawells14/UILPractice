from flask import Flask, request, url_for, flash, session
from flask import render_template
from werkzeug.utils import redirect

from app.db_interaction import create_user, get_all_users, is_taken, is_valid
from app.db_interaction import User

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET'])
def home():
    error = ''
    return render_template('homepage.html', users=get_all_users())


@app.route('/signup', methods=['POST'])
def signup():
    error = ''
    if request.method == 'POST':
        username = [request.form['uname']]
        fullname = [request.form['fname']]
        password = [request.form['pwd']]
        if is_taken(username):
            error = 'Username is already taken, You\'ll have to pick a new one'
            flash(error, 'error')
            return render_template('homepage.html', users=get_all_users())

        else:
            create_user(username[0], fullname[0], password[0], 0)
            message = 'Account Successfully Created!'
            flash(message, 'success')
            return redirect(url_for('home'))
    else:
        return render_template('homepage.html', error=error, users=get_all_users())


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    error = ''
    if request.method == 'POST':
        username = [request.form['uname']]
        password = [request.form['pwd']]
        if not is_taken(username):
            error = '%s does not exist' % username[0]
            flash(error, 'error')
            return redirect(url_for('home'))
        if not is_valid(username, password):
            error = 'Incorrect Username/Password'
            flash(error, 'error')
            return redirect(url_for('home'))
        else:
            session['loggedin'] = True
            return redirect(url_for('dashboard'))

    return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET'])
def dashboard():
    print(session)
    print(session['loggedin'])
    if session['loggedin'] == True:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('signin'))


if __name__ == '__main__':
    app.debug = True

    app.run()
