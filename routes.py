from flask import render_template, redirect, url_for, abort
from utils.read_json import load_ads
from data import projects

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
        print(type(projects))
        return render_template('home.html', projects=cached_load_ads())

    @app.route('/about', strict_slashes=False, methods=['GET'])
    def about():
        return render_template('about.html')

    @app.route('/ad/<int:ad_id>', strict_slashes=False, methods=['GET'])
    def get_ad(ad_id):
        ads = cached_load_ads()
        ad = next((ad for ad in ads if ad['id'] == ad_id), None)
        if ad:
            return render_template('ad.html', ad=ad)
        else:
            return abort(404)

    #TODO: Remove this mess and refactor ad so it works properly with new html template.
    # Nueva ruta para detalle de proyecto
    @app.route('/proyecto/<project_id>', strict_slashes=False, methods=['GET'])
    def project_detail(project_id):
        # projects = cached_load_ads()
        project = next((proj for proj in projects if proj['id'] == project_id), None)
        print("project --> ", project)
        if project is None:
            abort(404)  # Página no encontrada si el proyecto no existe
        return render_template('project_detail.html', project=project)
