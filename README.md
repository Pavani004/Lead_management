# Lead Management System

This project is a backend Lead Management System built using Flask. It provides RESTful APIs for user login and managing travel agent leads. The system uses MongoDB for flexible NoSQL data storage, JWT for secure authentication, and supports role-based access control. It is designed to be lightweight, scalable, and easily extensible for future features.

The key features include a RESTful API built with Flask, MongoDB integration using PyMongo and Flask-PyMongo, JWT-based authentication using Flask-JWT-Extended, and role-based access control implemented at the route level. The application also follows a modular structure with Blueprints to keep authentication and API logic separate and organized.

The project uses Python 3.10 and key libraries such as Flask, Flask-JWT-Extended, Flask-PyMongo, and Flask-RESTful. It does not require any ORM, allowing direct and efficient interaction with MongoDB documents. The app supports a minimal user login system with hardcoded roles for demonstration, and can be extended to support proper user registration and MongoDB-backed authentication.

To get started, you need Python 3.10 and MongoDB installed. First, clone the repository from GitHub using the command `git clone https://github.com/your-username/flask-lead-management.git`, then navigate into the project directory. Set up a virtual environment using `python -m venv venv`, activate it, and install dependencies with `pip install -r requirements.txt`. Finally, start MongoDB and run the Flask app using `python run.py`.

The MongoDB connection string is configured in the `config.py` file, and defaults to `mongodb://localhost:27017/leadsdb`. You can customize this as needed. JWT tokens are signed using a secret key defined in the same configuration file.

The API endpoints include:

- **POST /login**: To log in using a username and password and receive a JWT access token. The role is included in the token payload.  
- **POST /lead**: To create a new lead entry in MongoDB. This requires an access token and checks if the user has the `agent` role.

The project is structured into modular components. `app/__init__.py` sets up the app factory and extensions. `app/auth.py` handles authentication logic and routes. `app/routes.py` includes the secured lead management routes. `run.py` is the entry point of the application.

If you prefer to use Docker and Docker Compose, a configuration can be added to containerize both the Flask app and MongoDB database. Alternatively, you can use a MongoDB Docker container alone and run Flask natively.

The project is open source and licensed under the MIT License.
