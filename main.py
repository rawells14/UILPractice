from flask import Flask, request, url_for, flash, g
from flask import render_template
from markupsafe import Markup
from werkzeug.utils import redirect
from flask_login import LoginManager, login_required, logout_user, login_user, current_user

from db_interaction import *
from feedback import *
import settings

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'
login_manager.login_message = 'Please log in to view this'
login_manager.login_message_category = 'error'


@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(uid):
    return get_user_by_uid(uid)


@app.route('/', methods=['GET'])
def home():
    error = ''
    if current_user.is_active:
        return redirect(url_for('dashboard'))
    return render_template('homepage.html')


@app.route('/signup', methods=['POST'])
def signup():
    error = ''
    if request.method == 'POST':
        username = [request.form['uname']][0]
        fullname = [request.form['fname']][0]
        password = [request.form['pwd']][0]
        if is_taken(username):
            error = 'Username is already taken, You\'ll have to pick a new one'
        elif (len(username) < 4) or (' ' in username):
            error = 'Usernames must be at least 4 characters in length and contain no spaces'
        else:
            create_user(username, fullname, password)
            message = 'Account Successfully Created!'
            flash(message, 'success')
            return redirect(url_for('home'))
        flash(error, 'error')
        return render_template('homepage.html')

    else:
        return render_template('homepage.html', error=error)


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
@login_required
def dashboard():
    rank = compute_rank(current_user)
    data = correct_and_total_num(current_user.username)
    return render_template('dashboard.html', number_correct=data[0], number_attempted=data[1], rank=rank)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    users_found = []
    if request.method == 'POST':
        uname = [request.form['uname']][0]
        users_found = search_by_username(uname)
        if users_found.count() > 0:
            flash(str(users_found.count()) + ' users were found', 'success')
        else:
            flash(Markup('<strong>0</strong> users were found'), 'error')
        return render_template("search.html", users_found=users_found)
    else:
        return render_template("search.html")


@app.route('/user/<username>', methods=['GET'])
@login_required
def profile(username):
    user_prof = get_user_by_username(username)
    rank = compute_rank(user_prof)
    return render_template('profile.html', user=user_prof, rank=rank)


@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    return render_template('leaderboard.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html')
    if request.method == 'POST':
        name = [request.form['name']][0]
        message = [request.form['message']][0]
        new_feedback(name, message)
        flash('Feedback Submitted', 'success')
        return redirect(url_for('home'))


# Computer Science Methods:
@app.route('/cs', methods=['GET'])
def cs():
    return render_template('cs.html')


@app.route('/cs/new', methods=['GET', 'POST'])
def cs_question():
    question = get_random_question()
    return redirect('/cs/question/' + (str)(question.qid))


@app.route('/cs/question/<qid>', methods=['GET', 'POST'])
def cs_question_specific(qid):
    question = get_question_by_qid(qid)
    question.explanation = (str)(question.explanation)
    return render_template('question.html', question=question)


# Submit API
@app.route('/cs/submit', methods=['POST'])
def cs_submit():
    isCor = [request.form['isCor']][0]
    if isCor == 'true':
        correct(current_user)
        return 'Question accounted as correct'
    if isCor == 'false':
        incorrect(current_user)
        print('incorrect')
        return 'Question accounted as incorrect'
    return 'Question not accounted for'


@app.route('/math', methods=['GET'])
def math():
    return render_template('math.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not current_user.is_authenticated or not current_user.username == 'admin':
        flash('You are not allowed here', 'error')
        return redirect(url_for('home'))
    if request.method == 'POST':
        questionheader = [request.form['questionheader']][0]
        questiontext = [request.form['questiontext']][0]
        answerchoices = [request.form['answerchoices']][0]
        correctanswer = [request.form['correctanswer']][0]
        explanation = [request.form['explanation']][0]
        questionid = [request.form['questionid']][0]
        if questionid == '':
            add_question(questionheader, questiontext, answerchoices, (int)(correctanswer), (str)(explanation))
        else:
            update_question(questionid, questionheader, questiontext, answerchoices, (int)(correctanswer),
                            (str)(explanation))
        flash('Added New Question!', 'success')
        return render_template('admin.html')
    return render_template('admin.html')


if __name__ == '__main__':
    app.debug = settings.DEBUG
    app.run(use_reloader=settings.USE_RELOADER)
