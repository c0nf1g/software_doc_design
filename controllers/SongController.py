from flask import render_template


class SongController:
    def __init__(self, song_service):
        self.song_service = song_service

    def show_song(self, song_id):
        song = [self.song_service.get_song(song_id=song_id)]
        return render_template('song/song_list.html', songs=song)

    def show_songs(self):
        songs = self.song_service.get_songs()
        return render_template('song/song_list.html', songs=songs)

    def add_song(self, name, duration, artist_id, album_id):
        song = self.song_service.create_song(name, duration, artist_id, album_id)
        return self.show_song(song.id)

    def update_song(self, song_id, name, duration,
                    artist_id, album_id):
        song = self.song_service.update_song(song_id=song_id,
                                             name=name,
                                             duration=duration,
                                             artist_id=artist_id,
                                             album_id=album_id)
        return self.show_song(song.id)

    def delete_song(self, song_id):
        song = self.song_service.delete_song(song_id=song_id)
        return self.show_song(song.id)
