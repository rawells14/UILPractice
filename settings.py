SERVER_NAME = 'UILPractice.com'
DEBUG = True
SECRET_KEY = '123'
USE_RELOADER = False

# W for windows, L for linux
OS = 'W'

sqlite_database = 'sqlite:///' + 'data.db'
mysql_database = 'mysql://root:ryan@localhost/uilpractice'
DB_ADDRESS = sqlite_database
PROJECT_PATH = ''
if OS == 'L':
    DEBUG = False
    DB_ADDRESS = mysql_database
    PROJECT_PATH = '/var/www/FlaskApp/FlaskApp/'
