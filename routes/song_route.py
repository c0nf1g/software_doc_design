from flask import Blueprint, jsonify
from init_controllers import song_controller

song = Blueprint("song", __name__)


@song.route('/songs')
def get_songs():
    songs = song_controller.get_songs()
    result = []

    for song in songs:
        result.append(song.get_attrs())

    return jsonify(result)


@song.route('/songs/<song_id>')
def get_song(song_id):
    song = song_controller.get_song(song_id)
    return jsonify(song.get_attrs())