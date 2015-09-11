from flask import Flask, request, url_for, flash
from flask import render_template
from werkzeug.utils import redirect

from app.db_interaction import create_user, get_all_users, is_taken

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html', users=get_all_users())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    if (request.method == 'POST'):
        username = [request.form['uname']]
        fullname = [request.form['fname']]
        password = [request.form['pwd']]
        if is_taken(username):
            error = 'Username is already taken, You\'ll have to pick a new one'
            return render_template('signup.html', error=error)
        else:
            create_user(username[0], fullname[0], password[0], 0)
            message = 'Account Successfully Created!'
            flash(message)
            return redirect(url_for('home'))
    else:
        return render_template('signup.html', error=error)


if __name__ == '__main__':
    app.debug = True;
    app.run()
