import secrets
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
 
    app.config['DEBUG'] = False 
    app.config['ENV'] = 'production'
    app.config['SECRET_KEY'] = secrets.token_hex(32)
        
    CORS(app)

    from .routes import routes
    app.register_blueprint(routes)

    return app
