from mongoengine import connect
from scuto.util.decorators import asynchronos
from scuto.config import config
from .user import User
from .login import Login
from .session import Session
from .team import Team
from .challenge import Challenge
from .flag import Flag


@asynchronos
def init_mongodb(app):
    app['mongo'] = connect(**config['MongoDB'])