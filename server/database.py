from sqlalchemy import MetaData
from sqlalchemy import create_engine

database_metadata = MetaData()

engine = create_engine(('sqlite:///storage.db'))

