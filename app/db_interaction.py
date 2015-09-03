from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    name = Column(String(50), primary_key=True)
    fullname = Column(String(50))
    password = Column(String(12))
    score = Column(Integer())

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


def create_new_user(name, fullname, password):
    user = User(name='Davis', fullname='Davis Robertson', password='lank', score=100)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(user)
    session.commit()
