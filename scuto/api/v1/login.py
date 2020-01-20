from scuto.models import Login
from .router import routes
from scuto.util.decorators import jsonify, asynchronos


load = 0

@asynchronos
def record_login(user, ip, status):
    _login = Login(user=user, ip=ip, status=status)
    return _login.save()

@routes('/user/login_history')
@jsonify()
async def get_login_history(request):
    pass
