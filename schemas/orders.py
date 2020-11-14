from ma import ma
from models.orders import OrderModel


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OrderModel
        load_only = ("store",)
        dump_only = ("id",)
        include_fk = True
        load_instance = True
