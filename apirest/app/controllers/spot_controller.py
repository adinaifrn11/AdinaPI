from app.extensions import db
from app.models.spot import ParkingSpot
from app.models.parking import Parking
from app.schemas.spot_schema import SpotSchema
from app.utils.response import success_response, error_response


spot_schema = SpotSchema()
spots_schema = SpotSchema(many=True)


def criar_spot(data):
    dados_validados = spot_schema.load(data)

    parking = Parking.query.get(dados_validados["parking_id"])
    if not parking:
        return error_response("Recurso nao encontrado", 404)

    novo = ParkingSpot(**dados_validados)

    db.session.add(novo)
    db.session.commit()

    return success_response(spot_schema.dump(novo), 201)


def listar_spots():
    spots = ParkingSpot.query.all()
    return success_response(spots_schema.dump(spots))


def atualizar_spot(id, data):
    spot = ParkingSpot.query.get(id)
    if not spot:
        return error_response("Recurso nao encontrado", 404)

    spot.ocupada = data.get("ocupada", spot.ocupada)

    db.session.commit()

    return success_response(spot_schema.dump(spot))


def listar_spots_por_parking(parking_id):
    parking = Parking.query.get(parking_id)
    if not parking:
        return error_response("Recurso nao encontrado", 404)

    return success_response(spots_schema.dump(parking.spots))