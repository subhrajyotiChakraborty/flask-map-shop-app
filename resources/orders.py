from flask_restful import Resource
from flask import request

from schemas.orders import OrderSchema
from models.orders import OrderModel

order_schema = OrderSchema()
order_list_schema = OrderSchema(many=True)


class Order(Resource):
    @classmethod
    def post(cls):
        order_json = request.get_json()
        order = order_schema.load(order_json)

        try:
            order.save_to_db()
            return {"message": "Order successfully placed"}, 201
        except:
            return {"message": "Error occurred while placing the order"}, 500


class OrderList(Resource):
    @classmethod
    def get(cls):
        return {"orders": order_list_schema.dump(OrderModel.find_all())}, 200
