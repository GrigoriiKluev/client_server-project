from sqlalchemy import (
    create_engine, Table, String, Integer, MetaData, Column ,DateTime, )
from sqlalchemy.orm import mapper

import hashlib






engine = create_engine('sqlite:///echomodels.db')
metadata = MetaData()

echo_controller_table = Table (
    'echo_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('request', String ),
    Column('code', Integer),
    Column('data', String),
    Column('token',String),
)
metadata.create_all(engine)

class Echo:
    def __init__(self, request, code, data, token):
        self._request = request
        self._code = code
        self._data = data
        self._token =token
mapper(Echo, echo_controller_table)


request = {
                    'action': 'echo',
                    'time': 200,
                    'data': 'data',
                    'token':hashlib.sha256().hexdigest()
                }









echo =Echo(request.get('action'), request.get('time'), request.get('data'),request.get('token'))


print(echo._request,'\n',echo._token,'\n', echo._data,'\n', echo._code )

