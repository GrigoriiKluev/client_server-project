from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime)
from sqlalchemy.orm import mapper


engine = create_engine('sqlite:///storage.db')
metadata = MetaData()

client_table = Table(
    'client', metadata,
    Column('id', Integer, primary_key=True),
    Column('login', String),
    Column('password', String)
)
client_history_table = Table(
    'client_history', metadata,
    Column('id', Integer, primary_key=True),
    Column('enter_time', Integer),
    Column('ip_address', Integer)
)
contact_list_table = Table(
    'contact list', metadata,
    Column('id', Integer, primary_key=True),
    Column('id_owner', Integer),
    Column('id_client',Integer),
)

metadata.create_all(engine)

class ClientTable:
    def __init__(self, login, password ):
        self._login = login
        self._password = password


class ClientHistoryTable:
    def __init__(self, enter_time, ip_address):

        self._enter_time = enter_time
        self._ip_address = ip_address


class Contactlist :
    def __init__(self, id_owner, id_client):
        self._id_owner =id_owner
        self._id_client = id_client


mapper(ClientTable, client_table)
mapper(ClientHistoryTable, client_history_table)
mapper(Contactlist, contact_list_table)





