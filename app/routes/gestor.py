 
from flask import Blueprint, request, jsonify # type: ignore
from app.database import db
from app.models.funcionario import Funcionario

gestor_bp = Blueprint('gestor', __name__)

# 📌 Criar funcionário
@gestor_bp.route('/funcionarios', methods=['POST'])
def cadastrar_funcionario():
    data = request.json
    novo_funcionario = Funcionario(
        nome=data['nome'],
        matricula=data['matricula'],
        cpf=data['cpf']
    )
    db.session.add(novo_funcionario)
    db.session.commit()
    return jsonify({"mensagem": "Funcionário cadastrado com sucesso!"}), 201

# 📌 Editar funcionário
@gestor_bp.route('/funcionarios/<int:id>', methods=['PUT'])
def editar_funcionario(id):
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return jsonify({"erro": "Funcionário não encontrado"}), 404

    data = request.json
    funcionario.nome = data.get('nome', funcionario.nome)
    funcionario.matricula = data.get('matricula', funcionario.matricula)
    funcionario.cpf = data.get('cpf', funcionario.cpf)
    
    db.session.commit()
    return jsonify({"mensagem": "Funcionário atualizado com sucesso!"})

# 📌 Excluir funcionário
@gestor_bp.route('/funcionarios/<int:id>', methods=['DELETE'])
def excluir_funcionario(id):
    funcionario = Funcionario.query.get(id)
    if not funcionario:
        return jsonify({"erro": "Funcionário não encontrado"}), 404

    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({"mensagem": "Funcionário excluído com sucesso!"})
