from flask import request
from bson import json_util
from mongoengine import ValidationError
from scuto.models import User
from .router import routes
from .session import start_session
from .login import login
import bcrypt
import json


load = 0

class UserExistException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

def create_user_check_exist(user):
    exist = User.get_or_none(username=user["username"])
    if exist:
        raise UserExistException()
    user["salt"] = bcrypt.gensalt()
    user["password"] = bcrypt.hashpw(user["password"].encode('utf-8'), user["salt"]).decode('utf-8')
    user["salt"] = user["salt"].decode('utf-8')
    return user.save()

def verify_user(self, password):
    return bcrypt.checkpw(password.encode('utf-8'), str(self.password).encode('utf-8'))

@routes('/user/check_exist')
def check_exist():
    exist = User.get_or_none(username=user["username"])
    return {
        'result': True if exist else False
    }

@routes('/user/login')
def login():
    user = User.from_json(request.data)
    session = start_session(user)
    return json.dumps({
        'user': user.to_mongo().to_dict(),
        'session': session.to_mongo().to_dict()
    }, default=json_util.default)

@routes('/user/add_user')
def add_user():
    user = User.from_json(request.data)
    user["admin"] = False
    error = ''
    try:
        user = create_user_check_exist(user)
        session = start_session(user)
        return json.dumps({
            'user': user.to_mongo().to_dict(),
            'session': session.to_mongo().to_dict()
        }, default=json_util.default)
    except UserExistException as e:
        error = 'User already exists.'
    except ValidationError as e:
        error = e.message
    return {
        'status': 'failed',
        'error': error
    }

@routes('/user/add_admin')
def add_admin(admin_token):
    # TODO validate admin token
    user = User.from_json(request.data)
    user["admin"] = True
    return create_user_check_exist(user)
