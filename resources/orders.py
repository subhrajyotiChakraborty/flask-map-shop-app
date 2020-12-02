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


class EditOrder(Resource):
    @classmethod
    def put(cls, orderId: int):
        order_json = request.get_json()
        order = OrderModel.find_by_id(orderId)

        if order:
            order.store_id = order_json["store_id"]
            order.order_amount = order_json["order_amount"]
            order.order_number = order_json["order_number"]

            try:
                order.save_to_db()
            except:
                return {"message": "Error occurred while updating Order information"}, 500

            return order_schema.dump(order), 200

        return {"message": f"Order with ID {orderId} is not found"}, 404


class OrderList(Resource):
    @classmethod
    def get(cls):
        return {"orders": order_list_schema.dump(OrderModel.find_all())}, 200


class DeleteOrder(Resource):
    @classmethod
    def delete(cls, orderId: int):
        order = OrderModel.find_by_id(orderId)
        if order:
            try:
                order.delete_from_db()
            except:
                return {"message": "Error occurred while deleting the Order"}, 500

            return {"message": "Order deleted successfully"}, 200
        return {"message": f"Order with ID {orderId} is not found"}, 404
