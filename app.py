from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "Olá mundo"})

@app.route("/mensagens", methods=["GET"])
def listar_mensagens():
    return jsonify({
        "mensagens": [
            "Primeira mensagem",
            "Segunda mensagem"
        ]
    })