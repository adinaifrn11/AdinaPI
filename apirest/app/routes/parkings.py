from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.controllers.parking_controller import criar_parking, listar_parkings
from app.controllers.spot_controller import listar_spots_por_parking

parkings_bp = Blueprint("parkings", __name__)


# Rota protegida (precisa de token JWT)
@parkings_bp.route("/", methods=["POST"])
@jwt_required()
def post_parking():
    data = request.get_json()
    response, status = criar_parking(data)
    return jsonify(response), status


# Rota pública
@parkings_bp.route("/", methods=["GET"])
def get_parkings():
    response, status = listar_parkings()
    return jsonify(response), status


# Rota pública
@parkings_bp.route("/<int:parking_id>/spots", methods=["GET"])
def get_spots_by_parking(parking_id):
    response, status = listar_spots_por_parking(parking_id)
    return jsonify(response), status