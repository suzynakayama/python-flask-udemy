from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'secret_key'   # this should be an env variable. We are doing like this to learn.
api = Api(app)

jwt = JWT(app, authenticate, identity)          # auth

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help='This field cannot be left blank!'
    )

    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        item = next(filter(lambda x: x['name'] == name, items), None)         # next give us the first item of the filter function, and we add the None at the end so it doesn't return an error if there is no next
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        # data = request.get_json(silent=True)                 # force=True means we don't need the content-type in the header, this is dangerous because it will not look in the header. silent=True returns none if this returns an error.
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items            #! use this to tell Python you are using the global items variable here, and not creating a new local items variable
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': f'Item {name} deleted'}
    
    def put(self, name):  # if the item doesn't exits, it creates it.

        data = Item.parser.parse_args()
        # data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)         #! this will update all the item, name and price, unless you use the parser.
        return item

class ItemList(Resource):
    def get(self):
        return {'items': items}



api.add_resource(Item, '/items/<string:name>')  # add resource to the api with this route
api.add_resource(ItemList, '/items')

app.run(port=3005, debug=True)
