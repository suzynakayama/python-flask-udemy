
from ma import ma
from models.store import StoreModel
from models.item import ItemModel
from schemas.item import ItemSchema

class StoreSchema(ma.SQLAlchemyAutoSchema):
    items = ma.Nested(ItemSchema, many=True)        # items is something that is nested within a store and it contains many ItemSchemas
    
    class Meta:
        model = StoreModel               # create marshmallow fields based on our UserModel
        dump_only = ("id",)
        load_instance = True