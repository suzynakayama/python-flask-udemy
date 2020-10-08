from marshmallow import Schema, fields, INCLUDE

class BookSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    description = fields.Str()            # of import INCLUDE and use it below, but its better to have it on you schema

class Book:
    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

incoming_book_data = {
    'title': 'Clean Code',
    'author': 'Bob Martin',
    'description': 'A book about writing cleaner code.'
}

book_schema = BookSchema()
# book_schema = BookSchema(unknown=INCLUDE)
book = book_schema.load(incoming_book_data)
book_obj = Book(**book)

print(book_obj.title)