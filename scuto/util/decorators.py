from aiohttp.web import Response
from bson import json_util
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import asyncio
import json


_thread_pool = ThreadPoolExecutor()

def jsonify(dumps=json_util.default):
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