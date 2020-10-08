from ma import ma
from models.item import ItemModel
from models.store import StoreModel

class ItemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemModel               # create marshmallow fields based on our UserModel
        load_only = ("store",)
        dump_only = ("id",)
        include_fk = True               # include foreign keys
        load_instance = True