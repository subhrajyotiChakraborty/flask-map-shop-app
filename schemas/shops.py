from ma import ma
from models.shops import ShopModel


class ShopSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ShopModel
        dump_only = ("id",)
        load_instance = True
