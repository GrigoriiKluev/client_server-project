from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime, )
from sqlalchemy.orm import mapper

import hashlib

from datetime import datetime




engine = create_engine('sqlite:///serverdate.db')
metadata = MetaData()

server_date_table = Table (
    'serverdate_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('request', String ),
    Column('code', Integer),
    Column('time', DateTime),

)
metadata.create_all(engine)
class ServerDate:
    def __init__(self, action, time, data, token):
        self._action = action
        self._time = time
        self._data = data
        self._token =token
mapper(ServerDate, server_date_table)


request = {
                    'action': 'echo',
                    'time': datetime.now().timestamp(),
                    'data': 'data',
                    'token':hashlib.sha256().hexdigest()
                }
serv = ServerDate(request.get('action'),request.get('time'),request.get('data'), request.get('token'))

print (serv._action,'\n', serv._time,'\n', serv._data,'\n', serv._token)