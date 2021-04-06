from models.PlaylistHasSong import db, PlaylistHasSong
from csv_module.generate_csv import read_from_csv


class PlaylistHasSongDAO:
    def create_association_playlist_song(self, 
                                         playlist_song_id,
                                         is_downloaded, 
                                         stop_time, 
                                         playlist, 
                                         song):
        created_association = PlaylistHasSong(id=playlist_song_id,
                                              is_downloaded=is_downloaded,
                                              stop_time=stop_time,
                                              playlist=playlist,
                                              song=song)
        db.session.add(created_association)
        db.session.commit()

        return created_association

    def get_playlist_song_record(self, playlist_song_id):
        playlist_song = PlaylistHasSong.query.filter_by(id=playlist_song_id).first()
        return playlist_song
        
    def read_playlist_song_from_csv(self, filename):
        return read_from_csv(filename, 'PlaylistHasSong')
    
    def create_playlist_song_from_csv(self, playlist_song_headers, playlist_song_data):
        created_playlist_song = PlaylistHasSong()
        created_playlist_song.from_csv(playlist_song_headers, playlist_song_data)
        db.session.add(created_playlist_song)
        db.session.commit()
