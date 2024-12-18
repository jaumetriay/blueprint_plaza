from flask import render_template, redirect, url_for, abort
from utils.read_json import load_ads

"""
Initialize routes for the Flask application.

This function sets up the following routes:
- Error handler for 404 (Page Not Found)
- Index route ('/') that redirects to home
- Home route ('/home') that displays ads
- Individual ad route ('/ad/<ad_id>') that displays a specific ad

It also implements caching for loading ads to improve performance.

:param app: Flask application instance
:param cache: Cache object for caching expensive operations
"""

def init_routes(app, cache):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/', strict_slashes=False)
    def index():
        return redirect(url_for('home'))

    @cache.cached(timeout=3600)
    def cached_load_ads():
        return load_ads()

    @app.route('/home', strict_slashes=False, methods=['GET'])
    def home():
        return render_template('home.html', ads=cached_load_ads())

    @app.route('/ad/<int:ad_id>', strict_slashes=False, methods=['GET'])
    def get_ad(ad_id):
        ads = cached_load_ads()
        ad = next((ad for ad in ads if ad['id'] == ad_id), None)
        if ad:
            return render_template('ad.html', ad=ad)
        else:
            return abort(404)
