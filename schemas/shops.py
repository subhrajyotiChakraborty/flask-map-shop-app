from ma import ma
from models.shops import ShopModel
from schemas.orders import OrderSchema


class ShopSchema(ma.SQLAlchemyAutoSchema):
    orders = ma.Nested(OrderSchema, many=True)

    class Meta:
        model = ShopModel
        dump_only = ("id",)
        load_instance = True
