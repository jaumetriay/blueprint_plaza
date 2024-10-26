from flask import Flask
from flask_caching import Cache
from blueprint_plaza.routes import init_routes
import os
"""
This module initializes the Flask application and sets up caching.

It creates a Flask app, configures a simple cache, initializes routes,
and runs the app in debug mode if executed as the main script.

The app uses blueprint_plaza.routes for routing configuration.
"""

app = Flask(__name__)
app.config['PREFERRED_URL_SCHEME'] = 'https'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
init_routes(app, cache)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)