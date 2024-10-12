# Blueprint Plaza Project

Welcome to our project! A solution for premises with market potential in need for real-state investors.
This project uses [Poetry](https://python-poetry.org/) for dependency management.

## Installation

Before you can use this project, you need to install Poetry. Follow the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).
Once you have Poetry installed, you can install the project dependencies with:

\`\`\`bash
poetry install
\`\`\`

then run to start the project

\`\`\`bash
poetry run start
\`\`\`

## Main Project Files

## main.py

This is the entry point of the application. It sets up the Flask app, registers the blueprints for the login and publish functionalities, and runs the app.

## actions/login/login_routes.py

This file sets up the routes related to user login functionality. It includes the user loader for Flask-Login, the login route, the logout route, 
and a protected route that requires login.

## actions/login/user.py

This file contains the User class for Flask-Login. The User class has an id attribute and is used in the user loader in `login_routes.py`.

## actions/publish/publish_routes.py

This file sets up the routes for the publish functionality. It includes a route for publishing a property, which requires login.

## db/connection.py

This file sets up the SQLAlchemy engine and session. It uses the declarative base from SQLAlchemy and sets up a sessionmaker bound to the engine.

## forms/publish_form.py

This file contains the form for the publish functionality. The form includes fields for the base price, expected price, and description of a property.

## models/property.py

This file contains the SQLAlchemy model for a property. The Property class includes attributes for the premise id, base value, expected value, 
and description of a property.



Hola soc jo
