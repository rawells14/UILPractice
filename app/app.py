from flask import Flask
from app import routes
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('homepage.html')


@app.route('/math')
def math():
    return 'Practice Math'

@app.route('/cs')
def cs():
    return 'Practice Computer Science'



if __name__ == '__main__':
    app.debug = True;
    app.run()

