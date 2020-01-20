from aiohttp import web
from scuto.models import init_mongodb
from scuto.api.v1 import register_apis
from scuto.util.log import setup_logging
from scuto.util.middlewares import error_info


app = web.Application(middlewares=[error_info])
app.on_startup.append(init_mongodb)
app.on_startup.append(register_apis)
app.on_startup.append(setup_logging)