from functools import wraps
from aiohttp.web import RouteTableDef


apis = RouteTableDef()

def routes(route, methods=['GET']):
    def route_wrapper(handler):
        if isinstance(methods, list):
            for method in methods:
                apis.route(method, route)(handler)
        else:
            raise Exception('methods should be list')
        return handler
    return route_wrapper
