"""
This module initializes the Flask application and sets up caching.

It creates a Flask app, configures a simple cache, initializes routes,
and runs the app in debug mode if executed as the main script.

The app uses blueprint_plaza.routes for routing configuration.
"""
# pylint: disable=import-error
import os
from flask import Flask, request, session, g
from flask_caching import Cache
from routes import init_routes
import os
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # Clave secreta segura
app.config['PREFERRED_URL_SCHEME'] = 'https'
app.config['SUPPORTED_LANGUAGES'] = ['ca', 'es', 'en', 'fr']
cache = Cache(config={
    'CACHE_TYPE': 'redis',
    'CACHE_KEY_PREFIX': 'blueprint_plaza',
    'CACHE_REDIS_HOST': 'localhost',  # Add host
    'CACHE_REDIS_PORT': 6379,         # Add port
    'CACHE_DEFAULT_TIMEOUT': 300      # Add timeout
})
cache.init_app(app)
init_routes(app, cache)

def load_translations():
    translations = {}
    translations_path = os.path.join(os.path.dirname(__file__), 'translations')
    for lang in app.config['SUPPORTED_LANGUAGES']:
        file_path = os.path.join(translations_path, f"{lang}.json")
        with open(file_path, 'r', encoding='utf-8') as f:
            translations[lang] = json.load(f)
    return translations

app.config['TRANSLATIONS'] = load_translations()

@ app.before_request
def before_request():
    lang = session.get('lang', 'ca')
    if lang not in app.config['SUPPORTED_LANGUAGES']:
        lang = 'ca'
    g.lang = lang
    g.translations = app.config['TRANSLATIONS'].get(lang, {})

@app.context_processor
def inject_translations():
    def _(text):
        return g.translations.get(text, text)
    return {'_': _}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4300))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
