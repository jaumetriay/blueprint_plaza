from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from blueprint_plaza.actions.login.user import User

login_blueprint = Blueprint('login', __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the username and password. This example uses a simple check.
        if username == 'example' and password == '1234':
            user = User(1)
            login_user(user)
            return redirect(url_for('publish.publish'))
    return render_template('login.html')


@login_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'


@login_blueprint.route(
    '/protected')  # this is just an example for endpoints that require login, in the future this should go somewhere else
@login_required
def protected():
    return 'Logged in as: ' + str(current_user.get_id())


