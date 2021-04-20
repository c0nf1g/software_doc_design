from flask import Blueprint, jsonify
from init_layers import playlist_song_service

playlist_song = Blueprint("playlist_song", __name__)


@playlist_song.route('/playlist_song')
def get_users():
    playlists_songs = playlist_song_service.get_playlist_song_records()
    result = []

    for playlist_song in playlists_songs:
        result.append(playlist_song.get_attrs())

    return jsonify(result)


@playlist_song.route('/playlist_song/<playlist_song_id>')
def get_user(playlist_song_id):
    playlist_song = playlist_song_service.get_playlist_song_record(playlist_song_id)
    return jsonify(playlist_song.get_attrs())
