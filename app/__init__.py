from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'clave'
    
    CORS(app)

    from .routes import routes
    app.register_blueprint(routes)

    return app
