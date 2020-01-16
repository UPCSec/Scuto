from scuto.models import User, Session, Login, Team
from .router import apis
# The 'load' variable is set to let python intepreter to load these scripts to collect apis
from .user import load
from .login import load

def register(app, route, api):
    app.route(route)(api)

def register_apis(app):
    for api in apis:
        register(app, api[0], api[1])