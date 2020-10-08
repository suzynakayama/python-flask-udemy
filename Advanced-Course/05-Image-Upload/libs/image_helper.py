import os
import re
from typing import Union
from werkzeug.datastructures import FileStorage

from flask_uploads import UploadSet, IMAGES

IMAGE_SET = UploadSet('images', IMAGES)         # set the name images and the allowed extensions

def save_image(image: FileStorage, folder: str = None, name: str = None) -> str:
    """Takes FileStorage and saves it to a folder"""
    return IMAGE_SET.save(image, folder, name)

def get_path(filename: str = None, folder: str = None) -> str:
    """Take image name and folder and return full path"""
    return IMAGE_SET.path(filename, folder)

def find_image_any_format(filename: str, folder: str) -> Union[str, None]:
    """Takes a filename and return an image on any of the accepted formats"""
    for _format in IMAGES:
        image = f'{filename}.{_format}'
        image_path = IMAGE_SET.path(filename=image, folder=folder)
        if os.path.isfile(image_path):
            return image_path
    return None

def _retrieve_filename(file: Union[str, FileStorage]) -> str:
    """Takes FileStorage and and return the file name
    Allows our functions to call this with both file names and
    fileStorages and always gets back a file name
    """
    if isinstance(file, FileStorage):
        return file.filename
    return file

def is_filename_safe(file: Union[str, FileStorage]) -> bool:
    """Check our regex and return whether the string matches or not"""
    filename = _retrieve_filename(file)

    allowed_format = '|'.join(IMAGES)  # png|svg|jpe|jpg|jpeg
    regex = f'^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$'
    return re.match(regex, filename) is not None

def get_basename(file: Union[str, FileStorage]) -> str:
    """Return full name of image in the path
    get_basename('some/folder/image.jpg') return 'image.jpg'
    """
    filename = _retrieve_filename(file)
    return os.path.split(filename)[1]

def get_extension(file: Union[str, FileStorage]) -> str:
    """Return full extension
    get_extension('image.jpg') return 'jpg'
    """
    filename = _retrieve_filename(file)
    return os.path.splitext(filename)[1]