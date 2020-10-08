from flask_restful import Resource
from flask_uploads import UploadNotAllowed
from flask import request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback
import os

from libs import image_helper
from libs.strings import gettext
from schemas.image import ImageSchema

image_schema = ImageSchema()

class ImageUpload(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        """
        Used to upload an image file.
        It uses JWT to retrieve user info and then saves the image to the user's folder.
        If there is a filename conflict, it appends a number at the end.
        """
        data = image_schema.load(request.files)  # request.files is a dictionary in request that has a key of the name of the filename to the data of the file. The data is always going to be a FileStorage object from Werkzeug because Werkzeug is going to take all the incoming files and is going to wrap it with this FileStorage object. So this is going to be {'image': FileStorage}
        user_id = get_jwt_identity()
        folder = f'user_{user_id}'
        try:
            image_path = image_helper.save_image(data['image'], folder=folder)
            basename = image_helper.get_basename(image_path)
            return {'message': gettext('image_uploaded').format(basename)}, 201
        except UploadNotAllowed:
            extension = image_helper.get_extensions(data['image'])
            return {'message': gettext('image_illegal_extension').format(extension)}, 400


class Image(Resource):
    @classmethod
    @jwt_required
    def get(cls, filename: str):
        """Returns the requseted image if it exists. Looks up inside the logged user's folder"""
        user_id = get_jwt_identity()
        folder = f'user_{user_id}'
        if not image_helper.is_filename_safe(filename):
            return {'message': gettext("image_illegal_file_name").format(filename)}, 400
        
        try:
            return send_file(image_helper.get_path(filename, folder=folder))
        except FileNotFoundError:
            return {'message': gettext("image_not_found").format(filename)}, 404

    @classmethod
    @jwt_required
    def delete(cls, filename: str):
        user_id = get_jwt_identity()
        folder = f'user_{user_id}'
        if not image_helper.is_filename_safe(filename):
            return {'message': gettext("image_illegal_file_name").format(filename)}, 400
        
        try:
            os.remove(image_helper.get_path(filename, folder=folder))
            return {'message': gettext('image_deleted').format(filename)}, 200
        except FileNotFoundError:
            return {'message': gettext("image_not_found").format(filename)}, 404
        except:
            return {'message': gettext("image_delete_failed")}, 500


class AvatarUpload(Resource):
    @classmethod
    @jwt_required
    def put(cls):
        data = image_schema.load(request.files)
        filename = f'user_{get_jwt_identity()}'
        folder = 'avatars'
        avatar_path = image_helper.find_image_any_format(filename, folder)
        if avatar_path:
            try:
                os.remove(avatar_path)
            except:
                return {'message': gettext('avatar_delete_failed')}, 500
        
        try:
            ext = image_helper.get_extension(data['image'].filename)
            avatar = filename + ext
            avatar_path = image_helper.save_image(
                data['image'], folder=folder, name=avatar
            )
            basename = image_helper.get_basename(avatar_path)
            return {'message': gettext('avatar_uploaded').format(basename)}, 200
        except UploadNotAllowed:
            extension = image_helper.get_extensions(data['image'])
            return {'message': gettext('image_illegal_extension').format(extension)}, 400


class Avatar(Resource):
    @classmethod
    def get(cls, user_id: int):
        folder = 'avatars'
        filename = f'user_{user_id}'
        avatar = image_helper.find_image_any_format(filename, folder)
        if avatar:
            return send_file(avatar)
        return {'message': gettext('avatar_not_found')}, 404
