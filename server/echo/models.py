from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime, )
from sqlalchemy.orm import mapper
from database import database_metadata
import hashlib






engine = create_engine('sqlite:///echomodels.db')


echo_controller_table = Table (
    'echo_table', database_metadata,
    Column('id', Integer, primary_key=True),
    Column('content', String),
    Column('user', Integer),
    Column('created', DateTime),

)
database_metadata.create_all(engine)

class Echo:
    def __init__(self, content, user, date):
        self.content = content
        self.user = user
        self.date = date
mapper(Echo, echo_controller_table)














