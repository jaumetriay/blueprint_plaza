# routes.py

from flask import render_template, redirect, url_for, abort
from data import projects  # Asegúrate de importar `projects` correctamente

def init_routes(app, cache):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/', strict_slashes=False)
    def index():
        return redirect(url_for('home'))

    @app.route('/home', strict_slashes=False, methods=['GET'])
    def home():
        return render_template('home.html', projects=projects)  # Pasar `projects` al template

    @app.route('/about', strict_slashes=False, methods=['GET'])
    def about():
        return render_template('about.html')

    # Nueva ruta para detalle de proyecto
    @app.route('/proyecto/<project_id>', strict_slashes=False, methods=['GET'])
    def project_detail(project_id):
        # Buscar el proyecto por su ID
        project = next((proj for proj in projects if proj['id'] == project_id), None)
        if project is None:
            abort(404)  # Página no encontrada si el proyecto no existe
        return render_template('project_detail.html', project=project)
