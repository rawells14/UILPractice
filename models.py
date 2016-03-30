from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

Base = declarative_base()


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


class Badge(Base):
    __tablename__ = 'badges'
    uid = Column(Integer, primary_key=True)
    badgeids = Column(String(5000))

    def __repr__(self):
        return "<Badge(uid='%d', badgeids='%s')>" % (
            self.uid,
            self.badgeids)


class Flag(Base):
    __tablename__ = 'flags'
    qid = Column(Integer, primary_key=True, autoincrement=True)
    flags = Column(Integer)

    def __repr__(self):
        return "<Question(qid='%d', flags='%s')>" % (
            self.qid,
            self.flags)


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
