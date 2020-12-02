from typing import List

from db import db


class OrderModel(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String, nullable=False)
    order_amount = db.Column(db.Float, nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False)
    store = db.relationship("ShopModel")


    @classmethod
    def find_all(cls) -> List["OrderModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "OrderModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()