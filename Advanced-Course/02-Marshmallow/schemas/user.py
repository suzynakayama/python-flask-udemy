from ma import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel               # create marshmallow fields based on our UserModel
        load_only = ("password",)
        dump_only = ("id",)
        load_instance = True


# class UserSchema(Schema):
#     class Meta:                             # create a Meta class inside the Schema to define the load_only and the dump_only
#         load_only = ("password",)           # * Password is load_only, we are only going to use when we load, we are never going to return the password --> Note: we usa a tuple
#         dump_only = ("id",)                 # * Id is dump_only, we are only going to use when we return, we are never going to send the id when we load --> Note: we usa a tuple
#     id = fields.Int()   
#     username = fields.Str(required=True)
#     password = fields.Str(required=True)
