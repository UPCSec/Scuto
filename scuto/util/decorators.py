from aiohttp.web import Response
from bson import json_util, ObjectId
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from scuto.util.time import get_timestamp
from scuto.models.user import User
import asyncio
import json


_thread_pool = ThreadPoolExecutor()

def object_dump(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, datetime):
        return get_timestamp(obj)
    return json_util.default(obj)

def jsonify(dumps=object_dump):
    """
    Wrap response into json.
    """
    def wrapper(handler):
        @wraps(handler)
        async def wrapped(request):
            response = await handler(request)
            return Response(body=json.dumps(response, default=dumps), content_type='application/json')
        return wrapped
    return wrapper

def asynchronos(func):
    """
    Force a function to run asynchronosly, AND the function shouldn't be defined using 'async def'.
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        future = _thread_pool.submit(func, *args, **kwargs)
        return asyncio.wrap_future(future)
    return wrapped

def require_admin(func):
    """
    This interface requires admin token.
    """
    @wraps(func)
    def wrapped(request):
        token = request
        if User.is_admin():
            pass
        