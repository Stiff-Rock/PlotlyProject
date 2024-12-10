import os
import sys
import secrets
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
 

    if getattr(sys, 'frozen', False): 
        app.template_folder = os.path.join(sys._MEIPASS, 'templates')
        app.static_folder = os.path.join(sys._MEIPASS, 'static')
        print("Production Build")
    else:
        print("Developement Build")

    app.config['DEBUG'] = False 
    app.config['ENV'] = 'production'
    app.config['SECRET_KEY'] = secrets.token_hex(32)
        
    CORS(app)

    from .routes import routes
    app.register_blueprint(routes)

    return app
