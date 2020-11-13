from flask_restful import Resource
from flask import request

from schemas.shops import ShopSchema
from models.shops import ShopModel

shop_schema = ShopSchema()
shop_list_schema = ShopSchema(many=True)


class Shop(Resource):
    @classmethod
    def post(cls):
        shops_json = request.get_json()
        shop = shop_schema.load(shops_json)

        try:
            shop.save_to_db()
            return {"message": "Shop successfully created"}, 201
        except:
            return {"message": "Error occurred while creating the shop"}, 500


class ShopList(Resource):
    @classmethod
    def get(cls):
        return {"Shops": shop_list_schema.dump(ShopModel.find_all())}, 200
