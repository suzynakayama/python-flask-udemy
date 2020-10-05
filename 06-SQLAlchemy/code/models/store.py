import sqlite3
from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel', lazy='dynamic')  ## list of ItemModels, using the lazy='dynamic' helps us to create stores easily and fast, since we won't have to go to ItemModel every time

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}  #* use the .all() because we used the lazy='dynamic' on the relationship and now self.items is a query builder. Also, because of that, every time we call the json method we have to go to the table, so now the json method is slower.

    @classmethod                            # should still be a classmethod because we are returning an object of type ItemModel instead of a dictionary
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()     # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    