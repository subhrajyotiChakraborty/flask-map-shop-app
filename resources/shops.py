from flask_restful import Resource
from flask import request

from schemas.shops import ShopSchema
from models.shops import ShopModel

shop_schema = ShopSchema()
shop_list_schema = ShopSchema(many=True)


class Shop(Resource):
    @classmethod
    def post(cls):
        shop_json = request.get_json()
        shop = shop_schema.load(shop_json)

        try:
            shop.save_to_db()
            return {"message": "Shop successfully created"}, 201
        except:
            return {"message": "Error occurred while creating the shop"}, 500


class DeleteShop(Resource):
    @classmethod
    def delete(cls, shopId: int):
        shop = ShopModel.find_by_id(shopId)

        if shop:
            try:
                shop.delete_from_db()
                return {"message": "Shop deleted successfully"}, 200
            except:
                return {"message": "Error occurred while deleting the shop"}, 500

        return {"message": f"Shop with id {shopId} is not found"}, 404


class ShopList(Resource):
    @classmethod
    def get(cls):
        return {"shops": shop_list_schema.dump(ShopModel.find_all())}, 200
