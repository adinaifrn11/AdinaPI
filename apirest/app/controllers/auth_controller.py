from flask import request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User


def login():
    # Recebe os dados enviados no corpo da requisição
    dados = request.get_json()

    # Obtém email e senha do JSON
    email = dados.get("email")
    senha = dados.get("senha")

    # Procura o usuário pelo email
    usuario = User.query.filter_by(email=email).first()

    # Verifica se o usuário existe
    if not usuario:
        return jsonify({
            "success": False,
            "message": "Email ou senha inválidos."
        }), 401

    # Verifica se a senha está correta
    if not check_password_hash(usuario.senha, senha):
        return jsonify({
            "success": False,
            "message": "Email ou senha inválidos."
        }), 401

    # Gera o token JWT
    token = create_access_token(identity=usuario.id)

    # Retorna o token
    return jsonify({
        "success": True,
        "access_token": token
    }), 200