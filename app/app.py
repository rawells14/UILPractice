from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('homepage.html')


if __name__ == '__main__':
    app.debug = True;
    app.run()
