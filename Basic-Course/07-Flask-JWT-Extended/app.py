from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db

from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True  # with this, our Flask app will return the proper error and, extensions will be able to propagate their specific/custom errors. Otherwise we will always get a 500.
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'mysupersecretkey'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWTManager(app)  # link the JWTManager with the app

"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""
#* add the decorator below to add claims to the jwt - what happens is: whenever we create a new access token, we are going to will run this function to see if we need to add any extra data to that JWT as well
@jwt.user_claims_loader
def add_claims_to_jwt(identity):        # identity, in our case, will be the user_id, since this is what we pass to identity in the UserLogin POST
    if identity == 1:       # instead of hard-coding, you should read from a config file or a db
        return {'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401

@jwt.invalid_token_loader
# called when token sent on the authorization header is not an actual jwt token
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed',
        'error': 'invalid_token'
    }), 401

@jwt.unauthorized_loader        # called when they don't send us a jwt at all
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token',
        'error': 'authorization_required'
    }), 401

@jwt.needs_fresh_token_loader       # called when they don't send us a fresh token, but we need a fresh one
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401

@jwt.revoked_token_loader  # called when the token sent was revoked
def revoked_token_callback():
    return jsonify({
        'description': 'Token has been revoked.',
        'error': 'token_revoked'
    }), 401

api.add_resource(Store, '/stores/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/items/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/users/register')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserLogin, '/users/login')
api.add_resource(TokenRefresh, '/users/refresh')
api.add_resource(UserLogout, '/users/logout')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=3005, debug=True)
