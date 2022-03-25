from flask import Blueprint, jsonify
from init_layers import artist_service

artist = Blueprint("artist", __name__)


@artist.route('/artists')
def get_artists():
    artists = artist_service.get_artists()
    result = []

    for artist in artists:
        result.append(artist.get_attrs())

    return jsonify(result)


@artist.route('/artists/<artist_id>')
def get_artist(artist_id):
    artist = artist_service.get_artist(artist_id)
    return jsonify(artist.get_attrs())
