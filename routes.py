# pylint: disable=C0116
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

from flask import render_template, redirect, url_for, abort
# pylint: disable=import-error
from utils.read_json import load_ads



def init_routes(app, cache):
    @app.errorhandler(404)
    def page_not_found():
        return render_template('404.html'), 404

    @app.route('/', strict_slashes=False)
    def index():
        return redirect(url_for('home'))

    @cache.cached(timeout=3600)
    def cached_load_ads():
        return load_ads()

    @app.route('/home', strict_slashes=False, methods=['GET'])
    def home():
        projects = cached_load_ads()
        return render_template('home.html', projects=projects)

    @app.route('/about', strict_slashes=False, methods=['GET'])
    def about():
        return render_template('about.html')

    @app.route('/ad/<int:project_id>', strict_slashes=False, methods=['GET'])
    def project_detail(project_id):
        ads = cached_load_ads()
        ad = next((ad for ad in ads if ad['id'] == project_id), None)
        if ad:
            project = ad
            return render_template('project_detail.html', project=project)
        return abort(404)
