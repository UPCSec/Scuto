from aiohttp.web import Response
from bson import json_util
from functools import wraps
import json


def jsonify(dumps=json_util.default):
    def wrapper(handler):
        @wraps(handler)
        async def wrapped(request):
            response = await handler(request)
            return Response(body=json.dumps(response, default=dumps), content_type='application/json')
        return wrapped
    return wrapper