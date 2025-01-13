"""
This module initializes the Flask application and sets up caching.

It creates a Flask app, configures a simple cache, initializes routes,
and runs the app in debug mode if executed as the main script.

The app uses blueprint_plaza.routes for routing configuration.
"""
# pylint: disable=import-error
import os
from flask import Flask
from flask_caching import Cache
from routes import init_routes

app = Flask(__name__)
app.config['PREFERRED_URL_SCHEME'] = 'https'
cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'blueprint_plaza',
    'CACHE_REDIS_HOST': 'localhost',  # Add host
    'CACHE_REDIS_PORT': 6379,         # Add port
    'CACHE_DEFAULT_TIMEOUT': 300      # Add timeout
})
cache.init_app(app)
init_routes(app, cache)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4300))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
