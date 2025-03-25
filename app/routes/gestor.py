 
from flask import Blueprint, jsonify

gestor_bp = Blueprint('gestor', __name__)

@gestor_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({"message": "Área do Gestor"})
