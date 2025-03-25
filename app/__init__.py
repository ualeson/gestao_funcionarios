from flask import Flask # type: ignore
from app.config import Config
from app.database import db
from app.routes.gestor import gestor_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar os módulos
    app.register_blueprint(gestor_bp, url_prefix='/gestor')

    return app
