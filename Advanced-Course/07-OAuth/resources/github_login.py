from flask import request, g, url_for
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from oauth import github

from models.user import UserModel


class GithubLogin(Resource):
    @classmethod
    def get(cls):
        return github.authorize(url_for('github.authorized', _external=True))       # _external=True means we want to build the whole address for external purposes


class GithubAuthorize(Resource):
    @classmethod
    def get(cls):
        resp = github.authorized_response()

        if resp is None or resp.get('access_token') is None:
            error_response = {
                'error': request.args['error'],
                'error_description': request.args['error_description']
            }
            return error_response

        g.access_token = resp['access_token']
        github_user = github.get('user')
        github_username = github_user.data['login']
        
        user = UserModel.find_by_username(github_username)

        if not user:
            user = UserModel(username=github_username, password=None)
            user.save_to_db()
        
        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)

        return {'access_token': access_token, 'refresh_token': refresh_token}, 200