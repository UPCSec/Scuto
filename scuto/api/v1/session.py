from uuid import uuid4
from scuto.util.decorators import asynchronos
from scuto.models import Login, Session


load = 0

@asynchronos
def start_session(user, login):
    sessionid = uuid4()
    return Session(user=user, login=login, sessionid=sessionid).save()
