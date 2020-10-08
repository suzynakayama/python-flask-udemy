from marshmallow import Schema, fields
from typing import Union
from werkzeug.datastructures import FileStorage

class FileStorageField(fields.Field):
    default_error_messages = {
        'invalid': 'Not a valid image.'
    }

    def _deserialize(self, value, attr, data, **kwargs) -> Union[FileStorage, None]:
        if value is None:
            return None
        
        if not isinstance(value, FileStorage):
            self.fail('invalid')        #raises ValidationError

        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)