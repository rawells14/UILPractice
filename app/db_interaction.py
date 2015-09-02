from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sqlite3

DATABASE = 'sqlite:///data.db'

engine = create_engine(DATABASE, echo=True)
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


ryan = User(name='Ryan', fullname='Ryan Wells', password='dank', score='100')
print(ryan.password)