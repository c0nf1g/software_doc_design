from flask import Blueprint, jsonify
from init_controllers import artist_controller

artist = Blueprint("artist", __name__)


@artist.route('/artists')
def get_artists():
    artists = artist_controller.get_artists()
    result = []

    for artist in artists:
        result.append(artist.get_attrs())

    return jsonify(result)


@artist.route('/artists/<artist_id>')
def get_artist(artist_id):
    artist = artist_controller.get_artist(artist_id)
    return jsonify(artist.get_attrs())
