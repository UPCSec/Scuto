from scuto.models import User, Session, Login, Team
from .router import apis
# The 'load' variable is set to let python intepreter to load these scripts to collect apis
from .user import load
from .login import load


def register_apis(app):
    app.add_routes(apis)