from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from dotenv import load_dotenv
from flask_cors import CORS

from db import db
from ma import ma
from resources.shops import Shop, ShopList, DeleteShop, EditShop
from resources.orders import Order, OrderList, EditOrder, DeleteOrder

app = Flask(__name__)
CORS(app)

# For dev purpose
# load_dotenv(".env", verbose=True)
# app.config.from_object("default_config")
# app.config.from_envvar("APPLICATION_SETTINGS")

# For production purpose
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTINGS")

api = Api(app)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages, 400)

# For Shop
api.add_resource(Shop, "/shop")
api.add_resource(ShopList, "/shops")
api.add_resource(EditShop, "/shop/<int:shopId>")
api.add_resource(DeleteShop, "/shop/<int:shopId>")

# For Order
api.add_resource(Order, "/order")
api.add_resource(OrderList, "/orders")
api.add_resource(EditOrder, "/order/<int:orderId>")
api.add_resource(DeleteOrder, "/order/<int:orderId>")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(debug=True)
