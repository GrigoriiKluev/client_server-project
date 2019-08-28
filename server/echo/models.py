from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime,ForeignKey )
from sqlalchemy.orm import mapper
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
from auth.models import User



class Message(Base):
    __tablename__= 'Messages'
    id = Column(Integer, primary_key= True , autoincrement=True)
    data = Column(String, nullable=True)
    created = Column(DateTime, default= datetime.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='messages')













