from mongoengine.queryset.visitor import Q
from mongoengine import ValidationError
from scuto.models import User
from scuto.util.decorators import jsonify, asynchronos
from scuto.util.time import get_timestamp
from .router import routes
from .session import start_session
from .login import record_login
import bcrypt


load = 0

class UserExistException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

@asynchronos
def find_user(username, email):
    if username and not email:
        return User.objects(username=username)
    if not username and email:
        return User.objects(email=email)
    if username and email:
        return User.objects(Q(username=username) | Q(email=email))
    else:
        return None

async def is_exist(username, email):
    exist = await find_user(username, email)
    return True if exist else False

async def create_user_check_exist(user):
    if await is_exist(user.username, user.email):
        raise UserExistException()
    user.salt = bcrypt.gensalt()
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), user.salt).decode('utf-8')
    user.salt = user.salt.decode('utf-8')
    return user.save(force_insert=True)

@asynchronos
def verify_user(user, password):
    return bcrypt.checkpw(password.encode('utf-8'), str(user.password).encode('utf-8'))

@routes('/user/check_exist')
@jsonify()
async def check_exist(request):
    query = request.query
    return {
        'username': True if User.objects(username=query['username']) else False,
        'email': True if User.objects(username=query['email']) else False
    }

@routes('/user/login', methods=['POST'])
@jsonify()
async def login(request):
    user = request.json()
    exist_user = await find_user(user['usernameOrEmail', 'usernameOrEmail'])
    if await verify_user(exist_user, user['password']):
        _login = await record_login(user, request.remote, 'success')
        session = await start_session(user, _login)
        return {
            'user': user.username,
            'email': user.email,
            'admin': user.admin,
            'sessionid': str(session.sessionid),
            'expires': get_timestamp(session.start_time)
        }
    else:
        _login = await record_login(user, request.remote, 'failed')
        return {
            'status': 'failed'
        }

@routes('/user/register', methods=['POST'])
@jsonify()
async def register(request):
    user = User.from_json(await request.text())
    print(type(user.email))
    error = ''
    try:
        _login = await record_login(user, request.remote, 'success')
        await create_user_check_exist(user)
        session = await start_session(user, _login)
        return {
            'user': user.username,
            'email': user.email,
            'admin': user.admin,
            'sessionid': str(session.sessionid),
            'expires': get_timestamp(session.start_time)
        }
    except UserExistException as e:
        error = 'User already exists.'
    except ValidationError as e:
        error = e.message
    return {
        'status': 'failed',
        'error': error
    }

@routes('/user/add_admin', methods=['POST'])
@jsonify()
async def add_admin(request):
    # TODO validate admin token
    user = User.from_json(await request.text())
    user["admin"] = True
    error = ''
    try:
        user = await create_user_check_exist(user)
        return {
            'status': 'success'
        }
    except UserExistException as e:
        error = 'User already exists.'
    except ValidationError as e:
        error = e.message
    return {
        'status': 'failed',
        'error': error
    }

@routes('/user/remove', methods=['POST'])
@jsonify()
async def remove(request):
    pass

@routes('/user/request_reset_password', methods=['POST'])
@jsonify()
async def request_reset_password(request):
    pass

@routes('/user/reset_password')
@jsonify()
async def reset_password(request):
    pass