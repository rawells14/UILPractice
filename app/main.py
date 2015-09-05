from flask import Flask, request, url_for
from flask import render_template
from werkzeug.utils import redirect

from app.db_interaction import create_user, get_all_users


app = Flask(__name__)


@app.route('/', methods =['GET'])
def home():
    return render_template('homepage.html', users=get_all_users())


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ''
    # create_user('rwells', 'Ryan Wells', 'dank', 100)
    if (request.method == 'POST'):
        username = [request.form['uname']]
        fullname = [request.form['fname']]
        password = [request.form['pwd']]
        create_user(username[0], fullname[0], password[0], 0)
        return redirect(url_for('home'))
    else:
        return render_template('signup.html', error=error)


if __name__ == '__main__':
    app.debug = True;
    app.run()


