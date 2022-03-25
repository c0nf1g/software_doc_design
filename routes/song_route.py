from flask import render_template, request
from init_layers import song_controller
from . import song


@song.route('/song_view', methods=['GET'])
def song_index():
    return render_template('song/song_index.html')


@song.route('/song_view/get', methods=['GET'])
def get_songs():
    if request.args.get('id', None):
        song_id = int(request.args['id'])
        return song_controller.show_song(song_id=song_id)

    return song_controller.show_songs()


@song.route('/song_view/post', methods=['POST'])
def add_song():
    name = request.form.get('name')
    duration = request.form.get('duration')
    artist_id = request.form.get('artist_id')
    album_id = request.form.get('album_id')

    return song_controller.add_song(name, duration, artist_id, album_id)


@song.route('/song_view/put', methods=['POST'])
def update_song():
    song_id = request.form.get('id')
    name = request.form.get('name')
    duration = request.form.get('duration')
    artist_id = request.form.get('artist_id')
    album_id = request.form.get('album_id')

    return song_controller.update_song(song_id=song_id,
                                       name=name,
                                       duration=duration,
                                       artist_id=artist_id,
                                       album_id=album_id)


@song.route('/song_view/delete', methods=['POST'])
def delete_song():
    song_id = request.form.get('id')
    return song_controller.delete_song(song_id=song_id)
