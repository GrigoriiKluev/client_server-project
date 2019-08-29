#from decorators import logged, login_required
from database import  Session
from .models import User

class Users:
    def __init__(self, name , password):
        self._name = name
        self._password = password


    def create_user(self):
        session = Session()
        user = User(name=self._name, password=self._password)
        session.add(user)
        session.commit()



Users('Вася ', 'qwerty')