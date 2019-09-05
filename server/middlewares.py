import zlib
from protocol import make_response
from functools import wraps

from Cryptodome.Cipher import AES
import json
from auth.models import User
from database import Session
import hmac


def compression_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        b_request = zlib.decompress(request)
        b_response = func(b_request, *args, **kwargs)
        return zlib.compress(b_response)
    return wrapper

def encryption_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        encrypted_request = json.loads(request)
        key = encrypted_request.get('key')
        data = encrypted_request.get('data')
        cypher = AES.new(key, AES.MODE_EAX)
        decrypted_data = cypher.decrypt(data)
        decrypted_request = encrypted_request.copy()
        decrypted_request['data'] = decrypted_data
        bytes_request = json.dumps(request).encode()

        b_response = func(bytes_request, *args, **kwargs)


        decrypted_response = json.loads(b_response)
        decrypted_data = decrypted_response.get('data')
        encrypted_data = cypher.encrypt(decrypted_data)
        encrypted_response = b_response.copy()
        encrypted_response['data'] = encrypted_data
        return json.dumps(encrypted_response).encode()
    return wrapper

def auth_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        authenticated =True
        request_obj = json.loads(request)
        login = request_obj.get('login')
        token = request_obj.get('token')
        time = request_obj.get('time')

        session = Session()
        user = session.query(User).filter_by(name= login).first()
        if user:
            digest = hmac.new(time, user.password)

            if hmac.compare_digest(digest, token):
                authenticated = False
        else:
            authenticated = False

        if authenticated:
            return func(request, *args, **kwargs)

        response = make_response(request, 401, 'Access denied')
        return json.dumps(response).encode()
    return wrapper
