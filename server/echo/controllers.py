from functools import reduce
from database import session_scope, Session
from protocol import make_response
from database import Session
from decorators import logged

from .models import Message


@logged
def echo_controller(request):
    data = request.get('data')
    session = Session()
    message = Message(data=data.get('text'))
    session.add(message)
    session.commit()
    session.close()
    return make_response(request, 200, data)


def delete_message_controller(request):
    data = request.get('data')
    message_id = data.get('message_id')
    with session_scope() as session:
        message = session.query(Message).filter_by(id=message_id).first()
        session.delete(message)
        return make_response(request, 200)


def update_message_controller(request):
    data = request.get('data')
    message_id = data.get('message_id')
    message_data = data.get('message_data')
    with session_scope() as session:
        message = session.query(Message).filter_by(id=message_id).first()
        message.data = message_data
        return make_response(request, 200)


@logged
def get_messages_controller(request):
    session = Session()
    messages = reduce(
        lambda value, item: value + [
            {'data': item.data, 'created': item.created.timestamp()}
        ],
        session.query(Message).all(),
        []
    )
    return make_response(request, 200, messages)

