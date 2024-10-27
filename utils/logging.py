
from functools import wraps
from flask import current_app, request
"""
Decorator function to log route access.

This decorator logs the accessed route path using the Flask application's logger.
It can be applied to route handler functions to automatically log each request.

Usage:
    @log_route_access
    def route_handler():
        ...

Returns:
    function: The decorated function.
"""
def log_route_access(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_app.logger.info(f'Accessed: {request.path}')
        return f(*args, **kwargs)
    return decorated_function
