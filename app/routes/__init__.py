 
from flask import Flask
from app.routes.colaborador import colaborador_bp
from app.routes.gestor import gestor_bp

def init_app(app: Flask):
    app.register_blueprint(colaborador_bp, url_prefix='/colaborador')
    app.register_blueprint(gestor_bp, url_prefix='/gestor')
