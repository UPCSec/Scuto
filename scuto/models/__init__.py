from flask_mongoengine import MongoEngine
from .user import User
from .login import Login
from .session import Session
from .team import Team

def init_mongodb(app):
    db = MongoEngine(app)
    return db
