 
from flask import Blueprint, jsonify

colaborador_bp = Blueprint('colaborador', __name__)

@colaborador_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return jsonify({"message": "Área do Colaborador"})
