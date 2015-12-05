from flask import Flask, request, url_for, flash, g
from flask import render_template
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from werkzeug.utils import redirect

from db_interaction import create_user, get_all_users, is_taken, is_valid, get_user_by_username, search_by_username, \
    correct_and_total_num, compute_rank, correct, get_user_by_uid, incorrect


app = Flask(__name__)
app.secret_key = '123'
login_manager = LoginManager()
login_manager.init_app(app)


@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(uid):
    return get_user_by_uid(uid)


@app.route('/', methods=['GET'])
def home():
    error = ''
    return render_template('homepage.html', users=get_all_users())


@app.route('/signup', methods=['POST'])
def signup():
    error = ''
    if request.method == 'POST':
        username = [request.form['uname']][0]
        fullname = [request.form['fname']][0]
        password = [request.form['pwd']][0]
        if is_taken(username):
            error = 'Username is already taken, You\'ll have to pick a new one'
        if (len(username) < 4) or (' ' in username):
            error = 'Usernames must be at least 4 characters in length and contain no spaces'
        else:
            create_user(username, fullname, password)
            message = 'Account Successfully Created!'
            flash(message, 'success')
            return redirect(url_for('home'))
        flash(error, 'error')
        return render_template('homepage.html', users=get_all_users())

    else:
        return render_template('homepage.html', error=error, users=get_all_users())


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    error = ''
    if request.method == 'POST':
        username = [request.form['uname']][0]
        password = [request.form['pwd']][0]
        if not is_taken(username):
            error = '%s does not exist' % username
            flash(error, 'error')
            return redirect(url_for('home'))
        if not is_valid(username, password):
            error = 'Incorrect Username/Password'
            flash(error, 'error')
            return redirect(url_for('home'))
        else:
            u = get_user_by_username(username)
            login_user(u)
            flash("Successfully Logged In!")
            return redirect(url_for('dashboard'))
    return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if current_user == None or not current_user.is_active or not current_user.is_authenticated:
        return redirect(url_for('signin'))
    correct(current_user)
    rank = compute_rank(current_user)
    data = correct_and_total_num(current_user.username)
    return render_template('dashboard.html', number_correct=data[0], number_attempted=data[1], rank=rank)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    users_found = []
    if request.method == 'POST':
        uname = [request.form['uname']][0]
        users_found = search_by_username(uname)
        incorrect(current_user)
        return render_template("search.html", users_found=users_found)
    else:
        return render_template("search.html")


@app.route('/user/<username>', methods=['GET'])
def profile(username):
    user_prof = get_user_by_username(username)
    rank = compute_rank(user_prof)
    return render_template('profile.html', user=user_prof, rank=rank)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html')


if __name__ == '__main__':
    app.debug = True
    app.run(use_reloader=True)