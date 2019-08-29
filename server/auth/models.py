from database import Base
from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime,ForeignKey )
from  datetime import datetime
from sqlalchemy.orm import relationship



class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key= True , autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    sessions = relationship('Session', back_populates= 'user')
    messages = relationship('Message', back_populates='user')

    def __repr__(self):
        return "<User(name='%s', password='%s')>" % (self.name, self.password)

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='sessions')