from flask import request
from scuto.models import Login
from scuto.util.request import get_client_ip


def login(user, status):
    _login = Login(user=user, ip=get_client_ip(), status=status)
    return _login.save()

load = 0
