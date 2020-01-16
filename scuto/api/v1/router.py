from functools import wraps


apis = []

def routes(route):
    def route_wrapper(handler):
        apis.append((route, handler))
        return handler
    return route_wrapper
