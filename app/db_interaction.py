from flask_login import unicode
from sqlalchemy import Column, Integer, String, create_engine, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///data.db', echo=True)


class User(Base):
    __tablename__ = 'users'

    username = Column(String(50), primary_key=True)
    fullname = Column(String(50))
    password = Column(String(12))
    score = Column(Integer)

    def __repr__(self):
        return "<User(username='%s', fullname='%s', password='%s', score='%d')>" % (
            self.username, self.fullname, self.password, self.score)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.username)


def create_user(uname, full, pwd, scr):
    Session = sessionmaker(bind=engine)
    session = Session()
    u = User(username=uname, fullname=full, password=pwd, score=scr)
    session.add(u)
    session.commit()


def get_all_users():
    Session = sessionmaker(bind=engine)
    session = Session()
    list = []
    for i in session.query(User).order_by(User.username):
        list.append(i)
    return list


def get_user_by_username(username):
    lst = get_all_users()
    for i in lst:
        print(i)
        print(i.username)
        print(username)
        if i.username == username:
            return i
    return None


def is_taken(u):
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(User).filter_by(username=u[0]).first()
    return not (q is None)


def is_valid(u, p):
    username = u[0]
    password = p[0]
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(User).order_by(User.username):
        if i.username == username and i.password == password:
            return True
    return False
