import os
from typing import List

import stripe

from db import db

CURRENCY = 'usd'

## implement the many to many relationships with SQLAlchemy - an order can have many items and an item can be in many orders. Create a secondary table
# items_to_orders = db.Table(
#     'items_to_orders',
#     db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
#     db.Column('order_id', db.Integer, db.ForeignKey('orders.id')),
    # db.Column('quantity', db.Integer), ==> this won't work. In order to know the quantity of items we need to create an association object in our order resource and we will create the Model below instead of using the code above.
# )

class ItemsInOrder(db.Model):
    __tablename__ = 'items_in_orders'

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    quantity = db.Column(db.Integer)

    item = db.relationship('ItemModel')
    order = db.relationship('OrderModel', back_populates='items')


class OrderModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20), nullable=False)

# the back_populates makes the changes in both related models. You can also use back_ref instead, but it is more complex.
    items = db.relationship('ItemsInOrder', back_populates='order')  # self.items[0...x].item
    
    @property
    def description(self):
        """
        Generates a simple string representing this order, in the format of '5x chais, 2x table'
        """
        item_counts = [f'{i.quantity}x {i.item.name}' for i in self.items]
        return ','.join(item_counts)

    @property
    def amount(self):
        return int(sum([item_data.item.price * item_data.quantity for item_data in self.items]) * 100)

    @classmethod
    def find_all(cls) -> List['OrderModel']:
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int) -> 'OrderModel':
        return cls.query.filter_by(ud=_id).first()

    def set_status(self, new_status: str) -> None:
        self.status = new_status
        self.save_to_db()

    def charge_with_stripe(self, token: str) -> stripe.Charge:
        stripe.api_key = os.getenv('STRIPE_API_KEY')

        return stripe.Charge.create(
            amount=self.amount,         # in cents ($1 = 100)
            currency=CURRENCY,
            description=self.description,
            source=token
        )
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
