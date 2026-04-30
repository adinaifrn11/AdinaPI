from app.extensions import db
from app.models.parking import Parking
from app.schemas.parking_schema import ParkingSchema
from app.utils.response import success_response


parking_schema = ParkingSchema()
parkings_schema = ParkingSchema(many=True)


def criar_parking(data):
    dados_validados = parking_schema.load(data)

    novo = Parking(**dados_validados)

    db.session.add(novo)
    db.session.commit()

    return success_response(parking_schema.dump(novo), 201)


def listar_parkings():
    parkings = Parking.query.all()
    return success_response(parkings_schema.dump(parkings))