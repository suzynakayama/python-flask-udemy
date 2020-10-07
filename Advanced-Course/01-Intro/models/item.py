from typing import Dict, List, Union

from db import db

# * Below we are defining our custom type. It will be a dictionary and we ALWAYS use 'square brackets' []! The first parameter will be the keys type, in our case, str; the second parameter will be a Union of int, str and float, because our values can be any of those.
ItemJSON = Dict[str, Union[int, str, float]]


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)  # names are unique
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    store = db.relationship("StoreModel")

    def __init__(self, name: str, price: float, store_id: int):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self) -> ItemJSON:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "store_id": self.store_id,
        }

    @classmethod
    def find_by_name(
        cls, name: str
    ) -> "ItemModel":  # * In order to use the class as a type, we need to use within 'quotes' "".
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> List["ItemModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
