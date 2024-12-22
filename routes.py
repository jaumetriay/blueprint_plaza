from flask import render_template, redirect, url_for, abort

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

    @app.route('/home', strict_slashes=False, methods=['GET'])
    def home():
        return render_template('home.html')



    @app.route('/about', strict_slashes=False, methods=['GET'])
    def about():
        return render_template('about.html')

    @app.route('/proyecto1', strict_slashes=False, methods=['GET'])
    def proyecto1():
        return render_template('proyecto1.html')

    @app.route('/proyecto2', strict_slashes=False, methods=['GET'])
    def proyecto2():
        return render_template('proyecto2.html')

    @app.route('/proyecto3', strict_slashes=False, methods=['GET'])
    def proyecto3():
        return render_template('proyecto3.html')

