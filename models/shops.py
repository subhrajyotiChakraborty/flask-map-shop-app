from typing import List

from db import db


class ShopModel(db.Model):
    __tablename__ = "shops"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(90), nullable=False)
    store_image = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)

    orders = db.relationship("OrderModel", lazy="dynamic", cascade="all, delete-orphan")

    @classmethod
    def find_all(cls) -> List["ShopModel"]:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> "ShopModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
