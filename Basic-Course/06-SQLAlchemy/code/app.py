from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'     # it can be mySQL, PostgreSQL, etc.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # this turns off the Flask SQLAlchemy modification tracker because the SQLAlchemy already has its own tracker
app.secret_key = 'secret_key'  # this should be an env variable. We are doing like this to learn.
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
api = Api(app)

@app.before_first_request       # before any request, create the tables
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)          # auth

api.add_resource(Item, '/items/<string:name>')  # add resource to the api with this route
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/users/register')
api.add_resource(Store, '/stores/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':  # do this because if we import the app in another file the name will not be main (main is the name given to the file we are running), so it will not run the app again
    db.init_app(app)
    app.run(port=3005, debug=True)
