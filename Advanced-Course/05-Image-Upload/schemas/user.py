from ma import ma
from marshmallow import pre_dump
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel               # create marshmallow fields based on our UserModel
        load_only = ("password",)
        dump_only = ("id", "confirmation")
        include_relationships = True
        load_instance = True
    
    @pre_dump
    def _pre_dump(self, user: UserModel, **kwargs):
        """Use to modify the user before dumping. This will change the confirmation to be a list with only the last confirmation"""
        user.confirmation = [user.most_recent_confirmation]
        return user