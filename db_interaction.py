import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

Base = declarative_base()
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

sqlite_database = 'sqlite:///' + 'data.db'
mysql_database = 'mysql://root:ryan@localhost/uilpractice'
engine = create_engine(mysql_database, echo=False)

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))
    score = Column(Integer)
    totalattempted = Column(Integer)
    totalcorrect = Column(Integer)
    settings = Column(String(1000))

    def __repr__(self):
        return "<User(uid='%d', username='%s', fullname='%s', password='%s', score='%d')>" % (self.uid,
                                                                                              self.username,
                                                                                              self.fullname,
                                                                                              self.password, self.score)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.uid


class Submission(Base):
    __tablename__ = 'submissions'

    uid = Column(String(50))
    status = Column(String(50))
    time_stamp = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Submission(username='%s', status='%s', time_stamp='%d')>" % (
            self.username, self.status, self.time_stamp)


def new_submission(uname, status):
    t = time.time()
    sub = Submission(username=uname, status=status, time_stamp=t)
    session.add(sub)
    session.commit()


def create_user(uname, full, pwd):
    u = User(username=uname, fullname=full, password=pwd, score=0, totalattempted=0, totalcorrect=0)
    session.add(u)
    session.commit()


def get_all_users():
    list = session.query(User).order_by(User.score)
    return list


def compute_rank(user):
    users = get_all_users()
    rank = -1
    values = []
    value = 0
    for i in users:
        if i.username == user.username:
            value = i.score
        values.append(i.score)
    values.reverse()
    for i in range(len(values)):
        if values[i] == value:
            return i + 1

    return rank


def get_user_by_username(username):
    return session.query(User).filter(User.username == username).first()


def search_by_username(username):
    users = session.query(User).filter(User.username.contains(username))
    return users


def get_user_by_uid(uid):
    return session.query(User).filter(User.uid == uid).first()


def is_taken(u):
    q = session.query(User).filter_by(username=u).first()
    return not (q is None)


def is_valid(u, p):
    username = u
    password = p
    for i in session.query(User).order_by(User.score):
        if i.username == username and i.password == password:
            return True
    return False


def correct_and_total_num(username):
    u = get_user_by_username(username)
    data = []
    data.append(u.totalcorrect)
    data.append(u.totalattempted)
    return data


def incorrect(username):
    u = get_user_by_username(username)
    u.totalattempted += 1
    u.score = round(u.totalcorrect * u.totalcorrect / u.totalattempted)
    session.commit()


def correct(username):
    u = get_user_by_username(username)
    u.totalattempted += 1
    u.totalcorrect += 1
    u.score = round(u.totalcorrect * u.totalcorrect / u.totalattempted)
    session.commit()


Base.metadata.create_all(engine)
