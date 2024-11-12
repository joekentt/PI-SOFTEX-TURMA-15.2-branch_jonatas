from flask import Blueprint, jsonify, request
from service.usuario_service import UsuarioService
from entity.usuario import Usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email_usuario')
    senha = data.get('senha_usuario')
    try:
        usuario = UsuarioService.autenticar_usuario(email, senha)
        return jsonify(usuario.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401

@usuario_bp.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    data = request.get_json()
    usuario = Usuario(
        nome_usuario=data.get('nome_usuario'),
        email_usuario=data.get('email_usuario'),
        senha_usuario=data.get('senha_usuario'),
        data_nascimento_usuario=data.get('data_nascimento_usuario'),
        telefone_usuario=data.get('telefone_usuario')
    )
    try:
        usuario_cadastrado = UsuarioService.cadastrar_usuario(usuario)
        return jsonify(usuario_cadastrado.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    try:
        usuario = UsuarioService.buscar_por_id(id)
        return jsonify(usuario.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
