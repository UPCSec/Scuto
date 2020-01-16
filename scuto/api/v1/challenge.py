from flask import request
from bson import json_util
from scuto.models import Login
from .router import routes
import json


load = 0

def login(user, status):
    _login = Login(user=user, ip=get_client_ip(), status=status)
    return _login.save()

@routes('/user/login_history')
def get_login_history

