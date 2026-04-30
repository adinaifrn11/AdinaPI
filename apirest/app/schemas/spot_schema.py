from marshmallow import fields
from app.extensions import ma
from app.models.spot import ParkingSpot


class SpotSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ParkingSpot

    id = ma.auto_field(dump_only=True)
    codigo = ma.auto_field(required=True)
    ocupada = fields.Boolean(required=True)
    parking_id = ma.auto_field(required=True)