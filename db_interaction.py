import random
import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

import settings

Base = declarative_base()
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

data_base_address = settings.DB_ADDRESS
engine = create_engine(data_base_address, echo=False)

Session = sessionmaker(bind=engine)


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


class Question(Base):
    __tablename__ = 'questions'
    qid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    questionheader = Column(String(16000))
    questiontext = Column(String(16000))
    answerchoices = Column(String(16000))
    correctanswer = Column(Integer)
    explanation = Column(String(16000))

    def get_qid(self):
        return self.qid

    def __repr__(self):
        return "<Question(qid='%d', questionheader='%s', questiontext='%s', answerchoices='%s', correctanswer='%s', explanation='%d')>" % (
            self.qid,
            self.questiontext,
            self.answerchoices,
            self.correctanswer, self.explanation)


class Submission(Base):
    __tablename__ = 'submissions'

    uid = Column(String(50))
    status = Column(String(50))
    time_stamp = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Submission(username='%s', status='%s', time_stamp='%d')>" % (
            self.username, self.status, self.time_stamp)


def new_submission(uname, status):
    session = Session()
    t = time.time()
    sub = Submission(username=uname, status=status, time_stamp=t)
    session.add(sub)
    session.commit()
    session.close()


def create_user(uname, full, pwd):
    session = Session()
    u = User(username=uname, fullname=full, password=pwd, score=0, totalattempted=0, totalcorrect=0)
    session.add(u)
    session.commit()
    session.close()


def get_all_users():
    session = Session()
    list = session.query(User).order_by(User.score)
    session.close()
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
    session = Session()
    u = session.query(User).filter(User.username == username).first()
    session.close()
    return u


def search_by_username(username):
    session = Session()
    users = session.query(User).filter(User.username.contains(username))
    session.close()
    return users


def get_user_by_uid(uid):
    session = Session()
    uid = int(uid)
    session.close()
    return session.query(User).filter(User.uid == uid).first()


def is_taken(username):
    session = Session()
    q = session.query(User).filter(User.username == username).first()
    session.close()
    return not (q is None)


def is_valid(u, p):
    session = Session()
    username = u
    password = p
    for i in session.query(User).order_by(User.score):
        if i.username == username and i.password == password:
            session.close()
            return True

    session.close()
    return False


def correct_and_total_num(username):
    u = get_user_by_username(username)
    data = []
    data.append(u.totalcorrect)
    data.append(u.totalattempted)
    return data


def incorrect(user):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})


    #
    # u.update(totalattempted=u.totalattempted + 1
    # u.score = round(u.totalcorrect * u.totalcorrect / u.totalattempted)
    session.commit()
    session.close()


def correct(user):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalcorrect: User.totalcorrect + 1})
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})
    session.commit()
    session.close()


def get_random_question():
    session = Session()
    row_count = session.query(Question).count()
    qid = random.randint(1, row_count)
    question = session.query(Question).filter(Question.qid == qid).first()
    session.close()
    return question


def get_question_by_qid(qid):
    session = Session()
    question = session.query(Question).filter(Question.qid == qid).first()
    session.close()
    return question


def add_question(questionheader, questiontext, answerchoices, correctanswer, explanation):
    session = Session()
    question = Question(questionheader=questionheader, questiontext=questiontext, answerchoices=answerchoices,
                        correctanswer=correctanswer, explanation=explanation)
    session.add(question)
    session.commit()
    session.close()


def update_question(questionid, questionheader, questiontext, answerchoices, correctanswer, explanation):
    session = Session()
    session.query(Question).filter(Question.qid == questionid).update({Question.questionheader: questionheader})
    session.query(Question).filter(Question.qid == questionid).update({Question.questiontext: questiontext})
    session.query(Question).filter(Question.qid == questionid).update({Question.answerchoices: answerchoices})
    session.query(Question).filter(Question.qid == questionid).update({Question.correctanswer: correctanswer})
    session.query(Question).filter(Question.qid == questionid).update({Question.explanation: explanation})
    session.commit()
    session.close()


Base.metadata.create_all(engine)
