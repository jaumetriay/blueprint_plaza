from flask import Flask, render_template
from premise_update.login.login_routes import login_blueprint, login_manager

app = Flask(__name__)
app.register_blueprint(login_blueprint)
app.secret_key = 'my template secret key'  # need to replace with actual key
login_manager.init_app(app)


@app.route('/')
def home():
    return render_template('placeholder.html')


if __name__ == '__main__':
    app.run(debug=True)
