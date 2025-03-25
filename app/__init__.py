from flask import Flask
from app.routes import init_app

def create_app():
    app = Flask(__name__)
    
    # Registrar Blueprints
    init_app(app)

    return app

