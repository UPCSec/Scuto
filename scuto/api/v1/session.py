from flask import request
from uuid import uuid4
from scuto.models import Login, Session
from .login import login


load = 0

def start_session(user):
    _login = login(user, 'success')
    sessionid = uuid4()
    return Session(user=user, login=_login, sessionid=sessionid).save()
