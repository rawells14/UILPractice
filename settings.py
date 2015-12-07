SERVER_NAME = 'UILPractice.com'
DEBUG = True
SECRET_KEY = '123'
USE_RELOADER = True

# W for windows, L for linux
OS = 'L'

sqlite_database = 'sqlite:///' + 'data.db'
mysql_database = 'mysql://root:ryan@localhost/uilpractice'
DB_ADDRESS = sqlite_database
PROJECT_PATH = ''
if OS == 'L':
    DB_ADDRESS = mysql_database
    PROJECT_PATH = '/var/www/FlaskApp/FlaskApp/'
