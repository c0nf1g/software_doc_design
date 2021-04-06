from models.Playlist import db, Playlist
from csv_module.generate_csv import read_from_csv


class PlaylistDAO:
    def create_playlist(self, playlist_id, name, user_id):
        created_playlist = Playlist(id=playlist_id,
                                    name=name,
                                    user_id=user_id)
        db.session.add(created_playlist)
        db.session.commit()

        return created_playlist

    def get_playlist(self, playlist_id):
        playlist = Playlist.query.filter_by(id=playlist_id)
        return playlist

    def read_playlist_from_csv(self, filename):
        return read_from_csv(filename, 'Playlist')

    def create_playlist_from_csv(self, playlist_headers, playlist_data):
        created_playlist = Playlist()
        created_playlist.from_csv(playlist_headers, playlist_data)
        db.session.add(created_playlist)
        db.session.commit()
