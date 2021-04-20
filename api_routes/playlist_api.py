from flask import Blueprint, jsonify
from init_layers import playlist_service

playlist = Blueprint("playlist", __name__)


@playlist.route('/playlists')
def get_playlists():
    playlists = playlist_service.get_playlists()
    result = []

    for playlist in playlists:
        result.append(playlist.get_attrs())

    return jsonify(result)


@playlist.route('/playlists/<playlist_id>')
def get_playlist(playlist_id):
    playlist = playlist_service.get_playlist(playlist_id)
    return jsonify(playlist.get_attrs())