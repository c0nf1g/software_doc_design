from models.Song import db, Song
from csv_module.generate_csv import read_from_csv


class SongDAO:
    def create_song(self, name, duration,
                    artist_id, album_id, song_id=None):
        if song_id is None:
            created_song = Song(name=name,
                                duration=duration,
                                artist_id=artist_id,
                                album_id=album_id)
        else:
            created_song = Song(id=song_id,
                                name=name,
                                duration=duration,
                                artist_id=artist_id,
                                album_id=album_id)
        db.session.add(created_song)
        db.session.commit()
        return created_song
    
    def get_song(self, song_id):
        song = Song.query.filter_by(id=song_id).first()
        return song

    def get_songs(self):
        songs = Song.query.all()
        return songs

    def update_song(self, song_id, name,
                    duration, artist_id, album_id):
        song = self.get_song(song_id=song_id)
        song.name = name
        song.duration = duration
        song.artist_id = artist_id
        song.album_id = album_id
        db.session.commit()
        return song

    def delete_song(self, song_id):
        song = self.get_song(song_id=song_id)
        db.session.delete(song)
        db.session.commit()
        return song

    def read_song_from_csv(self, filename):
        return read_from_csv(filename, 'Song')

    def create_song_from_csv(self, song_headers, song_data):
        created_song = Song()
        created_song.from_csv(song_headers, song_data)
        db.session.add(created_song)
        db.session.commit()
