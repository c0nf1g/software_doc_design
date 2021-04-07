from flask import Blueprint, jsonify
from init_controllers import album_controller

album = Blueprint("album", __name__)


@album.route('/albums')
def get_albums():
    albums = album_controller.get_albums()
    result = []

    for album in albums:
        result.append(album.get_attrs())

    return jsonify(result)


@album.route('/albums/<album_id>')
def get_album(album_id):
    album = album_controller.get_album(album_id)
    return jsonify(album.get_attrs())