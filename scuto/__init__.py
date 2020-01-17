from aiohttp import web
from scuto.models import init_mongodb
from scuto.api.v1 import register_apis


app = web.Application()
app.__version__ = "0.0.1"
db = init_mongodb(app)
register_apis(app)
