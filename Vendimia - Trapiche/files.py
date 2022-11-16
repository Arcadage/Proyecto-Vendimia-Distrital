from flask import Blueprint, send_from_directory
from os import getcwd, path

routes_files = Blueprint("routes_files", __name__)

PATH_FILES = getcwd()

@routes_files.get("/download/<string:name_file>")
def download_image(name_file):
    return send_from_directory(PATH_FILES, path=name_file, as_attachment=True)
