from mongoengine import connect
from scuto.config import config
from .user import User
from .login import Login
from .session import Session
from .team import Team
from .challenge import Challenge
from .flag import Flag

def init_mongodb(app):
    db = connect(**config['MongoDB'])
    return db
