import random
import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from werkzeug.security import generate_password_hash, check_password_hash

import settings


Base = declarative_base()
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>

data_base_address = settings.DB_ADDRESS
if settings.OS == 'W':
    engine = create_engine(data_base_address, echo=False)
else:
    engine = create_engine(data_base_address, echo=False, pool_size=20, max_overflow=0, pool_recycle=3600)
# add on to production

Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(1000))
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
    subject = Column(String(250))

    def get_qid(self):
        return self.qid

    def __repr__(self):
        return "<Question(qid='%d', questionheader='%s', questiontext='%s', answerchoices='%s', correctanswer='%s', explanation='%d', subject='%s')>" % (
            self.qid,
            self.questiontext,
            self.answerchoices,
            self.correctanswer, self.explanation, self.subject)


class Submission(Base):
    __tablename__ = 'submissions'

    uid = Column(Integer())
    status = Column(String(50))
    time_stamp = Column(Integer, primary_key=True)

    def __repr__(self):
        return "<Submission(uid='%s', status='%s', time_stamp='%d')>" % (
            self.username, self.status, self.time_stamp)


def new_submission(uid, status):
    session = Session()
    t = time.time()
    sub = Submission(uid=uid, status=status, time_stamp=(int)(t))
    session.add(sub)
    session.commit()
    session.close()


def create_user(uname, full, pwd):
    session = Session()
    u = User(username=uname, fullname=full, password=generate_password_hash(pwd), score=0, totalattempted=0,
             totalcorrect=0, settings='')
    session.add(u)
    session.commit()
    session.close()


def get_all_users():
    session = Session()
    list = session.query(User).order_by(User.score.desc())
    session.close()
    return list


def users_by_accuracy():
    session = Session()
    list = session.query(User).order_by((User.totalcorrect * 100 / User.totalattempted).desc())
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
    username = username.lower()
    session = Session()
    q = session.query(User).filter(User.username == username).first()
    session.close()
    return not (q is None)


def is_valid(u, p):
    session = Session()
    user = session.query(User).filter(User.username == u.lower()).first()
    if (check_password_hash(user.password, p)):
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


def incorrect(user, qid):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})
    session.query(User).filter(User.username == user.username).update({User.settings: 'Last: ' + qid})
    session.commit()
    session.close()
    new_submission(user.uid, 'i')


def correct(user, qid):
    session = Session()
    session.query(User).filter(User.username == user.username).update({User.totalcorrect: User.totalcorrect + 1})
    session.query(User).filter(User.username == user.username).update({User.totalattempted: User.totalattempted + 1})
    session.query(User).filter(User.username == user.username).update({
        User.score: User.totalcorrect * User.totalcorrect / User.totalattempted})
    session.query(User).filter(User.username == user.username).update({User.settings: 'Last: ' + qid + '|'})
    session.commit()
    session.close()
    new_submission(user.uid, 'c')


def get_random_question(subject):
    session = Session()
    matching_subject = session.query(Question).filter(Question.subject == subject)
    row_count = matching_subject.count()
    rnd = random.randint(0, row_count - 1)
    session.close()
    return matching_subject[rnd]





def get_question_by_qid(qid):
    session = Session()
    question = session.query(Question).filter(Question.qid == qid).first()
    session.close()
    return question


def add_question(questionheader, questiontext, answerchoices, correctanswer, explanation, subject):
    session = Session()
    question = Question(questionheader=questionheader, questiontext=questiontext, answerchoices=answerchoices,
                        correctanswer=correctanswer, explanation=explanation, subject=subject)
    session.add(question)
    session.commit()
    session.close()


def update_question(questionid, questionheader, questiontext, answerchoices, correctanswer, explanation, subject):
    session = Session()
    session.query(Question).filter(Question.qid == questionid).update({Question.questionheader: questionheader})
    session.query(Question).filter(Question.qid == questionid).update({Question.questiontext: questiontext})
    session.query(Question).filter(Question.qid == questionid).update({Question.answerchoices: answerchoices})
    session.query(Question).filter(Question.qid == questionid).update({Question.correctanswer: correctanswer})
    session.query(Question).filter(Question.qid == questionid).update({Question.explanation: explanation})
    session.query(Question).filter(Question.qid == questionid).update({Question.subject: subject})
    session.commit()
    session.close()


def get_last_question(user):
    str = user.settings
    if str is None or '':
        return
    settings = str.split('|')
    question_id = settings[0].replace('Last: ', '')
    if question_id == '':
        return
    return (int)(question_id)


def get_table_amts():
    session = Session()
    data = []
    data.append(session.query(User.uid).count())
    data.append(session.query(Question.qid).count())
    data.append(session.query(Submission.uid).count())
    session.close()
    return data


Base.metadata.create_all(engine)

